import scrapy
from ..items  import WoolworthsSpiderItem
class WoolworthsSpider(scrapy.Spider):
    name = 'woolworths'
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def parse(self, response):
        # Extract breadcrumb
        breadcrumb = response.css('.breadcrumb-list a span::text').getall()

        # Extract product names
        product_names = response.css('.shelfProductTile-description span::text').getall()

        # Create a WoolworthsSpiderItem instance
        item = WoolworthsSpiderItem()
        item['breadcrumb'] = breadcrumb
        item['product_names'] = product_names

        # Yield the item to output it
        yield item
