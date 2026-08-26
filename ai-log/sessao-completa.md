# Sessão com IA — Exportação completa

> Hackathon Jovens Talentos AI Builder 2026 · Seazone
> Tema: Recomendação de investimento imobiliário — Itapema/SC
> Ferramenta: Claude Code / OpenCode · Data: 26/08/2026
>
> Este arquivo é a exportação **integral** da conversa de trabalho, em texto, conforme exigência do
> desafio (a seção completa de método está em `ai-log/README.md`).

---

## 1. Inventário dos arquivos disponíveis

**Pergunta:** "Quais arquivos estão disponíveis e qual é a função de cada um?"

**Resposta:** No workspace há três blocos:

- **Contexto (`contexto/`):**
  - `seazone_dados.md` — dados factuais da Seazone (identificação, áreas, franquias, tecnologia, indicadores, SPOTs).
  - `seazone_ai_builder_projetos_fontes.md` — estrutura da área de AI Builder, cultura AI First e projetos públicos de IA.
  - `Leticia-Gentil.md` — perfil profissional da autora (método, princípios, limites).

- **Dados (`data/`)** — mercado de Itapema/SC:
  - `Details_Itapema.csv` — anúncios Airbnb (descrição, comodidades, quartos, avaliações, ratings).
  - `Hosts_ids_Itapema.csv` — dados dos anfitriões (superhost, nº avaliações, tempo como host).
  - `Mesh_Ids_Data_Itapema.csv` — localização (lat/long, bairro) por anúncio.
  - `Price_AV_Itapema.csv` — série de preço diário por anúncio.
  - `VivaReal_Itapema.csv` — anúncios de venda (preço, área, condomínio).

- **Suporte (raiz):** `AGENTS.md` (regras/protocolos), `README.md` (apresentação do hackathon), `opencode.json`.

---

## 2. Granularidade de cada dataset

**Pergunta:** "Qual é a granularidade de cada dataset?"

**Resposta:**
| Dataset | Granularidade | Linhas |
|---|---|---|
| Details | 1 linha por anúncio Airbnb | 4.441 |
| Mesh | 1 linha por anúncio (com localização) | 4.441 |
| Hosts | 1 linha por host (owner repete por snapshot) | 4.440 / 3.057 owners |
| Price_AV | 1 linha por anúncio × data (painel diário) | 118.839 |
| VivaReal | 1 linha por anúncio imobiliário | 8.329 |

Price_AV cobre 2025-01-06 → 2025-04-20, e só ~1.005 dos 4.441 anúncios têm preço.

---

## 3. Colunas, significado e identificadores

**Pergunta:** "Quais são as colunas de cada arquivo, o que significam e quais campos são identificadores?"

**Resposta:** principais identificadores:
- `airbnb_listing_id` (Details, Mesh, Price_AV) — conecta Details↔Mesh (1:1, 100%) e Price_AV (~999).
- `owner_id` (Details ↔ Hosts) — 100% dos owners de Details presentes em Hosts.
- VivaReal usa `listing_id` próprio, sem chave comum — conexão por **bairro**.

---

## 4. Período coberto por dataset

- Cartões **Details e Hosts**: snapshot único em 13/01/2025.
- **Mesh**: `aquisition_date` espalhado de 2021 a 2026 (listings coletados ao longo do tempo).
- **Price_AV**: janela de preço 06/01 → 20/04/2025; coleta até 20/01/2025.
- **VivaReal**: snapshot de 11/01/2025.

---

## 5. Quantidade de imóveis/anúncios únicos

**Resposta:** Airbnb = 4.441 listings únicos; Price tem 1.005; Hosts 3.057 owners; VivaReal 8.293 imóveis únicos.

---

## 6. Cobertura de campos

**Pergunta:** "Qual percentual dos imóveis possui preço, disponibilidade, localização, quartos, banheiros, hóspedes?"

**Resposta (Airbnb, n=4.441):**
| Campo | Cobertura |
|---|---|
| Preço (`Price_AV`) | 22,5% |
| Disponibilidade | **inexistente** |
| Localização (via Mesh) | 100% |
| Quartos | 98,7% |
| Banheiros | 98,5% |
| Capacidade hóspedes | 100% |

**VivaReal (n=8.329):** preço de venda ~100%, condomínio 70%, IPTU 67%.

---

## 7. Valores anômalos

**Pergunta:** "Existem valores claramente anômalos?"

**Resposta:** sim, candidatos a revisão:
- Diária: pico R$ 29.000, 92 registros a R$ 10.000.
- Venda VivaReal: mínimo R$ 10.000 (implausível).
- Contagens = 0 (quartos/banheiros/camas) podem ser ausência de dado.
- Banheiros=19, camas=50 (chácaras/pousadas) — plausível, mas revisar.
- `number_of_guests` parece tetado em 16.

