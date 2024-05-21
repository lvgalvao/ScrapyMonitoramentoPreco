# Projeto Piloto

## Extração

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

```bash
scrapy runspider quotes_spider.py -o quotes.csv
```
## Tranformação e Load

```python
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
```

```bash
python transform.py
```

## Dashboard

```python
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
```

```bash
streamlit run app.py
```