import scrapy

class WoolworthsSpiderItem(scrapy.Item):
    breadcrumb = scrapy.Field()
    product_names = scrapy.Field()
