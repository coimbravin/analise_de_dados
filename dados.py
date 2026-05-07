import sqlite3
import pandas as pd
# Banco de Dados SQLite
nome_db = "cadastro_estudantes.db"
#conexoes com o banco de dados
conn = sqlite3.connect(nome_db)
# trazer para dentro do pandas
query = "select * from tb_alunos"
df_alunos = pd.read_sql (query, conn)
query = "select * from tb_enderecos"
df_enderecos = pd.read_sql(query,conn)
# merge entre tb_alunos e tb_endercos
df = pd.merge(df_alunos, df_enderecos, left_on="endereco_id", right_on="id", how="inner")
df[["nome_aluno", "email", "endereco"]]