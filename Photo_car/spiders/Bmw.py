# -*- coding: utf-8 -*-
import scrapy
from Photo_car.items import PhotoCarItem

class BmwSpider(scrapy.Spider):
    name = 'Bmw'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class= 'uibox']")[1:]
        for uibox in uiboxs:
            title = response.xpath(".//div[@class='uibox-title']/a/text()").extract()[1]
            urls = uibox.xpath(".//ul/li/a/img/@src").extract()
            # for url in urls:
            #     url = response.urljoin(url)
            #     print(url)
            urls = list(map(lambda url:response.urljoin(url), urls))
            item = PhotoCarItem(title=title, urls=urls)
            yield item