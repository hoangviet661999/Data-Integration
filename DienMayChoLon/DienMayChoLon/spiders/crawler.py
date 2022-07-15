import scrapy
import json
from ..items import DienmaycholonItem
class Spider(scrapy.Spider):
    name = 'crawler'
    page_number = 1
    base_url = 'https://dienmaycholon.vn/may-giat/'
    api_url = 'https://dienmaycholon.vn/api/product/cate?id=3&page={}'
    start_urls = [api_url.format(0)]
    # download_delay = 1
    def parse(self, response):
        data = json.loads(response.body)
        for washer in range(len(data['data']['data'])):
            washer_name = data['data']['data'][washer]['alias']
            washer_url = self.base_url + washer_name
            yield scrapy.Request(washer_url, callback= self.parse_product)
       
    def parse_product(self,response): 
        parameter_list = response.xpath('//nav[@class = "list_specifications"]//ul//li//p/text()').extract()

        item = DienmaycholonItem()
        item['ten'] = response.xpath('//div[@class = "name_pro_detail"]//h1/text()').extract()[0]
        item['gia'] = response.xpath('//div[@class = "price_sale"]//span/text()').extract_first()
        item['url'] = response.request.url  
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Loại máy giặt':
                item['loai_may'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Khối lượng giặt':
                item['khoi_luong_giat'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Động cơ':
                item['kieu_dong_co'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Công nghệ giặt':
                item['cong_nghe_giat'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Bảng điều khiển':
                item['bang_dieu_khien'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Lồng Giặt':
                item['chat_lieu'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Kích thước (R*S*C)':
                item['kich_thuoc'] = parameter_list[i+1]
                break
        for i in range(len(parameter_list)):
            if parameter_list[i] == 'Hãng sản xuất':
                item['hang'] = parameter_list[i+1]
                break
        
        if Spider.page_number <= 20:
             Spider.page_number += 1
             yield scrapy.Request(url = self.api_url.format(Spider.page_number), callback= self.parse)
        yield item