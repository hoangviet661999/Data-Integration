import scrapy


class NguyenKimeSpider(scrapy.Spider):
    name = 'crawler'
    # allowed_domains = ['https://www.nguyenkim.com/may-giat-electrolux-inverter-9-kg-ewf9025bqwa.html']
    # start_urls = ['https://www.nguyenkim.com/may-giat-electrolux-inverter-9-kg-ewf9025bqwa.html']
    start_urls = 'https://www.nguyenkim.com/may-giat/page-?/'



    def start_requests(self):
        for i in range(8):
            start_url2 = self.start_urls.replace("?", str(i))
            yield scrapy.Request(start_url2, callback=self.parse)

    def parse(self, response):
        links =response.xpath('//div[@class="item-list product"]//a/@href').getall()
        for link in links:
            yield scrapy.Request(link, callback=self.parsePage)
        

    def parsePage(self, response):
        data = dict()
        title = response.xpath('//h1[@class="product_info_name"]//text()').get()
        price = response.xpath('//span[@class="nk-price-final"]//text()').get()
        url = response.request.url
        img = response.xpath('//ul[@class="nk-product-bigImg"]/li/div/img/@src').get()
        description = response.xpath('//tbody[@id="custom-scroll-popup-tskt"]//text()').getall()

        t, d =[], []
        for tit, des in zip(description[0::2], description[1::2]):
            t.append(tit)
            d.append(des)
        
        data['title'] = title
        data['price'] = price
        data['url'] = url
        data['img'] = img

        for i in range(len(t)):
            data[t[i]] = d[i]
        
        return data