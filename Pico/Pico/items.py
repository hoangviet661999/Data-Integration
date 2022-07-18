# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PicoItem(scrapy.Item):
    ten = scrapy.Field()
    gia = scrapy.Field()
    loai_may = scrapy.Field()
    khoi_luong_giat = scrapy.Field()
    tien_ich = scrapy.Field()
    bang_dieu_khien = scrapy.Field()
    kich_thuoc= scrapy.Field()
    hang = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
