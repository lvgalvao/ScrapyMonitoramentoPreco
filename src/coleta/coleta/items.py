# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductItem(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
    old_price_reais = scrapy.Field()
    old_price_centavos = scrapy.Field()
    new_price_reais = scrapy.Field()
    new_price_centavos = scrapy.Field()
    reviews_rating_number = scrapy.Field()
    reviews_amount = scrapy.Field()

