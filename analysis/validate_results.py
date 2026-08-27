from pathlib import Path
import pandas as pd

OUTPUTS = Path(__file__).resolve().parent / "outputs"


def close(value, expected, tolerance):
    return abs(float(value) - expected) <= tolerance


def status(ok):
    return "✓" if ok else "⚠"


def main():
    checks = []

    perfil = pd.read_csv(OUTPUTS / "perfil.csv")
    p2 = perfil.loc[perfil["number_of_bedrooms"].eq(2)].iloc[0]
    checks.append(("2Q permanece o perfil mais eficiente", perfil.iloc[0]["number_of_bedrooms"] == 2))
    checks.append(("Eficiência 2Q próxima de 0,060%/dia", close(p2["eficiencia_pct_dia"], 0.060, 0.006)))

    loc = pd.read_csv(OUTPUTS / "localizacao.csv").set_index("zona")
    checks.append(("Orla tem diária mediana superior ao Interior", loc.loc["Orla", "diaria_mediana"] > loc.loc["Interior", "diaria_mediana"]))
    checks.append(("Diária Orla próxima de R$594", close(loc.loc["Orla", "diaria_mediana"], 594, 35)))
    checks.append(("Diária Interior próxima de R$477", close(loc.loc["Interior", "diaria_mediana"], 477, 35)))

    reg = pd.read_csv(OUTPUTS / "regressao.csv").set_index("variavel")
    checks.append(("Regressão usa aproximadamente 999 listings", close(reg.iloc[0]["n"], 999, 20)))
    checks.append(("R² próximo de 0,41", close(reg.iloc[0]["r2"], 0.41, 0.06)))
    checks.append(("Quartos associado positivamente à diária", reg.loc["quartos", "coeficiente_log"] > 0))
    checks.append(("Orla associada positivamente à diária", reg.loc["orla", "coeficiente_log"] > 0))

    be = pd.read_csv(OUTPUTS / "break_even.csv")
    interior = be[(be["zona"] == "Interior") & (be["number_of_bedrooms"] == 2)].iloc[0]
    orla = be[(be["zona"] == "Orla") & (be["number_of_bedrooms"] == 2)].iloc[0]
    checks.append(("2Q Interior exige menos ocupação que 2Q Orla para 8%", interior["ocupacao_para_8pct"] < orla["ocupacao_para_8pct"]))
    checks.append(("Break-even 2Q Interior próximo de 44%", close(interior["ocupacao_para_8pct"], 0.44, 0.05)))
    checks.append(("Break-even 2Q Orla próximo de 54%", close(orla["ocupacao_para_8pct"], 0.54, 0.05)))

    centro = pd.read_csv(OUTPUTS / "tese_centro.csv")
    c1 = centro.loc[centro["number_of_bedrooms"].eq(1)]
    c2 = centro.loc[centro["number_of_bedrooms"].eq(2)]
    checks.append(("Centro 1Q tem evidência de preço", len(c1) == 1 and pd.notna(c1.iloc[0]["diaria_mediana"])))
    checks.append(("Centro 2Q é pelo menos tão eficiente quanto 1Q", len(c1) == 1 and len(c2) == 1 and c2.iloc[0]["eficiencia_pct_dia"] >= c1.iloc[0]["eficiencia_pct_dia"] * 0.95))

    print("VALIDAÇÃO DOS RESULTADOS PUBLICADOS")
    print("=" * 42)
    passed = 0
    for label, ok in checks:
        print(f"{status(ok)} {label}")
        passed += int(bool(ok))
    print()
    print(f"{passed}/{len(checks)} verificações dentro do esperado")
    if passed != len(checks):
        print("ATENÇÃO: divergências devem ser investigadas; não ajuste o código apenas para fazê-lo bater com o README.")


if __name__ == "__main__":
    main()
