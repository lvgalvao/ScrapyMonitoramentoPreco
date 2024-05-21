import pandas as pd
import sqlite3
from datetime import datetime

# Defina a variável origem
origem = "quotes_scrapy"

# Carregar o CSV em um DataFrame pandas
df = pd.read_csv('quotes.csv')

# Adicionar a coluna _origem
df['_origem'] = origem

# Adicionar a coluna _data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('quotes', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()
