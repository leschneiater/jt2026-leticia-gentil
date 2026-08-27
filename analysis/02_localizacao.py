import pandas as pd
from common import airbnb_base, load_details, load_mesh, write_csv


def build_location_table() -> pd.DataFrame:
    details = load_details()[["airbnb_listing_id"]]
    mesh = load_mesh()[["airbnb_listing_id", "suburb"]]
    all_listings = details.merge(mesh, on="airbnb_listing_id", how="left")
    all_listings["zona"] = all_listings["suburb"].isin({"Meia Praia", "Centro", "Canto da Praia"}).map({True: "Orla", False: "Interior"})

    priced = airbnb_base(validated_prices=False).dropna(subset=["diaria_mediana"])

    supply = (
        all_listings.groupby("zona", as_index=False)
        .agg(anuncios=("airbnb_listing_id", "nunique"))
    )
    daily = (
        priced.groupby("zona", as_index=False)
        .agg(
            diaria_mediana=("diaria_mediana", "median"),
            anuncios_com_preco=("airbnb_listing_id", "nunique"),
        )
    )
    out = supply.merge(daily, on="zona", how="left")
    out["share_oferta_pct"] = out["anuncios"] / out["anuncios"].sum() * 100
    out["presenca_price_av_pct"] = out["anuncios_com_preco"] / out["anuncios"] * 100
    write_csv(out, "localizacao.csv")
    return out


if __name__ == "__main__":
    print(build_location_table().to_string(index=False))
