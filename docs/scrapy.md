# Scrapy

## Criando um projet

Precisamos criar um o nosso projeto

Vamos usar o scrapy e ele já criar uma estrutura de projeto, assim conseguimos parametrizar algumas classes para acelerar o desenvolvimento utilizando o framework  do que queremos coletar

```bash
scrapy startproject coleta
```

Vamos fazer uma leve análise

```bash
scrapy shell
```

Precisamos criar nossa spider

```bash
scrapy genspider mercadolivre mercadolivre.com.br
```

```bash
scrapy shell
```

```python
>>> fetch('https://lista.mercadolivre.com.br/tenis-corrida-masculino')
```

```python
>>> response
```

```python
>>> response.text
```
response.css('div.ui-search-result__content').get()

products = response.css('div.ui-search-result__content')


len(products)


### Brand
products.xpath('//*[@id=":Ral5e6:"]/div[2]/div/div[2]/span/text()').get()
products.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()

### Nome
products.css('h2.ui-search-item__title::text').get()
products.xpath('//*[@id=":Ral5e6:"]/div[2]/div/div[2]/a/h2/text()').get()

### Old price real
products.css('span.andes-money-amount__fraction::text').get()


### Old price centavos

andes-money-amount__cents.andes-money-amount__cents--superscript-16

products.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-16::text').get()

### New price reais
products.css('span.andes-money-amount__fraction::text').get()

products[0].css('span.andes-money-amount__fraction::text').getall()

## Review

ui-search-reviews__rating-number

### New price centavos
products.xpath('//*[@id=":Ral5e6:"]/div[2]/div/div[3]/div[1]/div/div/span[1]/span[4]/text()').get()

CSS Selectors e XPath são duas linguagens de consulta diferentes usadas para selecionar elementos em documentos HTML e XML. Ambos são amplamente usados em web scraping, testes automatizados, e manipulação de documentos. Aqui está uma comparação detalhada entre os dois:

### Proxima pagina

next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()



### CSS Selectors

#### Vantagens
1. **Sintaxe Simples**: CSS Selectors têm uma sintaxe mais simples e legível, especialmente para seleções básicas.
2. **Desempenho**: Em muitos casos, CSS Selectors podem ser mais rápidos, já que muitos motores de renderização da web são otimizados para CSS.
3. **Popularidade**: São amplamente utilizados em desenvolvimento web para estilizar páginas, tornando-os familiares para muitos desenvolvedores.
4. **Suporte Padrão**: Suportado nativamente em muitas bibliotecas de scraping (como BeautifulSoup e Scrapy).

#### Desvantagens
1. **Limitações de Consulta**: CSS Selectors não têm a mesma flexibilidade e poder de expressão que XPath para consultas complexas.
2. **Suporte Limitado para XML**: Embora possam ser usados para XML, CSS Selectors são menos comuns e menos poderosos nesse contexto comparado ao XPath.

#### Exemplos
- Selecionar um elemento `div` com uma classe específica:
  ```css
  div.example
  ```
- Selecionar todos os elementos `a` dentro de um `div` com ID `container`:
  ```css
  #container a
  ```
- Selecionar o primeiro elemento `p` dentro de um `div`:
  ```css
  div > p:first-child
  ```

### XPath

#### Vantagens
1. **Flexibilidade e Poder**: XPath é extremamente poderoso e flexível, permitindo consultas muito complexas.
2. **Suporte Completo para XML**: XPath foi projetado para trabalhar com XML, tornando-o ideal para manipulação de documentos XML.
3. **Seleção Relativa**: Permite navegar no documento relativo a um nó, usando eixos como `parent`, `ancestor`, `sibling`, etc.
4. **Filtragem Avançada**: Suporta filtros avançados e funções para manipulação de strings, números, e booleanos.

#### Desvantagens
1. **Sintaxe Complexa**: A sintaxe de XPath pode ser mais complexa e menos intuitiva, especialmente para consultas simples.
2. **Desempenho**: Pode ser mais lento em algumas implementações devido à sua flexibilidade e poder.

#### Exemplos
- Selecionar todos os elementos `div` com uma classe específica:
  ```xpath
  //div[@class='example']
  ```
- Selecionar todos os elementos `a` dentro de um `div` com ID `container`:
  ```xpath
  //div[@id='container']//a
  ```
- Selecionar o primeiro elemento `p` dentro de um `div`:
  ```xpath
  //div/p[1]
  ```

### Comparação em Uso

Vamos comparar como selecionar um elemento `span` com várias classes usando ambos:

#### CSS Selector
```css
span.andes-money-amount.andes-money-amount-combo__previous-value.andes-money-amount--previous.andes-money-amount--cents-superscript
```

#### XPath
```xpath
//span[contains(@class, 'andes-money-amount') and contains(@class, 'andes-money-amount-combo__previous-value') and contains(@class, 'andes-money-amount--previous') and contains(@class, 'andes-money-amount--cents-superscript')]
```

### Escolhendo Entre CSS Selectors e XPath

- **Use CSS Selectors** se:
  - Você está realizando consultas simples.
  - Está trabalhando principalmente com HTML.
  - Você prefere uma sintaxe mais curta e intuitiva.
  - O desempenho é uma consideração crítica.

- **Use XPath** se:
  - Você precisa realizar consultas complexas.
  - Está manipulando documentos XML.
  - Precisa de filtragem avançada ou seleção relativa.
  - Está confortável com uma sintaxe mais complexa e poderosa.

Em resumo, a escolha entre CSS Selectors e XPath depende das necessidades específicas do seu projeto e do seu conforto com cada linguagem. Ambos têm suas vantagens e desvantagens, e podem ser usados de forma complementar em muitos casos.


## Como rodar nossos spider

```bash
scrapy crawl mercadolivre

>>>
```

## Salvar

```bash
scrapy crawl mercadolivreitem -o ../../data/data.jsonl
```