# ai-log — Registro do processo com IA

Esta pasta documenta **como o trabalho foi construído com IA**, que é parte da avaliação do hackathon
(30% da nota: iteração, persistência diante de obstáculo e senso crítico sobre o que a IA devolveu).

> Instrução: exporte a sessão inteira em texto (`.md`, `.txt` ou `.json`) do seu assistente
> (Claude Code / OpenCode). Este arquivo descreve o método; a conversa completa deve ficar aqui em texto.

## Método de trabalho

A investigação seguiu uma sequência lógica orientada por IA, com revisão crítica das respostas:

1. **Mapeamento da base** — colunas, granularidade, identificadores e relações entre os 5 datasets.
2. **Qualidade de dados** — cobertura por campo (ex.: preço só ~22% dos listings), anomalias de preço
   e contagens, e segmentos com amostra pequena.
3. **Definição de regras** — janela de análise 06/01 a 20/04/2025 (alta temporada), série mínima
   (≥40 dias / ≥2 meses), mediana do listing e recorte por n≥30, sem projeção anual.
4. **Análise de nicho/mercado** — oferta por bairro, tipo, quartos, capacidade e distribuição de preços.
5. **Localização** — divisão orla × interior e melhor localização.
6. **O que explica a diária** — cruzamentos de superhost, guest favorite, nº de avaliações, rating e
   regressão descritiva.
7. **Conexão Airbnb × venda** — junção por bairro e proxy de eficiência de capital (diária ÷ aquisição).
8. **Síntese + posicionamento** — resposta às 4 perguntas do desafio + posição sobre a tese dos compactos no Centro.

## Decisões críticas tomadas ao longo do caminho (com senso crítico sobre a IA)

- **Limitação estrutural identificada**: ocupação e receita total **não são mensuráveis** nos dados
  (não há calendário de reservas). A IA tentou sugerir proxies de "atividade"; **descartamos tratar isso
  como ocupação real** — documentamos como hipótese fraca, nunca facto.
- **Critério definido**: perante a impossibilidade de ROI real, adotei **eficiência de capital**
  (diária ÷ preço de aquisição) e **break-even** (ocupação mínima para meta). Justificativa transparente.
- **Amostras pequenas**: hotéis (n=1), bairros periféricos e ≥5 quartos foram **excluídos ou rotulados**,
  evitando recomendações sem embasamento.
- **Posição sobre a tese**: a IA ajudou a testar a tese dos compactos; **manti o veredito crítico** de que
  ela é parcialmente sustentada, mas não a mais eficiente — e especial "studio" não tem evidência (n=0).

## O que eu faria com mais uma semana
1. Obter **dado de ocupação/calendário de reservas** (API/integração da Seazone) e converter os cenários
   de **break-even** em **ROI real** por perfil.
2. Cruzar com **custo operacional** (taxa de gestão, limpeza, manutenção) para chegar a **lucro líquido**.
3. Refinar a definição de **orla por distância à praia** (coordenadas do `Mesh`) e validar a regressão com
   termo de interação louca quartos × localização.