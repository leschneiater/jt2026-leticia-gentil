import importlib

STEPS = [
    ("01_perfil", "build_profile_table"),
    ("02_localizacao", "build_location_table"),
    ("03_regressao", "run_regression"),
    ("04_break_even", "build_break_even_table"),
    ("05_tese_centro", "build_centro_table"),
]


def main() -> None:
    print("REPRODUCAO DA ANALISE — JT2026 LETICIA GENTIL")
    print("=" * 50)
    for i, (module_name, fn_name) in enumerate(STEPS, start=1):
        print(f"[{i}/{len(STEPS)}] {module_name}")
        module = importlib.import_module(module_name)
        fn = getattr(module, fn_name)
        df = fn()
        print(f"  ✓ {len(df)} linhas geradas")
    print()
    print("Resultados salvos em analysis/outputs/")
    print("Agora execute: python analysis/validate_results.py")


if __name__ == "__main__":
    main()
