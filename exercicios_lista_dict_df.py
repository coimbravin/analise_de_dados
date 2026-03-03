"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)
# b) Mostre as 5 primeiras linhas
df_vendas.head()
# c) Mostre o formato (linhas, colunas)
df_vendas.shape
# d) Mostre os tipos de dados das colunas
df_vendas.dtypes
# RESOLUCAO: complete aqui



# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas.loc[:, ["mes" , "vendas"]]
# b) Mostre somente a primeira linha
df_vendas.head(1)
df_vendas.loc[0:0,]
# c) Mostre as linhas de indice 2 ate 4
df_vendas.loc[2:4,]

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
filter = df_vendas["vendas"] > 12000
# b) Filtre apenas a filial "Centro"
filter = df_vendas ["filial"] == "Centro"
df_vendas.loc[filter]
# c) Filtre vendas acima de 11000 na filial "Norte"
filter = (df_vendas["vendas"] >= 11000) & (df_vendas["filial"] == "Norte")
df_vendas.loc[filter]

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]
# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas.loc[:, ["filial","mes","ticket_medio","meta_batida"]]

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
df_vendas.loc[:, ["vendas"]].sum()
df_vendas.groupby("filial")["vendas"].sum()
# b) Calcule media de clientes por mes
df_vendas.groupby("mes")["clientes"].mean()
# c) Descubra a filial com maior total de vendas
maximo = df_vendas["vendas"].max()
filter = df_vendas["vendas"] == maximo
df_vendas.loc[filter]

#Groupby
df_vendas.groupby("filial")["vendas"].max()

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
# b) Pegue os 3 maiores resultados de vendas
# c) Mostre um ranking com "filial", "mes", "vendas"

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
# 2) Ordene o resumo por total_vendas (desc)
# 3) Exiba qual filial teve melhor desempenho geral

# RESOLUCAO: complete aqui






# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
type(dados_list_dict)
# 2. Qual é o tipo do primeiro elemento?
dic= dados_list_dict[0]
type(dic)
# 3. Como acessar a lista da "Column A"?
dic["Column A"]
# 4. Como acessar o segundo elemento da "Column C"?
dic["Column C"]

# RESPONDA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
df1 = pd.DataFrame(dados_list_dict[0])
# 2. Mostre:
#    - shape
#    - tipos das colunas
# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna

# RESOLVA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
# 2. Crie coluna "Media" = média por linha
# 3. Filtre linhas onde Total > 10

# RESOLVA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.
df_vendas.to_dict()
df_vendas.to_dict(orient="records")

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.

df_vendas.to_dict(orient="list")
# RESOLVA AQUI:


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
list = df1["Column A"].to_list()
# 2. Multiplique cada elemento da lista por 10.
# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.

# RESOLVA AQUI:



# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
df = pd.DataFrame
# 2. Quantos registros existem?
# 3. Quais são as chaves do primeiro dicionário?
# 4. Liste todos os países existentes (sem repetição).

# RESOLVA AQUI:



# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
# 2. Mostre shape, tipos e primeiras linhas
# 3. Converta a coluna periodo para datetime

# RESOLVA AQUI:



# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
# 2. Filtre apenas Produto A
# 3. Filtre valor > 4000
# 4. Combine Brasil + Produto A

# RESOLVA AQUI:


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
# 2. Ordene por valor decrescente
# 3. Ordene por periodo e depois por valor

# RESOLVA AQUI:



# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
# 2. Total exportado por produto
# 3. Média por país
# 4. Quantidade de operações por país

# RESOLVA AQUI:


# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem

# Explique em comentário o que essa tabela representa

# RESOLVA AQUI:



# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor

# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

# RESOLVA AQUI:


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela

# RESOLVA AQUI:



# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

# RESOLVA AQUI:



# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

# RESOLVA AQUI:








