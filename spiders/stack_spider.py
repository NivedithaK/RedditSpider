from scrapy import Spider
from ..items import QuoteItem

class QuoteSpider(Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/",
    ]

    def parse(self, response):
        block = response.xpath('//div[@class="quote"]/div')
        quotes = block.xpath(
            '//div/span[@class="text"]/text()').extract()
        authors = block.xpath(
            '//div/span/small[@class="author"]/text()').extract()

        for i in range(len(quotes)):
            item = QuoteItem()
            item['text'] = quotes[i]
            item['author'] = authors[i]
            yield item
