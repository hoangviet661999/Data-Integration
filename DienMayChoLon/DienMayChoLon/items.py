# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DienmaycholonItem(scrapy.Item):
    ten = scrapy.Field()
    gia = scrapy.Field()
    loai_may = scrapy.Field()
    khoi_luong_giat = scrapy.Field()
    kieu_dong_co = scrapy.Field()
    cong_nghe_giat = scrapy.Field()
    bang_dieu_khien = scrapy.Field()
    chat_lieu = scrapy.Field()
    kich_thuoc = scrapy.Field()
    hang = scrapy.Field()
    url = scrapy.Field()

    pass
