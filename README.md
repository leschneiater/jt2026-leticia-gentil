**Vídeo (até 3 min):** [VIDEO](https://drive.google.com/file/d/1y-VsZxMTcC0KePQLwtJGNfH6GmYKjID3/view?usp=sharing)

---

# Hackathon Jovens Talentos AI Builder 2026 · Seazone

**Autora:** Leticia Schneiater Gentil (LETS) · **Cargo:** AI Builder

**Desafio:** recomendação de investimento imobiliário para a Seazone — **Itapema/SC** — construída com IA, a partir de dados reais de Airbnb e VivaReal.

**Entregável central:** [RELATÓRIO](https://leschneiater.github.io/jt2026-leticia-gentil/) — relatório navegável que responde as 4 perguntas do desafio + a posição sobre a tese dos compactos no Centro.

---

## Como rodar / abrir

O relatório é **um único arquivo HTML autossuficiente** (CSS embutido, sem dependências externas). Basta abrir:

```bash
# na raiz do repositório
open relatorio.html      # macOS
xdg-open relatorio.html  # Linux
start relatorio.html     # Windows
```

Também funciona impresso (há regras de `@media print`).

### Como os números foram gerados
As análises foram feitas com **scripts Python puros** (sem bibliotecas externas) sobre os datasets da pasta `data/`. A lógica (medianas por perfil, eficiência, break-even e regressão) está documentada no relatório e reproduzida nos arquivos de apoio.

---

## Resumo da recomendação final

**Compraria apartamentos de 2 quartos, na zona litorânea (Meia Praia preferida), operados como anúncio profissional com reserva instantânea, para aluguel de curta estadia.**

| Eixo | Recomendação | Evidência |
|---|---|---|
| Tipologia | **Apartamento** (> casa) | 84% da oferta; melhor eficiência de capital |
| Nº de quartos | **2** (alternativa: 1) | 0,060%/dia vs 0,039%/0,029% para 3q/4q |
| Tipo de anúncio | **Profissional + reserva instantânea** | +0,221 log; 0,058%/dia vs 0,043% |
| Localização | **Orla (Meia Praia/Centro)** | diária ~25% maior que interior |

**Estimativa simples de retorno (cenário), 2q na orla:** com ocupação de 50% (~182 noites × R$ 596), receita bruta ≈ **R$ 108,5 mil**; após condomínio+IPTU ≈ **R$ 101 mil** → retorno bruto ≈ **~9,2% a.a.** (antes de custos operacionais). Isso é **cenário de sensibilidade**, não ROI observado.

### Posição sobre a tese dos compactos no Centro

A análise interna sugeriu *"apartamentos compactos (studio/1 quarto) no Centro"* como aposta mais eficiente.

> **Veredito:** parcialmente sustentada, mas **não é a mais eficiente da cidade**. O studio (0q) no Centro **não tem série de preço** (n=0) → sem evidência. O 1q no Centro é eficiente (0,051%/dia), mas o 2q no Centro empata (0,052%) e os perfis 1–2q gerais/Meia Praia são superiores (0,057–0,060%). Recomendo **1–2 quartos**, não estúdio, e **sem exclusividade do Centro**.

---

## Respostas às 4 perguntas do desafio

### 1. Qual o melhor perfil de imóvel?
**Apartamento de 2 quartos**, perfil profissional e reserva instantânea. Critério: eficiência de capital (diária ÷ preço de aquisição). Robusto após filtro de amostra mínima (n≥30).

### 2. Qual a melhor localização em termos de receita?
**Orla (Meia Praia e Centro)**. Maior oferta, diária ~25% maior e proxy de atividade superior. *Receita real não é computável nos dados (ver limitações).*

### 3. Quais características explicam as melhores receitas?
**Localização (orla) e nº de quartos** dominam (R² ≈ 0,41). Superhost e guest favorite **não explicam** diária maior; nº de avaliações tem relação **inversa** com a diária.

### 4. O que compraria hoje + estimativa de retorno?
**2q na orla, anúncio profissional, curta estadia.** Estimativa de cenário ~9,2% a.a. a 50% de ocupação; break-even por perfil na tabela do relatório.

---

## Estrutura do repositório

| Caminho | Conteúdo |
|---|---|
| `README.md` | Este arquivo (link do vídeo na 1ª linha) |
| `index.html` | Relatório completo navegável (recomendação + análise) |
| `ai-log/` | Conversas com a IA em texto (processo de trabalho) |
| `contexto/` | Base de contexto da empresa e perfil profissional |
| `data/` | Datasets de apoio (Airbnb + VivaReal) |

---

## Fontes de contexto

- `contexto/seazone_ai_builder_projetos_fontes.md` — estrutura AI Builder e cultura AI First
- `contexto/seazone_dados.md` — dados factuais da Seazone
- `contexto/Leticia-Gentil.md` — perfil e método de trabalho da autora
