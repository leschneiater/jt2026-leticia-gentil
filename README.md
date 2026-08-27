**Vídeo (até 3 min):** [VIDEO](https://drive.google.com/file/d/1y-VsZxMTcC0KePQLwtJGNfH6GmYKjID3/view?usp=sharing)

---

# Hackathon Jovens Talentos AI Builder 2026 · Seazone

**Autora:** Leticia Schneiater Gentil  
**Desafio:** recomendação de investimento imobiliário para a Seazone em **Itapema/SC**, construída com IA a partir de dados reais de Airbnb e VivaReal.

**Entregável central:** [RELATÓRIO NAVEGÁVEL](https://leschneiater.github.io/jt2026-leticia-gentil/)

**Decisão auditada:** [`DECISAO_FINAL.md`](./DECISAO_FINAL.md)  
**Análise reproduzível:** [`analysis/README.md`](./analysis/README.md)  
**Pipeline completo:** [`analysis/run_all.py`](./analysis/run_all.py)  
**Validação dos resultados:** [`analysis/validate_results.py`](./analysis/validate_results.py)  
**Gate reproduzível da decisão:** [`analysis/decision_gate.py`](./analysis/decision_gate.py)

O relatório responde às quatro perguntas do desafio, apresenta uma posição sobre a tese dos compactos no Centro, explicita as limitações dos dados e documenta como a IA foi utilizada durante a investigação.

---

## Recomendação executiva

**Se a Seazone fosse comprar hoje, eu priorizaria um apartamento de 2 quartos na orla, com Meia Praia como primeira região de busca, operado profissionalmente para curta estadia e com reserva instantânea.**

Essa decisão não significa que a orla seja a alternativa de menor risco.

O **2 quartos no Interior apresenta menor break-even** no cenário analisado. A escolha da Orla é uma decisão estratégica: aceita uma ocupação necessária maior em troca de **diária observada superior, maior escala observada de oferta e maior disponibilidade de evidência de preços**.

| Dimensão da decisão | Leitura da análise |
|---|---|
| **Tipologia** | Apartamento concentra os perfis mais eficientes analisados |
| **Nº de quartos** | **2 quartos** apresenta a melhor eficiência de capital entre segmentos robustos (~0,060%/dia) |
| **Tipo de anúncio** | Operação **profissional + reserva instantânea** aparece associada a métricas superiores; associação não implica causalidade |
| **Localização** | **Orla** apresenta diária mediana observada de ~R$ 594 vs ~R$ 477 no Interior |
| **Menor risco de retorno** | **2Q Interior** precisa de ~44% de ocupação para atingir 8% no cenário-base |
| **Escolha estratégica** | **2Q Orla**, com Meia Praia como primeira região de busca |
| **Condição de reversão** | se 2Q Orla não sustentar ~54% nas premissas comparáveis, a decisão reverte para 2Q Interior |

---

## Como defini “melhor”

O desafio deixa os termos “melhor perfil” e “melhor localização” propositalmente abertos.

Por isso, a decisão não usa uma hierarquia rígida. Ela segue uma **regra de decisão**:

1. **Robustez** — eliminar ou rebaixar segmentos com evidência insuficiente.
2. **Eficiência de capital e risco** — estabelecer o baseline econômico usando preço de aquisição e break-even.
3. **Potencial operacional** — avaliar diária observada, escala de oferta e disponibilidade de evidência de preços.
4. **Decisão humana condicionada** — uma alternativa de maior risco só pode ser escolhida se o trade-off estiver explícito e houver um critério objetivo que possa invalidá-la.

Essa regra evita combinar automaticamente dois vencedores independentes — por exemplo, “2 quartos é o melhor perfil” + “Orla tem maior diária” — sem testar diretamente o conflito entre as alternativas finais.

### Confronto direto: 2Q Interior × 2Q Orla

| Métrica | 2Q Interior | 2Q Orla | Diferença da Orla |
|---|---:|---:|---:|
| Preço mediano de aquisição | **R$ 750 mil** | **R$ 1,10 milhão** | +R$ 350 mil (~46,7%) |
| Ocupação para retorno de 6% | **33%** | **42%** | +9 p.p. |
| Ocupação para retorno de 8% | **44%** | **54%** | +10 p.p. |
| Ocupação para retorno de 10% | **54%** | **67%** | +13 p.p. |

A leitura correta é:

- **2Q Interior** é o baseline de menor risco de capital;
- **2Q Orla** é uma escolha estratégica condicionada;
- passar o hurdle de ~54% significa apenas que a Orla atende à meta mecânica de 8% usada no cenário — **não prova que ela supera o Interior na mesma ocupação**.

### Condição objetiva de reversão

> **Se dados reais mostrarem que o 2Q Orla não consegue sustentar aproximadamente 54% de ocupação nas premissas comparáveis, a recomendação muda para 2Q Interior.**

O detalhamento dessa lógica está congelado em [`DECISAO_FINAL.md`](./DECISAO_FINAL.md).

---

# Respostas às 4 perguntas do desafio

## 1. Qual o melhor perfil de imóvel para investir na cidade?

**Apartamento de 2 quartos.**

Entre os segmentos com amostra robusta, foi o perfil com melhor relação entre diária e preço de aquisição.

| Perfil | Diária mediana | n séries | Eficiência %/dia |
|---|---:|---:|---:|
| **Apartamento · 2q** | R$ 484 | 333 | **0,060** |
| Apartamento · 1q | R$ 400 | 106 | 0,057 |
| Apartamento · 3q | R$ 680 | 390 | 0,039 |
| Apartamento · 4q | R$ 1.050 | 68 | 0,029 |

O ponto central não é que imóveis maiores cobrem diárias menores — eles cobram mais.

O problema é que **o preço de aquisição cresce mais rápido que a diária**, reduzindo a eficiência do capital adicional.

Nos atributos operacionais, anúncios classificados como **profissionais** e com **reserva instantânea** aparecem associados a métricas superiores de diária/eficiência.

Essa relação é tratada como **associação observada**, não como causalidade comprovada.

---

## 2. Qual a melhor localização em termos de receita?

A resposta defensável com a base disponível é a **Orla**, especialmente **Meia Praia e Centro**, pela combinação de **diária observada e escala de oferta**.

- Orla: diária mediana de aproximadamente **R$ 594**;
- Interior: diária mediana de aproximadamente **R$ 477**;
- Meia Praia concentra cerca de **64% da oferta observada** e possui a maior amostra de anúncios com série de preço.

### Limitação importante

A base não contém calendário de reservas.

Portanto, não é possível medir diretamente:

- ocupação;
- noites vendidas;
- receita total;
- RevPAR por bairro.

A presença no `Price_AV` é tratada apenas como um **proxy de cobertura/atividade da base**, nunca como ocupação real.

Por isso, a conclusão correta não é:

> “a Orla comprovadamente gera mais receita”.

É:

> **a Orla apresenta maior potencial de monetização por diária dentro das variáveis observáveis disponíveis.**

Maior oferta e maior presença no `Price_AV` **não comprovam demanda nem receita realizada**.

---

## 3. Quais características explicam as melhores receitas?

Como a receita total não é observável, a análise utiliza a **diária mediana do anúncio** como variável mensurável.

Foi aplicada uma regressão descritiva com `log(diária)` como variável resposta.

**Amostra:** n ≈ 999  
**R²:** ≈ 0,41

| Variável | Coeficiente | Associação aproximada com a diária |
|---|---:|---:|
| Nº de quartos | +0,327 | +38,7% por quarto adicional |
| Operador profissional | +0,221 | +24,7% |
| Orla vs Interior | +0,142 | +15,3% |
| Superhost | +0,008 | ~+0,8% |
| Guest favorite | −0,040 | ~−3,9% |
| log(nº avaliações) | −0,105 | ~−10,0% por +1 unidade em log(reviews) |

O modelo é **descritivo e associativo**.

Ele não demonstra que alterar uma característica causará a variação indicada.

O principal aprendizado é que **número de quartos, localização e perfil profissional do anúncio** aparecem como os sinais positivos mais fortes.

Superhost e Guest Favorite não apresentam prêmio relevante de diária nesta especificação.

O comportamento negativo do número de avaliações também não é interpretado como causalidade: pode refletir diferenças de composição entre anúncios novos, maduros, premium ou de maior volume.

---

## 4. Se a Seazone fosse investir hoje, o que eu compraria e por quê?

**Compraria um apartamento de 2 quartos na Orla, com Meia Praia como primeira região de busca.**

A operação seria estruturada para curta estadia, como anúncio profissional e com reserva instantânea.

A escolha considera um trade-off explícito:

- **2Q Interior** é a alternativa de menor risco no cenário de retorno;
- **2Q Orla** é a escolha estratégica pela diária observada superior, pela escala observada de oferta e pela maior disponibilidade de evidência de preços.

### Estimativa simples de retorno — cenário, não previsão

Para manter coerência entre o imóvel recomendado e a diária utilizada no cálculo, o cenário considera:

- aquisição mediana: **~R$ 1,10 milhão**;
- diária de referência para 2Q na Orla: **~R$ 480**;
- condomínio + IPTU: **~R$ 6.970/ano**;
- custos operacionais, tributos e taxa de gestão: **não incluídos**.

| Ocupação hipotética | Receita bruta | Após condomínio + IPTU | Retorno mecânico |
|---|---:|---:|---:|
| 40% | ~R$ 70,1 mil | ~R$ 63,1 mil | ~5,7% |
| 50% | ~R$ 87,6 mil | ~R$ 80,6 mil | ~7,3% |
| **54%** | ~R$ 94,6 mil | ~R$ 87,6 mil | **~8,0%** |
| 60% | ~R$ 105,1 mil | ~R$ 98,2 mil | ~8,9% |

Este quadro é uma **análise de sensibilidade**, não uma previsão de ROI.

A base de preços cobre o período de **06/01 a 20/04/2025** e não permite inferir ADR anual nem ocupação real.

O dado que mais poderia mudar a decisão é justamente a **ocupação observada**.

**Gate final:** se a ocupação real do 2Q Orla ficar estruturalmente abaixo de ~54% nas premissas comparáveis, o 2Q Interior passa a ser a alternativa mais defensável pelo menor risco de capital.

---

# Posição sobre a tese dos compactos no Centro

A hipótese preliminar interna era que:

> **apartamentos compactos — studio ou 1 quarto — no Centro seriam a aposta mais eficiente para a Seazone.**

## Veredito: a tese precisa ser reformulada

**Não sustentaria “studio/1q no Centro” como a aposta mais eficiente da cidade.**

Os dados sustentam uma leitura mais ampla:

> **imóveis de 1–2 quartos são perfis eficientes em capital, sem exclusividade do Centro.**

| Perfil | Bairro | Diária | n | Venda mediana | Eficiência %/dia |
|---|---|---:|---:|---:|---:|
| Studio (0q) | Centro | sem série válida | 0 | — | n/a |
| 1q | Centro | R$ 450 | 78 | R$ 890k | 0,051 |
| **2q** | Centro | R$ 580 | 65 | R$ 1,12M | **0,052** |
| 3q | Centro | R$ 790 | 45 | R$ 2,10M | 0,038 |

O componente **studio** não pode ser validado com o recorte disponível.

O 1q no Centro é eficiente, mas o 2q no próprio Centro apresenta eficiência ligeiramente superior.

Por isso, a tese final passa de:

> **“studio/1q + Centro”**

para:

> **“1–2 quartos + análise por risco e potencial operacional”.**

---

# Metodologia e limitações

## Dados utilizados

- `data/Details_Itapema.csv` — características dos anúncios Airbnb;
- `data/Hosts_ids_Itapema.csv` — informações dos anfitriões;
- `data/Mesh_Ids_Data_Itapema.csv` — localização e bairro dos anúncios;
- `data/Price_AV_Itapema.csv` — séries de preço do Airbnb;
- `data/VivaReal_Itapema.csv` — mercado de aquisição.

## Regras principais

- janela observada de preço: **06/01 a 20/04/2025**;
- mediana por listing para reduzir o peso de anúncios com mais observações;
- segmentos pequenos tratados como indicativos;
- prioridade para recortes com **n ≥ 30**;
- preços de venda inferiores a R$ 50 mil removidos por plausibilidade;
- para a agregação regional deste relatório, **Orla = Meia Praia + Centro + Canto da Praia**;
- separação explícita entre dado observado, métrica derivada e informação não observável.

## O que é observado

Exemplos:

- diária;
- preço de venda;
- número de quartos;
- bairro;
- reviews;
- status de Superhost;
- perfil profissional do anúncio.

## O que é derivado

Exemplos:

- eficiência de capital;
- break-even;
- regressão descritiva;
- cenários mecânicos de retorno.

## O que não é observável na base

- ocupação real;
- receita total;
- RevPAR;
- ROI real.

Essa é a principal limitação da análise.

---

# Como trabalhei com IA

A IA foi utilizada como **ferramenta de investigação e execução**, não como fonte final de verdade.

O registro textual da sessão principal está em:

[`ai-log/transcricao-completa.md`](./ai-log/transcricao-completa.md)

O adendo posterior de auditoria da decisão está em:

[`ai-log/adendo-decisao-final.md`](./ai-log/adendo-decisao-final.md)

Durante o processo, a IA foi usada para:

1. mapear os cinco datasets, sua granularidade, colunas e chaves;
2. investigar cobertura, valores ausentes, amostras pequenas e inconsistências;
3. testar hipóteses sobre perfil, localização, tipo de anúncio e retorno;
4. refazer análises quando uma conclusão dependia de segmentos frágeis;
5. conectar o mercado de Airbnb com o mercado de venda;
6. construir métricas derivadas como eficiência de capital e break-even;
7. confrontar a tese interna dos compactos no Centro;
8. documentar limitações e separar dado observado de hipótese;
9. auditar a decisão final confrontando diretamente 2Q Interior × 2Q Orla e definindo uma condição objetiva de reversão.

Um ponto crítico do processo foi a decisão de **não tratar presença na série de preços como ocupação**.

A ausência de calendário de reservas impediu que receita e ROI fossem apresentados como fatos observados.

O processo completo também mostra erros, revisões e mudanças de direção da própria IA — parte importante da forma como a análise foi construída.

---

# O que eu faria com mais uma semana

1. Aprofundaria a análise de **ROI**, incorporando dados que hoje não estão disponíveis na base, principalmente ocupação real, receita realizada e custos operacionais, para transformar os cenários atuais em uma análise de retorno mais completa.

2. Transformaria esta análise em uma **ferramenta de apoio à decisão**, na qual fosse possível selecionar uma região e receber automaticamente uma avaliação do mercado de curta estadia e do mercado imobiliário local.

3. Integraria diferentes fontes de dados por **APIs**, conectando informações de plataformas como Airbnb, VivaReal e outras bases relevantes para ampliar a precisão da análise.

4. Usaria IA para processar essas fontes e gerar automaticamente indicadores de perfil de imóvel, localização, preço de aquisição, potencial de receita e cenários de retorno.

5. O objetivo seria criar uma operação reutilizável: mudar a região analisada e receber um novo relatório, permitindo levar essas informações rapidamente para **reuniões e tomadas de decisão de investimento**.

---

# Como reproduzir a análise

A análise foi organizada para que os principais resultados possam ser recalculados diretamente a partir dos cinco CSVs da pasta `data/`.

## 1. Instalar as dependências

Na raiz do repositório:

```bash
pip install -r analysis/requirements.txt
```

## 2. Executar o pipeline completo

```bash
python analysis/run_all.py
```

Esse comando executa, em sequência:

1. `01_perfil.py` — perfil por número de quartos e eficiência de capital;
2. `02_localizacao.py` — comparação Orla × Interior;
3. `03_regressao.py` — regressão descritiva com `log(diária)`;
4. `04_break_even.py` — ocupação necessária para metas de 6%, 8% e 10%;
5. `05_tese_centro.py` — teste da tese dos compactos no Centro.

Os resultados são gravados em `analysis/outputs/`:

```text
analysis/outputs/
├── perfil.csv
├── localizacao.csv
├── regressao.csv
├── break_even.csv
└── tese_centro.csv
```

## 3. Validar os resultados publicados

Depois de executar o pipeline:

```bash
python analysis/validate_results.py
```

A validação compara os resultados recalculados com os valores e relações publicados neste README e no relatório.

Ela foi construída para **sinalizar divergências, não mascará-las**. Se algum resultado não estiver dentro do esperado, a diferença deve ser investigada antes de qualquer alteração na conclusão.

## 4. Executar o gate final da decisão

```bash
python analysis/decision_gate.py
```

O `decision_gate.py` é a camada posterior de decisão entre **2Q Interior × 2Q Orla**. Ele não substitui a análise dos CSVs.

A cadeia completa é:

```text
CSVs originais
    ↓
scripts 01–05
    ↓
outputs CSV
    ↓
validate_results.py
    ↓
decision_gate.py + DECISAO_FINAL.md
    ↓
README + relatório
```

O detalhamento técnico da reprodução está em [`analysis/README.md`](./analysis/README.md).

---

# Como abrir o relatório

O relatório é um único arquivo HTML autossuficiente, com CSS embutido e sem dependências externas.

```bash
# na raiz do repositório
open index.html      # macOS
xdg-open index.html  # Linux
start index.html     # Windows
```