---

## 7. Contradições título x coordenadas x bairro

**Título vs bairro:** ~124 anúncios citam no título um bairro diferente do `suburb` registrado (muitos marcando "Meia Praia" de bairros vizinhos — nome da praia usado como marketing). Coordenadas do Mesh são internamente válidas dentro de Itapema.

---

## 8. Segmentos com amostra pequena

- **hotel**: n=1 com preço → sem validade.
- Bairros <30 com data: Alto São Bento, Sertão do Trombudo, Leopoldo Zarling, Jardim Praiamar, Areal, Lameiro.
- 42 listings com <20 dias de série.

---

## 9. Métricas diretamente observáveis

**Diretas:** diária (Price_AV), preço de venda, quartos, banheiros, hóspedes, superhost, genre, nº reviews, ratings, bairro/coords.
**Não observáveis (impossíveis):** ocupação, disponibilidade, receita total, RevPAR — ausência de calendário de reservas.

---

## 10. Ocupação estimável?

**Não.** Não há calendário de reservas em nenhum dataset. `Price_AV` só tem preço. `min_nights`=0; `can_instant_book` é reserva instantânea, não disponibilidade. Proxies de atividade são fracos e marcados como hipótese.

---

## 11. Período sem extrapolação enganosa

Janela recomendada: **06/01 → 20/04/2025** (alta temporada), só. Proibida projeção anual (falta inverno) e generalização para os 77% sem preço. Série mínima ≥40 dias e ≥2 meses.

---

## 12. Distribuição da oferta Airbnb

- **Bairro:** Meia Praia 64%, Centro 15%, Morretes 10% (89% nos 3).
- **Tipo:** apartamento 84%, casa 10%.
- **Quartos:** 3q 43%, 2q 33%.
- **Capacidade:** 6 (28%) / 8 (22%).

Maior segmento composto: apartamento 3q em Meia Praia.

---

## 13. Perfil de maior oferta / poucos concorrentes

**Maior oferta:** Meia Praia; apartamento 3q; capacidade 6–8.
**Poucos concorrentes:** células bairro×tipo com ≤10 — Lameiro, Sertão do Trombudo, Leopoldo, Ilhota, Morretes×hotel etc. (24 de 45 células <15). Mas são também os de menor demanda/amostra.

---

## 14. Distribuição de preços por tipologia

**Mediana diária:** apartamento R$ 585; casa R$ 500 (cauda alta); outros R$ 150; hotel n=1.
**Por bairro:** Tabuleiro R$ 610, Meia Praia R$ 595, Centro R$ 580.

---

## 15. Diária alta × Ocupação alta

**Impossível:** não há ocupação. Só diária alta é calculável por tipologia/bairro. Registrado como patrimônio não-respondível.

---

## 16. Diária alta × baixa ocupação / diária menor × ocupação suficiente

**Respostas iguais:** impossível — falta disponibilidade/ocupação para o componente "ocupação"/"receita". O trio de perguntas (diária×ocupação) em todas as combinações é marcado como **impossível** com os datasets.

---

## 17. Receita e diária média por nº de quartos

**Diária média (mediana):** 0q R$ 380 · 1q R$ 384 · 2q R$ 472 · 3q R$ 680 · 4q R$ 1.000. Cresce com os quartos.
**Receita:** impossível (depende de ocupação).

---

## 18. Aumento da diária entre faixas

0→1: +R$ 4 (+1%) · 1→2: +R$ 88 (+23%) · 2→3: +R$ 208 (+44%) · 3→4: +R$ 320 (+47%).

---

## 19. Aumento do preço de aquisição (VivaReal) nos mesmos saltos

0→1: −R$ 90k (−11%) · 1→2: +R$ 35k (+5%) · 2→3: +R$ 997k (+125%) · 3→4: +R$ 1.718k (+96%).
A aquisição dispara a partir de 3 quartos (diferente da diária, suave).

---

## 20. Perfil mais eficiente para investimento

**Múltiplo de eficiência (diária ÷ aquisição):**
- 2q: 0,059%/dia (melhor) · 1q: 0,051 · 3q: 0,038 · 4q: 0,030.
- 2 quartos = maior fração do preço "paga" pela diária.

---

## 21. Robustez: conclusão se mantém ao excluir amostras pequenas?

**Sim — e melhora.** Após filtro (n≥30 na diária validada ≥40 dias + aquisição ≥30):
- 2q: 0,061%/dia · 1q: 0,053 · 3q: 0,038 · 4q: 0,030.
- Studio (0q) e 5q+ descartados por ausência de série.

