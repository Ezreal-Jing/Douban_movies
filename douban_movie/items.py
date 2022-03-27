# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #ID = scrapy.Field()
    comments = scrapy.Field()
    rating = scrapy.Field()
    #votes = scrapy.Field()

