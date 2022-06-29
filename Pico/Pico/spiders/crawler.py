import scrapy
from ..items import PicoItem

class Spider(scrapy.Spider):
    name = 'crawler'
    page_number = 1
    base_url = 'https://pico.vn/may-giat-nhom-72.html'
    api_url = 'https://pico.vn/may-giat-nhom-72.html?&pageIndex={}'
    start_urls = [api_url.format(1)]
    # download_delay = 1
    def parse(self, response):
        all_washers = response.xpath('//h6/a/@href').extract()
        for washer_url in all_washers:
            yield scrapy.Request(washer_url, callback= self.parse_product)
       
    def parse_product(self,response): 

        item = PicoItem()
        item['ten'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "widget-header--button-close-icon", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "chat-button--img", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "product-title", " " ))]/text()').extract()[0]
        item['gia'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]//strong/text()').extract_first()
        parameter_list  = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "spec-title", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "spec-content", " " ))]//span/text()').extract()
        for idx in range(len(parameter_list)):
            if 'Loại máy giặt' in parameter_list[idx]:
                item['loai_may'] = parameter_list[idx+1]
                break
        for idx in range(len(parameter_list)):
            if 'Khối lượng giặt' in parameter_list[idx]:
                item['khoi_luong_giat'] = parameter_list[idx+1]
                break
        for idx in range(len(parameter_list)):
            if 'Các chế độ giặt' in parameter_list[idx]:
                item['tien_ich'] = parameter_list[idx+1]
                break
        for idx in range(len(parameter_list)):
            if 'bảng điều khiển' in parameter_list[idx]:
                item['bang_dieu_khien'] = parameter_list[idx+1]
                break
        for idx in range(len(parameter_list)):
            if 'Kích thước' in parameter_list[idx]:
                item['kich_thuoc'] = parameter_list[idx+1]
                break

        for idx in range(len(parameter_list)):
            if 'Hãng' in parameter_list[idx]:
                item['hang'] = parameter_list[idx+1]
                break
        if Spider.page_number <= 50:
            Spider.page_number += 1
            yield scrapy.Request(url = self.api_url.format(Spider.page_number), callback= self.parse)
        yield item