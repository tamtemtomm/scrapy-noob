import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://chocolate.co.uk/collections/all"]

    def parse(self, response):
        products = response.css('product-item')
        for product in products:
            yield{
                'name': product.css('a.product-item-meta__title::text').get(),
                'price': product.css('span.price').get().replace('<span class="price price--highlight">\n              <span class="visually-hidden">Sale price</span>', '').replace('</span>', ''),
                'url': product.css('div.product-item-meta a').attrib['href']    
            }
        
        pass
