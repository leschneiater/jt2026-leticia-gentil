import math
import numpy as np
import pandas as pd
import statsmodels.api as sm
from common import airbnb_base, as_bool, load_hosts, write_csv


def run_regression() -> pd.DataFrame:
    df = airbnb_base(validated_prices=False).dropna(subset=["diaria_mediana", "number_of_bedrooms"]).copy()
    hosts = load_hosts()[["owner_id", "is_superhost"]]
    df = df.merge(hosts, on="owner_id", how="left", suffixes=("", "_host"))

    df["log_diaria"] = np.log(df["diaria_mediana"].clip(lower=1))
    df["quartos"] = df["number_of_bedrooms"]
    df["profissional"] = as_bool(df["is_professional"])
    df["orla"] = df["zona"].eq("Orla").astype(float)
    df["superhost"] = as_bool(df["is_superhost"])
    df["guest_favorite"] = as_bool(df["is_guest_favorite"])
    df["log_reviews"] = np.log1p(df["number_of_reviews"].fillna(0))

    cols = ["quartos", "profissional", "orla", "superhost", "guest_favorite", "log_reviews"]
    model_df = df[["log_diaria"] + cols].replace([np.inf, -np.inf], np.nan).dropna()
    X = sm.add_constant(model_df[cols])
    model = sm.OLS(model_df["log_diaria"], X).fit()

    rows = []
    for name in cols:
        coef = float(model.params[name])
        rows.append({
            "variavel": name,
            "coeficiente_log": coef,
            "associacao_pct_aprox": (math.exp(coef) - 1) * 100,
            "p_value": float(model.pvalues[name]),
            "n": int(model.nobs),
            "r2": float(model.rsquared),
        })
    out = pd.DataFrame(rows)
    write_csv(out, "regressao.csv")
    return out


if __name__ == "__main__":
    print(run_regression().to_string(index=False))
