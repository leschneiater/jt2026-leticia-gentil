import pandas as pd
from common import (
    MIN_SEGMENT_N,
    apartment_airbnb,
    apartment_sales,
    write_csv,
)


def build_profile_table() -> pd.DataFrame:
    air = apartment_airbnb(validated_prices=True).dropna(subset=["diaria_mediana", "number_of_bedrooms"])
    sales = apartment_sales().dropna(subset=["sale_price", "bedrooms"])

    daily = (
        air.groupby("number_of_bedrooms", as_index=False)
        .agg(diaria_mediana=("diaria_mediana", "median"), n_series=("airbnb_listing_id", "nunique"))
    )
    sale = (
        sales.groupby("bedrooms", as_index=False)
        .agg(venda_mediana=("sale_price", "median"), n_vendas=("listing_id", "nunique"))
        .rename(columns={"bedrooms": "number_of_bedrooms"})
    )
    out = daily.merge(sale, on="number_of_bedrooms", how="inner")
    out = out[(out["n_series"] >= MIN_SEGMENT_N) & (out["n_vendas"] >= MIN_SEGMENT_N)].copy()
    out["eficiencia_pct_dia"] = out["diaria_mediana"] / out["venda_mediana"] * 100
    out = out.sort_values("eficiencia_pct_dia", ascending=False)
    write_csv(out, "perfil.csv")
    return out


if __name__ == "__main__":
    df = build_profile_table()
    print(df.to_string(index=False))
