from scrapy import Spider
from ..items import TILItem

class StackSpider(Spider):
    name = "til"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "https://www.reddit.com/r/todayilearned/top/?t=week",
    ]

    def parse(self, response):
        titles = response.xpath('//div/h3[@class="_eYtD2XCVieq6emjKBH3m"]/text()').extract()
        links = response.xpath('//div/a[@class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"]//@href').extract()

        for i in range(len(titles)):
            if (titles[i].startswith('TIL')):
                item = TILItem()
                item['title'] = titles[i]
                item['url'] = links[i]
                yield item
