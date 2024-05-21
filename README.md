# ScrapyMonitoramentoPreco

Este README fornece uma visão geral clara e detalhada do projeto, incluindo a arquitetura, a estrutura de diretórios, as instruções de instalação e uso, além dos módulos específicos para extração, transformação e visualização de dados.

Uma ETL em Python para Monitoramento de Preço

## Uma ETL em Python para Monitoramento de Preço

Solução em Python para estratégias de pricing
Temos uma pipeline e uma ETL em Python que coleta, consolida e gera insights
sobre determinada cadeira de produtos

## Arquitetura
Uma ETL em Python para Web Scraping

- Extração - Scrapy
- Transformação e Load - Pandas
- Dashboard - Streamlit
- Banco de dados - Postgres

### Diagrama

![arquitetura](/pics/arquitetura.png)

### Excalidraw

[Excalidraw]https://link.excalidraw.com/l/8pvW6zbNUnD/4qYJqXpeRfP

### Estrutura de Diretórios
```plaintext
ScrapyMonitoramentoPreco/
├── scrapy_monitoramento/
│   ├── spiders/
│   │   └── preco_spider.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── transform.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md

## Documentação
## Como usar
## Módulos

Claro, Luciano! Aqui está um README detalhado para o projeto de monitoramento de preços usando Scrapy, Pandas, Postgres e Streamlit.

```markdown
# ScrapyMonitoramentoPreco

Uma ETL em Python para Monitoramento de Preço

## Resumo
Solução em Python para estratégias de pricing. Temos uma pipeline e uma ETL em Python que coleta, consolida e gera insights sobre determinada cadeira de produtos.

## Arquitetura
Uma ETL em Python para Web Scraping

- **Extração** - Scrapy
- **Transformação** - Pandas e Postgres
- **Dashboard** - Pandas e Streamlit

### Diagrama

![arquitetura](/pics/arquitetura.png)

### Excalidraw

[Excalidraw](https://link.excalidraw.com/l/8pvW6zbNUnD/4qYJqXpeRfP)

## Documentação

### Estrutura de Diretórios
```plaintext
ScrapyMonitoramentoPreco/
├── scrapy_monitoramento/
│   ├── spiders/
│   │   └── preco_spider.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── transform.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md
```

### Pré-requisitos
Certifique-se de ter o Python 3.8+ e o PostgreSQL instalado em seu sistema.

### Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/seu-usuario/ScrapyMonitoramentoPreco.git
cd ScrapyMonitoramentoPreco
pip install -r requirements.txt
```

### Como usar

#### Extração de Dados
Para iniciar a extração de dados usando Scrapy, execute:
```bash
cd scrapy_monitoramento
scrapy crawl preco_spider
```

#### Transformação de Dados
Após a extração, use o script de transformação para processar os dados:
```bash
cd transformacao
python transform.py
```

#### Executar o Dashboard
Para visualizar os dados e insights no Streamlit, execute:
```bash
cd dashboard
streamlit run app.py
```

## Módulos

### Scrapy (Extração)
A pasta `scrapy_monitoramento` contém o spider do Scrapy responsável por coletar os dados de preços dos produtos.

#### preco_spider.py
```python
import scrapy
from scrapy_monitoramento.items import PrecoItem

class PrecoSpider(scrapy.Spider):
    name = "preco_spider"
    start_urls = ['https://exemplo.com/produtos']

    def parse(self, response):
        for produto in response.css('div.produto'):
            item = PrecoItem()
            item['nome'] = produto.css('h2::text').get()
            item['preco'] = produto.css('span.preco::text').get()
            yield item
```

### Pandas e Postgres (Transformação)
A pasta `transformacao` contém scripts para transformar os dados extraídos e inseri-los no banco de dados Postgres.

#### transform.py
```python
import pandas as pd
from sqlalchemy import create_engine

# Carregar dados extraídos
df = pd.read_csv('path/to/extracted/data.csv')

# Transformações necessárias
df['preco'] = df['preco'].str.replace('R$', '').astype(float)

# Conectar ao Postgres e inserir dados
engine = create_engine('postgresql://usuario:senha@localhost:5432/precos')
df.to_sql('tabela_precos', engine, if_exists='replace', index=False)
```

### Streamlit (Dashboard)
A pasta `dashboard` contém a aplicação Streamlit para visualizar os dados e insights.

#### app.py
```python
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Conectar ao Postgres e carregar dados
engine = create_engine('postgresql://usuario:senha@localhost:5432/precos')
df = pd.read_sql('tabela_precos', engine)

# Visualizar dados no Streamlit
st.title('Monitoramento de Preços')
st.write(df)
```

## Contribuindo
Para contribuir com este projeto, por favor, envie um pull request ou abra uma issue para discutirmos as mudanças.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
```

Este README fornece uma visão geral clara e detalhada do projeto, incluindo a arquitetura, a estrutura de diretórios, as instruções de instalação e uso, além dos módulos específicos para extração, transformação e visualização de dados.