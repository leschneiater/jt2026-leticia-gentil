# Decisão Final Auditada

Este arquivo congela a lógica da recomendação final e explicita como resolver o principal conflito encontrado na análise: **2 quartos no Interior apresenta menor risco de retorno, enquanto 2 quartos na Orla é a escolha estratégica**.

O objetivo aqui não é adicionar uma nova narrativa ao projeto, mas tornar a decisão **auditável, falsificável e consistente com os próprios números**.

---

## 1. Regra de decisão

A análise usa quatro dimensões, e não uma hierarquia rígida:

1. **Robustez** — eliminar ou rebaixar segmentos com evidência insuficiente.
2. **Eficiência de capital e risco** — estabelecer o baseline econômico usando preço de aquisição e break-even.
3. **Potencial operacional** — avaliar diária observada, escala de oferta e disponibilidade de evidência de preços.
4. **Decisão humana condicionada** — uma alternativa de maior risco só pode ser escolhida se o trade-off estiver explícito e houver um critério objetivo que possa invalidá-la.

Essa regra evita combinar automaticamente dois vencedores independentes — por exemplo, “2 quartos é o melhor perfil” + “Orla tem maior diária” — sem testar o conflito entre as alternativas finais.

---

## 2. Confronto direto: 2Q Interior × 2Q Orla

| Métrica | 2Q Interior | 2Q Orla | Diferença da Orla |
|---|---:|---:|---:|
| Preço mediano de aquisição | **R$ 750 mil** | **R$ 1,10 milhão** | +R$ 350 mil (~46,7%) |
| Ocupação para retorno de 6% | **33%** | **42%** | +9 p.p. |
| Ocupação para retorno de 8% | **44%** | **54%** | +10 p.p. |
| Ocupação para retorno de 10% | **54%** | **67%** | +13 p.p. |

### O que essa tabela prova

- **Interior domina em risco de capital** no cenário mecânico: exige menos capital e menor ocupação para os mesmos retornos-alvo.
- A recomendação da Orla **não pode ser defendida como a opção de menor risco**.
- Escolher Orla significa aceitar conscientemente um hurdle operacional maior.

### O que essa tabela não prova

Ela não demonstra que o Interior realiza maior receita, porque a base não contém ocupação observada, noites vendidas, receita total ou RevPAR.

Também não demonstra que a Orla supera o Interior em retorno quando ambos operam na mesma ocupação. A decisão pela Orla é uma **preferência estratégica condicionada**, não o resultado de uma dominância econômica direta.

---

## 3. Evidência operacional que favorece a Orla

A evidência regional disponível mostra:

| Evidência regional | Orla | Interior |
|---|---:|---:|
| Diária mediana observada | ~R$ 594 | ~R$ 477 |
| Anúncios observados | 3.545 (~80%) | 896 (~20%) |
| Presença em `Price_AV` | ~24% | ~17% |

Esses indicadores sustentam apenas que a Orla apresenta **maior diária observada, maior escala observada de oferta e maior disponibilidade de evidência de preços**.

Eles **não são evidência direta de demanda, ocupação ou receita realizada**.

---

## 4. Condição objetiva de reversão

Para o cenário de 2Q Orla usado no relatório:

- aquisição mediana: ~R$ 1,10 milhão;
- diária de referência: ~R$ 480;
- condomínio + IPTU: ~R$ 6.970/ano;
- meta de retorno usada como hurdle: **8%**.

Nesse cenário, o 2Q Orla precisa de aproximadamente **54% de ocupação** para atingir 8%.

### Gate de decisão

> **Se dados reais mostrarem que o 2Q Orla não consegue sustentar aproximadamente 54% de ocupação nas premissas comparáveis, a recomendação muda para 2Q Interior.**

O 2Q Interior exige aproximadamente **44%** para o mesmo retorno-alvo, uma vantagem de cerca de **10 pontos percentuais** no hurdle operacional.

Se a Orla atingir ou superar 54%, ela **passa o hurdle mínimo escolhido para a estratégia**, mas isso ainda não significa que supera o Interior em retorno na mesma ocupação. Significa apenas que o risco adicional aceito na escolha estratégica deixou de violar a meta de retorno definida.

---

## 5. Decisões congeladas

| Pergunta | Critério | Resultado | Evidência contrária | Decisão final |
|---|---|---|---|---|
| Melhor perfil | eficiência + robustez | **Apartamento 2Q** | 1Q tem eficiência próxima | manter 2Q pela combinação de eficiência e amostra |
| Melhor localização | potencial de monetização observável | **Orla** | receita real não é observável | chamar de potencial por diária, não receita comprovada |
| Menor risco | break-even | **2Q Interior** | menor escala regional observada | Interior é o baseline de risco |
| Compra estratégica | potencial operacional sujeito a hurdle | **2Q Orla** | Interior exige ~10 p.p. menos ocupação para 8% | Orla apenas condicional à validação do hurdle de ~54% |
| Tese compactos Centro | eficiência por perfil | **não sustentada como tese exclusiva** | 1Q Centro é competitivo | reformular para 1–2Q + análise por risco/potencial |

---

## 6. Evidências que contradizem a recomendação e precisam permanecer visíveis

1. **2Q Interior tem menor break-even** em todos os retornos-alvo comparados.
2. **Orla custa mais para adquirir** no recorte usado na decisão.
3. A base **não possui ocupação real**.
4. A base **não possui receita total, RevPAR ou ROI observado**.
5. Maior oferta e maior presença em `Price_AV` **não comprovam demanda**.
6. O componente **studio no Centro não pode ser validado** por ausência de série de preço suficiente.

Uma recomendação só permanece válida enquanto essas contradições forem tratadas como limites da decisão, e não apagadas da síntese.

---

## 7. Veredito final

**Baseline de menor risco:** apartamento de 2 quartos no Interior.

**Recomendação estratégica:** apartamento de 2 quartos na Orla, com Meia Praia como primeira região de busca, **condicionada à validação de ocupação suficiente para ultrapassar o hurdle de aproximadamente 54% no cenário de 8%**.

A decisão final, portanto, não é “Orla é objetivamente melhor”. É:

> **A Seazone pode aceitar o risco adicional da Orla pela maior diária e escala observadas, desde que a operação valide o patamar mínimo necessário. Se essa condição falhar, a decisão reverte para 2Q Interior.**
