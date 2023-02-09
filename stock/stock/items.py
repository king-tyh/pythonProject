# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name  =  scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    forum = scrapy.Field()
    money_stream = scrapy.Field()
    data = scrapy.Field()
    price = scrapy.Field()
    range = scrapy.Field()
    increment = scrapy.Field()
    turnover = scrapy.Field()
    turnvolume = scrapy.Field()
    amplitude = scrapy.Field()
    highest = scrapy.Field()
    lowest = scrapy.Field()
    begin = scrapy.Field()
    history = scrapy.Field()
    volume_rate = scrapy.Field()
    turnover_rate = scrapy.Field()
    pe_rate = scrapy.Field()
    market_rate = scrapy.Field()

