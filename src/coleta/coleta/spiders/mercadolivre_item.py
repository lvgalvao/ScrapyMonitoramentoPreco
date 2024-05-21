import scrapy
from coleta.items import ProductItem

class MercadoLivreSpider(scrapy.Spider):
    name = 'mercadolivreitem'
    start_urls = ['https://lista.mercadolivre.com.br/tenis-corrida-masculino']
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()
            
            item = ProductItem()
            item['brand'] = product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
            item['name'] = product.css('h2.ui-search-item__title::text').get()
            item['old_price_reais'] = prices[0] if len(prices) > 0 else None
            item['old_price_centavos'] = cents[0] if len(cents) > 0 else None
            item['new_price_reais'] = prices[1] if len(prices) > 1 else None
            item['new_price_centavos'] = cents[1] if len(cents) > 1 else None
            item['reviews_rating_number'] = product.css('span.ui-search-reviews__rating-number::text').get()
            item['reviews_amount'] = product.css('span.ui-search-reviews__amount::text').get()
            
            yield item

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)