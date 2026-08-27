**Vídeo (até 3 min):** [VIDEO](https://drive.google.com/file/d/1y-VsZxMTcC0KePQLwtJGNfH6GmYKjID3/view?usp=sharing)

---

# Hackathon Jovens Talentos AI Builder 2026 · Seazone

**Autora:** Leticia Schneiater Gentil  
**Desafio:** recomendação de investimento imobiliário para a Seazone em **Itapema/SC**, construída com IA a partir de dados reais de Airbnb e VivaReal.

**Entregável central:** [RELATÓRIO NAVEGÁVEL](https://leschneiater.github.io/jt2026-leticia-gentil/)

O relatório responde às quatro perguntas do desafio, apresenta uma posição sobre a tese dos compactos no Centro, explicita as limitações dos dados e documenta como a IA foi utilizada durante a investigação.

---

## Recomendação executiva

**Se a Seazone fosse comprar hoje, eu priorizaria um apartamento de 2 quartos na orla, com Meia Praia como primeira região de busca, operado profissionalmente para curta estadia e com reserva instantânea.**

Essa decisão não significa que a orla seja a alternativa de menor risco.

O **2 quartos no interior apresenta menor break-even** no cenário analisado. A escolha da orla é uma decisão estratégica: aceita uma ocupação necessária maior em troca de **diária observada superior, escala de oferta e maior profundidade do mercado de curta estadia**.

| Dimensão | Leitura da análise |
|---|---|
| **Tipologia** | Apartamento concentra os perfis mais eficientes analisados |
| **Nº de quartos** | **2 quartos** apresenta a melhor eficiência de capital entre segmentos robustos (~0,060%/dia) |
| **Tipo de anúncio** | Operação **profissional + reserva instantânea** aparece associada a métricas superiores; associação não implica causalidade |
| **Localização** | **Orla** apresenta diária mediana observada de ~R$ 594 vs ~R$ 477 no interior |
| **Menor risco de retorno** | **2q Interior** precisa de ~44% de ocupação para atingir 8% no cenário-base |
| **Escolha estratégica** | **2q Orla**, com Meia Praia como primeira região de busca |

---

## Como defini “melhor”

O desafio deixa os termos “melhor perfil” e “melhor localização” propositalmente abertos.

Por isso, a decisão foi analisada a partir de quatro dimensões:

1. **Eficiência de capital** — diária mediana observada ÷ preço mediano de aquisição.
2. **Risco** — ocupação mínima necessária para atingir uma meta de retorno em um cenário mecânico.
3. **Potencial operacional** — diária observada, escala de oferta e presença de dados de preço na região.
4. **Robustez** — prioridade para segmentos com amostra suficiente e separação entre evidência, hipótese e limitação.

Essas dimensões não apontam sempre para o mesmo imóvel.

O principal trade-off encontrado foi:

- **2q Interior** → menor preço de entrada e menor ocupação necessária para atingir o retorno-alvo;
- **2q Orla** → diária observada maior e mercado de curta estadia mais profundo.

A recomendação final privilegia a segunda alternativa para a estratégia da Seazone, mantendo o Interior como referência de menor risco de capital.

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

A resposta defensável com a base disponível é a **orla**, especialmente **Meia Praia e Centro**, pela combinação de **diária observada e escala de oferta**.

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

> “a orla comprovadamente gera mais receita”.

É:

> **a orla apresenta maior potencial de monetização por diária dentro das variáveis observáveis disponíveis.**

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
| Orla vs interior | +0,142 | +15,3% |
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

**Compraria um apartamento de 2 quartos na orla, com Meia Praia como primeira região de busca.**

A operação seria estruturada para curta estadia, como anúncio profissional e com reserva instantânea.

A escolha considera um trade-off explícito:

- **2q Interior** é a alternativa de menor risco no cenário de retorno;
- **2q Orla** é a escolha estratégica pela diária observada superior e pela escala do mercado de short stay.

### Estimativa simples de retorno — cenário, não previsão

Para manter coerência entre o imóvel recomendado e a diária utilizada no cálculo, o cenário considera:

- aquisição mediana: **~R$ 1,10 milhão**;
- diária de referência para 2q na orla: **~R$ 480**;
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

Se o 2q na orla operar estruturalmente abaixo do patamar necessário, o 2q no interior passa a ser a alternativa mais defensável pelo menor risco de capital.

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
- para a agregação regional deste relatório, **orla = Meia Praia + Centro + Canto da Praia**;
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

Durante o processo, a IA foi usada para:

1. mapear os cinco datasets, sua granularidade, colunas e chaves;
2. investigar cobertura, valores ausentes, amostras pequenas e inconsistências;
3. testar hipóteses sobre perfil, localização, tipo de anúncio e retorno;
4. refazer análises quando uma conclusão dependia de segmentos frágeis;
5. conectar o mercado de Airbnb com o mercado de venda;
6. construir métricas derivadas como eficiência de capital e break-even;
7. confrontar a tese interna dos compactos no Centro;
8. documentar limitações e separar dado observado de hipótese.

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

# Como abrir o relatório

O relatório é um único arquivo HTML autossuficiente, com CSS embutido e sem dependências externas.

```bash
# na raiz do repositório

open index.html      # macOS
xdg-open index.html  # Linux
start index.html     # Windows
