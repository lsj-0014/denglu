# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EstateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    job_way = scrapy.Field()
    job_house = scrapy.Field()
    job_area = scrapy.Field()
    job_orientation = scrapy.Field()
    job_address = scrapy.Field()
    job_price = scrapy.Field()
    pass

