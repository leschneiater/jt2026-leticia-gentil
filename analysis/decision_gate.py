"""Gate auditável da decisão final do hackathon.

Este script NÃO reconstrói a análise original a partir dos CSVs e não deve ser
interpretado como tal. Ele torna reproduzível apenas a camada final de decisão,
usando os parâmetros já publicados no relatório/README.

Objetivo:
- deixar explícito que 2Q Interior é o baseline de menor risco;
- testar o hurdle de 8% do 2Q Orla;
- registrar a condição objetiva de reversão.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Segmento:
    nome: str
    preco_compra: float
    ocupacao_6: float
    ocupacao_8: float
    ocupacao_10: float


INTERIOR_2Q = Segmento(
    nome="2Q Interior",
    preco_compra=750_000,
    ocupacao_6=0.33,
    ocupacao_8=0.44,
    ocupacao_10=0.54,
)

ORLA_2Q = Segmento(
    nome="2Q Orla",
    preco_compra=1_100_000,
    ocupacao_6=0.42,
    ocupacao_8=0.54,
    ocupacao_10=0.67,
)

# Parâmetros do cenário mecânico publicado para 2Q Orla.
DIARIA_ORLA_2Q = 480.0
CUSTOS_FIXOS_ORLA = 6_970.0
META_RETORNO = 0.08


def retorno_mecanico(preco_compra: float, diaria: float, ocupacao: float, custos_fixos: float) -> float:
    receita_bruta = diaria * 365 * ocupacao
    return (receita_bruta - custos_fixos) / preco_compra


def ocupacao_para_meta(preco_compra: float, diaria: float, custos_fixos: float, meta: float) -> float:
    return (meta * preco_compra + custos_fixos) / (diaria * 365)


def main() -> None:
    hurdle_calculado = ocupacao_para_meta(
        preco_compra=ORLA_2Q.preco_compra,
        diaria=DIARIA_ORLA_2Q,
        custos_fixos=CUSTOS_FIXOS_ORLA,
        meta=META_RETORNO,
    )

    print("DECISÃO FINAL — GATE AUDITÁVEL")
    print("=" * 38)
    print(f"Baseline de menor risco: {INTERIOR_2Q.nome}")
    print(f"Recomendação estratégica: {ORLA_2Q.nome}")
    print()
    print("Break-even publicado por retorno-alvo:")
    print(f"  6%  -> Interior {INTERIOR_2Q.ocupacao_6:.0%} | Orla {ORLA_2Q.ocupacao_6:.0%}")
    print(f"  8%  -> Interior {INTERIOR_2Q.ocupacao_8:.0%} | Orla {ORLA_2Q.ocupacao_8:.0%}")
    print(f" 10%  -> Interior {INTERIOR_2Q.ocupacao_10:.0%} | Orla {ORLA_2Q.ocupacao_10:.0%}")
    print()
    print(f"Hurdle calculado para 2Q Orla atingir 8%: {hurdle_calculado:.2%}")
    print(f"Hurdle arredondado comunicado: {ORLA_2Q.ocupacao_8:.0%}")
    print(f"Vantagem de risco do Interior no alvo de 8%: {(ORLA_2Q.ocupacao_8 - INTERIOR_2Q.ocupacao_8):.0%} p.p.")
    print()
    print("Regra de reversão:")
    print(
        "  Se dados reais indicarem que 2Q Orla não sustenta aproximadamente "
        f"{ORLA_2Q.ocupacao_8:.0%} de ocupação nas premissas comparáveis, "
        "a recomendação reverte para 2Q Interior."
    )
    print()
    print("Observação: passar o hurdle de 54% não prova que Orla supera Interior")
    print("na mesma ocupação; apenas mostra que a alternativa estratégica atende")
    print("à meta de retorno escolhida apesar do maior risco de capital.")


if __name__ == "__main__":
    main()
