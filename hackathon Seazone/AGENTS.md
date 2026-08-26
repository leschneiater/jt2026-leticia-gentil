## 1. Fontes de contexto e dados

Existem duas fontes principais de informação neste workspace:

### 1.1 Base de contexto

A base de conhecimento está na pasta:

`contexto/`

Os arquivos desta pasta contêm informações factuais, organizacionais e de negócio que devem ser utilizadas como referência para análises e decisões deste projeto.

Atualmente existem:

- `contexto/Leticia-Gentil.md`
- `contexto/seazone_ai_builder_projetos_fontes.md`
- `contexto/seazone_dados.md`

Antes de responder sobre Seazone, estrutura da empresa, áreas, projetos, problemas, oportunidades ou perfil profissional da participante, consulte os arquivos relevantes da pasta `contexto/`.

---

### 1.2 Base de dados

Os datasets disponíveis para análise estão na pasta:

`data/`

Atualmente existem:

- `data/Details_Itapema.csv`
- `data/Hosts_ids_Itapema.csv`
- `data/Mesh_Ids_Data_Itapema.csv`
- `data/Price_AV_Itapema.csv`
- `data/VivaReal_Itapema.csv`

Esses arquivos devem ser utilizados como fonte de evidência quantitativa sempre que uma análise envolver imóveis, anúncios, hosts, preços, localização, mercado de Itapema ou outras informações presentes nos datasets.

Antes de tirar conclusões a partir dos dados:

1. identificar quais arquivos são relevantes para a pergunta;
2. inspecionar colunas, tipos de dados e granularidade;
3. verificar valores ausentes, duplicidades e possíveis inconsistências;
4. identificar chaves que permitam relacionar os datasets;
5. diferenciar dado observado de interpretação;
6. registrar limitações relevantes da base;
7. não inferir o significado de campos ambíguos sem evidência;
8. não alterar os arquivos originais durante análises exploratórias.

Sempre que uma conclusão depender dos datasets, indicar quais arquivos e evidências sustentam a conclusão.

Quando necessário, cruzar informações entre `contexto/` e `data/`, mantendo a seguinte distinção:

- `contexto/` → informações de negócio, organização, projeto e conhecimento documentado;
- `data/` → evidências quantitativas e registros utilizados para análise.

Não invente informações quando elas não estiverem presentes nas fontes.

Quando houver conflito entre conhecimento geral, documentos do projeto e dados observados, sinalize o conflito.

Quando uma informação não puder ser confirmada, informe a incerteza.

Não trate hipótese como fato.
