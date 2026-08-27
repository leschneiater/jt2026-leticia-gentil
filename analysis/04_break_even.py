import pandas as pd
from common import apartment_airbnb, apartment_sales, write_csv

TARGETS = [0.06, 0.08, 0.10]


def _annual_fixed_costs(group: pd.DataFrame) -> float:
    iptu = pd.to_numeric(group["yearly_iptu"], errors="coerce")
    condo = pd.to_numeric(group["monthly_condo_fee"], errors="coerce")
    yearly = iptu.fillna(0) + condo.fillna(0) * 12
    yearly = yearly[yearly > 0]
    return float(yearly.median()) if len(yearly) else 0.0


def build_break_even_table() -> pd.DataFrame:
    air = apartment_airbnb(validated_prices=True).dropna(subset=["diaria_mediana", "number_of_bedrooms"])
    sales = apartment_sales().dropna(subset=["sale_price", "bedrooms"])

    daily = (
        air.groupby(["zona", "number_of_bedrooms"], as_index=False)
        .agg(diaria_mediana=("diaria_mediana", "median"), n_series=("airbnb_listing_id", "nunique"))
    )

    sale_rows = []
    for (zona, quartos), g in sales.groupby(["zona", "bedrooms"]):
        sale_rows.append({
            "zona": zona,
            "number_of_bedrooms": quartos,
            "venda_mediana": float(g["sale_price"].median()),
            "custos_fixos_anuais_medianos": _annual_fixed_costs(g),
            "n_vendas": int(g["listing_id"].nunique()),
        })
    sale = pd.DataFrame(sale_rows)
    out = daily.merge(sale, on=["zona", "number_of_bedrooms"], how="inner")

    for target in TARGETS:
        col = f"ocupacao_para_{int(target*100)}pct"
        out[col] = (
            target * out["venda_mediana"] + out["custos_fixos_anuais_medianos"]
        ) / (out["diaria_mediana"] * 365)

    out = out.sort_values(["number_of_bedrooms", "zona"])
    write_csv(out, "break_even.csv")
    return out


if __name__ == "__main__":
    print(build_break_even_table().to_string(index=False))
