import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('quotes.db')

# Carregar os dados da tabela 'quotes' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM quotes", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title('Quotes Dashboard')

# Mostrar o DataFrame
st.subheader('DataFrame')
st.write(df)

# KPI 1: Número total de citações
total_quotes = df.shape[0]
st.metric(label="Número Total de Citações", value=total_quotes)

# KPI 2: Número de autores únicos
unique_authors = df['author'].nunique()
st.metric(label="Número de Autores Únicos", value=unique_authors)

# KPI 3: Citações mais recentes coletadas
most_recent_collection = df['_data_coleta'].max()
st.metric(label="Data da Coleta Mais Recente", value=most_recent_collection)

# Mostrar citações por autor
st.subheader('Citações por Autor')
quotes_by_author = df['author'].value_counts()
st.bar_chart(quotes_by_author)

# Mostrar algumas citações
st.subheader('Algumas Citações')
for index, row in df.iterrows():
    st.write(f"**{row['author']}**: {row['text']}")

