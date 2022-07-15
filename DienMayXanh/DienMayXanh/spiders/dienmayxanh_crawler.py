import scrapy
from ..items import DienmayxanhItem
class Spider(scrapy.Spider):
    name = 'crawler'
    page_number = 1
    base_url = 'https://www.dienmayxanh.com'
    api_url = 'https://www.dienmayxanh.com/Category/FilterProductBox?c=1944&o=9&pi={}'
    start_urls = [api_url.format(0)]
    # download_delay = 1
    def parse(self, response):
        all_washers = response.xpath('//a/@href').extract()
        all_washers = [url for url in all_washers if url.startswith('/may-giat')]
        for washer in all_washers:
            washer_url = self.base_url + washer
            yield scrapy.Request(washer_url, callback= self.parse_product)

    def parse_product(self,response):
        price = response.xpath('//p[@class = "box-price-present"]/text()').extract_first()
        name = response.xpath('//p[@class = "parameter__title"]/text()').extract_first()
        parameter_list = response.xpath('//ul[contains(@class, "parameter__list")]')

        item = DienmayxanhItem()
        item['ten'] = name.replace('Thông số kỹ thuật', '')
        item['gia'] = price
        item['url'] = response.request.url  
        item['loai_may'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['khoi_luong_giat'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['kieu_dong_co'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['cong_nghe_giat'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['tien_ich'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['bang_dieu_khien'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['chat_lieu'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['kich_thuoc_va_khoi_luong'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]//div[@class="liright"]//span/text()').extract()
        item['hang'] = parameter_list.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "active", " " ))]//li[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//div[@class="liright"]//span/text()').extract()

        # next_page = 'https://www.dienmayxanh.com/Category/FilterProductBox?c=1944&ext=sp2020&o=9&pi={}' + str(Spider.page_number)
        if Spider.page_number <= 20:
            Spider.page_number += 1
            yield scrapy.Request(url = self.api_url.format(Spider.page_number), callback= self.parse)
        yield item