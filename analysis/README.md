# Como reproduzir a análise

Esta pasta transforma os cálculos registrados na sessão com IA em artefatos executáveis.

O objetivo não é criar uma nova metodologia nem adicionar complexidade ao projeto. É permitir que os principais resultados publicados sejam recalculados diretamente a partir dos cinco CSVs originais.

## Requisitos

- Python 3.10+

Instale as dependências:

```bash
pip install -r analysis/requirements.txt
```

## Executar toda a análise

Na raiz do repositório:

```bash
python analysis/run_all.py
```

O pipeline executa:

1. `01_perfil.py` — perfil por número de quartos e eficiência de capital;
2. `02_localizacao.py` — Orla × Interior;
3. `03_regressao.py` — regressão descritiva com `log(diária)`;
4. `04_break_even.py` — ocupação necessária para metas de 6%, 8% e 10%;
5. `05_tese_centro.py` — teste da tese de compactos no Centro.

Os resultados são gravados em:

```text
analysis/outputs/
├── perfil.csv
├── localizacao.csv
├── regressao.csv
├── break_even.csv
└── tese_centro.csv
```

## Validar contra os resultados publicados

Depois de executar o pipeline:

```bash
python analysis/validate_results.py
```

A validação compara resultados recalculados com os valores e relações publicados no README e no relatório.

Ela foi deliberadamente construída para **sinalizar divergências**, e não para mascará-las. Se um resultado não estiver dentro do esperado, a orientação é investigar a diferença entre metodologia, filtro ou transformação — nunca alterar o código apenas para fazê-lo coincidir com a conclusão publicada.

## Regras preservadas da análise original

- mediana por listing para não dar peso excessivo a anúncios com mais registros em `Price_AV`;
- série validada: pelo menos 40 observações e presença em pelo menos 2 meses;
- prioridade para segmentos com n ≥ 30;
- preço de venda mínimo de R$ 50 mil como filtro de plausibilidade;
- `Orla = Meia Praia + Centro + Canto da Praia`;
- VivaReal não possui chave comum com Airbnb; o cruzamento é analítico por perfil/bairro;
- ocupação real, noites vendidas, receita total, RevPAR e ROI real permanecem **não observáveis** na base.

## Camada final de decisão

`decision_gate.py` não substitui os scripts acima. Ele é a camada posterior que transforma os resultados em uma regra de decisão auditável entre 2Q Interior e 2Q Orla.

A cadeia completa passa a ser:

```text
CSVs originais
    ↓
01–05 scripts analíticos
    ↓
outputs CSV
    ↓
validate_results.py
    ↓
decision_gate.py / DECISAO_FINAL.md
    ↓
README + relatório
```
