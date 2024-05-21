# Documentação do Dashboard

## Pesquisa de Mercado - Tênis Esportivos no Mercado Livre

Este projeto utiliza o Streamlit para criar uma aplicação interativa que analisa dados de tênis esportivos do Mercado Livre. A seguir, são descritos os módulos e funcionalidades utilizados.

### Módulos Utilizados

#### `streamlit`

Streamlit é um framework de código aberto que permite criar aplicações web interativas em Python de forma rápida e fácil. Abaixo estão os principais componentes do Streamlit usados no projeto:

- **`st.title`**: Define o título da aplicação.
- **`st.subheader`**: Define um subtítulo para as seções da aplicação.
- **`st.columns`**: Cria uma disposição em colunas, permitindo organizar os elementos da aplicação lado a lado.
- **`st.metric`**: Exibe KPIs (Key Performance Indicators) de forma visualmente atraente.
- **`st.bar_chart`**: Cria gráficos de barras para visualização de dados.
- **`st.write`**: Exibe tabelas e outros tipos de dados.

#### `pandas`

Pandas é uma biblioteca essencial para manipulação e análise de dados em Python. No projeto, é usada para carregar, processar e analisar os dados dos tênis esportivos.

- **`pd.read_sql_query`**: Lê os dados de uma tabela SQL e retorna um DataFrame.
- **`df.shape`**: Retorna o número de linhas e colunas do DataFrame.
- **`df['column_name'].nunique`**: Conta o número de valores únicos em uma coluna.
- **`df['column_name'].mean`**: Calcula a média dos valores em uma coluna.
- **`df['column_name'].value_counts`**: Conta a frequência dos valores únicos em uma coluna.
- **`df.groupby('column_name').mean`**: Agrupa os dados por uma coluna e calcula a média de cada grupo.
- **`df.sort_values`**: Ordena os valores de um DataFrame.

#### `sqlite3`

SQLite3 é um banco de dados SQL leve e autônomo. É usado no projeto para armazenar os dados dos tênis esportivos.

- **`sqlite3.connect`**: Conecta ao banco de dados SQLite.
- **`pd.read_sql_query`**: Executa uma consulta SQL e retorna os resultados como um DataFrame.

### Estrutura do Código

O código do projeto está estruturado da seguinte forma:

1. **Conectar ao Banco de Dados**
    ```python
    conn = sqlite3.connect('../data/quotes.db')
    df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)
    conn.close()
    ```

2. **Título da Aplicação**
    ```python
    st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')
    ```

3. **KPIs Principais**
    ```python
    st.subheader("KPIs Principais")
    col1, col2, col3 = st.columns(3)

    total_items = df.shape[0]
    col1.metric(label="Número Total de Itens", value=total_items)

    unique_brands = df['brand'].nunique()
    col2.metric(label="Número de Marcas Únicas", value=unique_brands)

    average_new_price = df['new_price'].mean()
    col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")
    ```

4. **Análises Específicas**
    - **Marcas mais encontradas até a 10ª página**
        ```python
        st.subheader('Marcas mais encontradas até a 10ª página')
        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = df.head(500)['brand'].value_counts().sort_values(ascending=False)
        col1.bar_chart(top_10_pages_brands)
        col2.write(top_10_pages_brands)
        ```

    - **Preço médio por marca**
        ```python
        st.subheader('Preço médio por marca')
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
        col1.bar_chart(average_price_by_brand)
        col2.write(average_price_by_brand)
        ```

    - **Satisfação por marca**
        ```python
        st.subheader('Satisfação por marca')
        col1, col2 = st.columns([4, 2])
        df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
        satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
        col1.bar_chart(satisfaction_by_brand)
        col2.write(satisfaction_by_brand)
        ```

### Como Executar o Projeto

1. **Instale as dependências necessárias:**
    ```bash
    pip install streamlit pandas sqlite3
    ```

2. **Navegue até o diretório do projeto:**
    ```bash
    cd src/dashboard
    ```

3. **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```

4. **Acesse o aplicativo no navegador:**
    Abra `http://localhost:8501` no seu navegador para visualizar o aplicativo Streamlit.
