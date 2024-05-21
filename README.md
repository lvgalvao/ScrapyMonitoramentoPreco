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
```

## Documentação

[Github Pages](https://lvgalvao.github.io/ScrapyMonitoramentoPreco/)

## Como usar
## Módulos