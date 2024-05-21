## Transformação de Dados - Pesquisa de Mercado

Este módulo do projeto utiliza Pandas e SQLite para transformar e armazenar dados coletados sobre tênis esportivos do Mercado Livre. A seguir, são descritos os módulos e funcionalidades utilizados.

### Módulos Utilizados

#### `pandas`

Pandas é uma biblioteca essencial para manipulação e análise de dados em Python. No projeto, é usada para carregar, processar e analisar os dados dos tênis esportivos.

- **`pd.read_json`**: Lê dados de um arquivo JSON e retorna um DataFrame.
- **`df.head`**: Exibe as primeiras linhas do DataFrame.
- **`df['column_name'].fillna`**: Preenche valores nulos em uma coluna com um valor especificado.
- **`df['column_name'].astype`**: Converte o tipo dos dados em uma coluna.
- **`df['column_name'].str.replace`**: Substitui ocorrências de um padrão de string por outro.
- **`df.drop`**: Remove colunas ou linhas do DataFrame.
- **`pd.options.display.max_columns`**: Configura a exibição de todas as colunas do DataFrame.

#### `sqlite3`

SQLite3 é um banco de dados SQL leve e autônomo. É usado no projeto para armazenar os dados dos tênis esportivos.

- **`sqlite3.connect`**: Conecta ao banco de dados SQLite.
- **`df.to_sql`**: Salva os dados de um DataFrame em uma tabela do banco de dados SQL.
- **`conn.close`**: Fecha a conexão com o banco de dados.

#### `datetime`

A biblioteca `datetime` do Python fornece classes para manipulação de datas e horas. É usada no projeto para adicionar uma coluna com a data e hora atuais aos dados.

- **`datetime.now`**: Retorna a data e hora atuais.

### Estrutura do Código

O código do projeto está estruturado da seguinte forma:

1. **Definir o Caminho para o Arquivo JSONL**
    ```python
    jsonl_path = '../data/data.jsonl'
    ```

2. **Ler os Dados do Arquivo JSONL**
    ```python
    df = pd.read_json(jsonl_path, lines=True)
    print(df.head())
    ```

3. **Adicionar Colunas Fixas e Data de Coleta**
    ```python
    df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
    df['_data_coleta'] = datetime.now()
    ```

4. **Tratar Valores Nulos e Colunas Numéricas**
    ```python
    df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
    df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
    df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
    df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
    df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
    ```

5. **Remover Parênteses das Colunas `reviews_amount`**
    ```python
    df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
    df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)
    ```

6. **Calcular Valores Totais dos Preços**
    ```python
    df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
    df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100
    df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)
    ```

7. **Salvar os Dados no Banco de Dados SQLite**
    ```python
    conn = sqlite3.connect('../data/quotes.db')
    df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)
    conn.close()
    ```

8. **Configurar Pandas para Mostrar Todas as Colunas**
    ```python
    pd.options.display.max_columns = None
    print(df.head())
    ```

### Como Executar o Projeto

1. **Instale as dependências necessárias:**
    ```bash
    pip install pandas sqlite3
    ```

2. **Navegue até o diretório do projeto:**
    ```bash
    cd src/transformacao
    ```

3. **Execute o script de transformação:**
    ```bash
    python process_data.py
    ```

### Descrição dos Campos no DataFrame

- **`_source`**: URL da fonte de onde os dados foram coletados.
- **`_data_coleta`**: Data e hora em que os dados foram coletados.
- **`old_price`**: Preço antigo calculado a partir de `old_price_reais` e `old_price_centavos`.
- **`new_price`**: Preço novo calculado a partir de `new_price_reais` e `new_price_centavos`.
- **`reviews_rating_number`**: Avaliação média do produto.
- **`reviews_amount`**: Número de avaliações do produto.
