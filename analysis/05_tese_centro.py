import pandas as pd
from common import apartment_airbnb, apartment_sales, write_csv


def build_centro_table() -> pd.DataFrame:
    air = apartment_airbnb(validated_prices=True)
    air = air[air["suburb"].eq("Centro")].dropna(subset=["number_of_bedrooms"])
    sales = apartment_sales()
    sales = sales[sales["suburb"].eq("Centro")].dropna(subset=["bedrooms"])

    daily = (
        air.groupby("number_of_bedrooms", as_index=False)
        .agg(diaria_mediana=("diaria_mediana", "median"), n_series=("airbnb_listing_id", "nunique"))
    )
    sale = (
        sales.groupby("bedrooms", as_index=False)
        .agg(venda_mediana=("sale_price", "median"), n_vendas=("listing_id", "nunique"))
        .rename(columns={"bedrooms": "number_of_bedrooms"})
    )
    out = sale.merge(daily, on="number_of_bedrooms", how="left")
    out["eficiencia_pct_dia"] = out["diaria_mediana"] / out["venda_mediana"] * 100
    out = out.sort_values("number_of_bedrooms")
    write_csv(out, "tese_centro.csv")
    return out


if __name__ == "__main__":
    print(build_centro_table().to_string(index=False))