---

## 22. Investigação de localização (orla vs interior)

**Respostas:** orla (Meia Praia + Centro + Canto) = 3.545 anúncios (80%), diária R$ 594, aquisição R$ 2,4M; interior = 896, diária R$ 477, aquisição R$ 900k.
- Orla: diária maior + oferta maior + maior proxy de atividade.
- Interior: eficiência de capital ~2× maior (0,053 vs 0,025 %/dia).

"Orla + ocupação + receita alta simultâneos" = **impossível** (sem ocupação).

---

## 23. O que explica a receita (variáveis de qualidade)

**Diária (proxy de receita por noite):**
- Superhost: sem prêmio (média até menor).
- Guest guest favorite: sem prêmio.
- Nº de reviews: relação **inversa** à diária.
- Star rating: efeito nulo (quase todos 5.0).
- **Localização (orla) + nº de quartos** = principais explicadores.

---

## 24. Conexão Airbnb × mercado de vendas (dois cenários)

**Junção por bairro** (99% dos listings Airbnb têm bairro no VivaReal). Cenários propostos:
- **A — Investidor/operador**: eficiência de capital (diária ÷ venda) com custo (condomínio+IPTU).
- **B — Mercado**: estrutura de oferta e oportunidade vs saturação.

---

## 25. O que falta para responder "melhor perfil"

**Falta:** (1) ocupação/calendário de reservas (bloqueador, para ROI real); (2) custo operacional por noite.
**Hipóteses não validadas:** profissional+instant book geram mais ocupação; guest favorite gera mais receita.

**Tipo de anúncio (medido):** prof profissional 0,058%/dia vs não-prof 0,043%; instant book 0,050 vs 0,044; guest favorite sem prêmio.

---

## 26. Como tratar a ocupação (decisão) — break-even

Decidimos usar o **break-even**: ocupação mínima necessária para atingir meta de retorno, usando venda+condomínio+IPTU.

**Resultado (meta 8% a.a.):**
- 2q Interior: 44% · 1q Interior: 48% · 1q Orla: 51% · 2q Orla: 54% · 3q: 60–63% · 4q Orla: 80%.
→ 2q interior exige menor ocupação (menor risco). 4q orla o menos alcançável.

---

## 27. Briefing oficial do hackathon

Fonte consultada: `seazone-tech.github.io/jovens-talentos-2026-hackathon-data/`. Trata-se de:
- **Missão:** recomendar investimento imobiliário para a Seazone em Itapema/SC, respondendo 4 perguntas.
- **Entregáveis:** repositório (`jt2026-primeiro-ultimo-nome`) + vídeo de até 3 min no Drive + base `ai-log/`.
- **Avaliação:** raciocínio 45%, processo com IA 30%, comunicação 25%.
- **Tese a pontenciar:** "apart crash compactos (studio/1q) no Centro" é a aposta mais eficiente — precisa tomar posição.

---

## 28. Posição sobre a tese dos compactos no Centro

**Evidência (Centro):** Apto 1q = 0,051%/dia (R$ 450, venda R$ 890k); Apto 2q = 0,052%; Apto 3q = 0,038%.
**Studio (0q) no Centro: sem dados de preço (n=0).** 1q Meia Praia (0,055%) > 1q Centro.

**Veredito:** a tese é **parcialmente sustentada, mas não é a mais eficiente da cidade.** Recomendo **1–2 quartos** (não estúdio), **sem exclusividade do Centro**.

---

## 29. Entrega em HTML + README

Construídos:
- **`relatorio.html`** — relatório navegável que responde as 4 perguntas + posição da tese, tabelas, gr falço SVG e break-even a 6%/8%/10%.
- **`README.md`** — entregável central (link do vídeo na 1ª linha), como rodar, resumo.
- **`ai-log/`** — este log + `README.md` do método.

---

## 30. Recomendação final consolidada

**Compraria:** apartamento de **2 quartos**, na **orla (Meia Praia)** e **anúncio profissional com reserva instantânea**, para aluguel de curta estadia.

- **Estimativa (cenário):** 2q orla a 50% de ocupação (182 noites × R$ 596) ≈ R$ 108,5 mil bruto → ~9,2% a.a.
- **Qualidades que explicam melhor diária:** orla e nº de quartos; superhost/guest favorite sem prêmio.
- **Risco:** menor exigência de ocupação = 2q interior (44% p/ 8%).

**Tese:** parcialmente sustentada; studio sem evidência; melhor validada para 1–2 quartos, sem prioridade ao Centro.

---

_— fim da sessão —_