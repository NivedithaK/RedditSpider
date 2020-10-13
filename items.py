# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class QuoteItem(Item):
    # Fields of the item
    text = Field()
    author = Field()

class TILItem(Item):
    # Fields of the item
    title = Field()
    url = Field()