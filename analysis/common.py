from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = Path(__file__).resolve().parent / "outputs"
OUTPUTS.mkdir(exist_ok=True)

ORLA_BAIRROS = {"Meia Praia", "Centro", "Canto da Praia"}
MIN_SALE_PRICE = 50_000
MIN_SERIES_OBS = 40
MIN_SERIES_MONTHS = 2
MIN_SEGMENT_N = 30


def _read(name: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(DATA / name, low_memory=False, **kwargs)


def load_details() -> pd.DataFrame:
    df = _read("Details_Itapema.csv", dtype={"airbnb_listing_id": str, "owner_id": str})
    return df


def load_mesh() -> pd.DataFrame:
    return _read("Mesh_Ids_Data_Itapema.csv", dtype={"airbnb_listing_id": str})


def load_hosts() -> pd.DataFrame:
    df = _read("Hosts_ids_Itapema.csv", dtype={"owner_id": str})
    df["host_snapshot_date"] = pd.to_datetime(df["host_snapshot_date"], errors="coerce")
    # Um owner aparece em mais de um snapshot; usamos o registro mais recente.
    df = df.sort_values("host_snapshot_date").drop_duplicates("owner_id", keep="last")
    return df


def load_prices() -> pd.DataFrame:
    df = _read("Price_AV_Itapema.csv", dtype={"airbnb_listing_id": str})
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df.dropna(subset=["date", "price"])


def load_sales() -> pd.DataFrame:
    df = _read("VivaReal_Itapema.csv", dtype={"listing_id": str})
    for col in ["sale_price", "yearly_iptu", "monthly_condo_fee", "bedrooms", "usable_area"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df[df["sale_price"].ge(MIN_SALE_PRICE)].copy()
    df["zona"] = df["suburb"].apply(zone_from_suburb)
    return df


def zone_from_suburb(suburb) -> str:
    return "Orla" if suburb in ORLA_BAIRROS else "Interior"


def as_bool(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().map({"true": 1.0, "false": 0.0}).fillna(0.0)


def listing_prices(validated: bool = False) -> pd.DataFrame:
    """Uma linha por listing com a mediana da série Price_AV.

    `validated=True` aplica a regra documentada na sessão: pelo menos 40
    observações de preço e presença em pelo menos dois meses distintos.
    """
    prices = load_prices().copy()
    prices["month"] = prices["date"].dt.to_period("M").astype(str)
    out = (
        prices.groupby("airbnb_listing_id", as_index=False)
        .agg(
            diaria_mediana=("price", "median"),
            n_obs=("price", "size"),
            n_meses=("month", "nunique"),
            data_min=("date", "min"),
            data_max=("date", "max"),
        )
    )
    if validated:
        out = out[(out["n_obs"] >= MIN_SERIES_OBS) & (out["n_meses"] >= MIN_SERIES_MONTHS)].copy()
    return out


def airbnb_base(validated_prices: bool = False) -> pd.DataFrame:
    details = load_details()
    mesh = load_mesh()[["airbnb_listing_id", "suburb", "latitude", "longitude"]]
    px = listing_prices(validated=validated_prices)
    df = details.merge(mesh, on="airbnb_listing_id", how="left").merge(px, on="airbnb_listing_id", how="left")
    df["zona"] = df["suburb"].apply(zone_from_suburb)
    df["number_of_bedrooms"] = pd.to_numeric(df["number_of_bedrooms"], errors="coerce")
    df["number_of_reviews"] = pd.to_numeric(df["number_of_reviews"], errors="coerce")
    return df


def apartment_airbnb(validated_prices: bool = False) -> pd.DataFrame:
    df = airbnb_base(validated_prices=validated_prices)
    return df[df["listing_type"].astype(str).str.lower().eq("apartamento")].copy()


def apartment_sales() -> pd.DataFrame:
    df = load_sales()
    return df[df["listing_type"].astype(str).str.lower().eq("apartamento")].copy()


def write_csv(df: pd.DataFrame, name: str) -> Path:
    path = OUTPUTS / name
    df.to_csv(path, index=False)
    return path
