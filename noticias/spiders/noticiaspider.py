# -*- coding: utf-8 -*-
import scrapy


class NoticiaspiderSpider(scrapy.Spider):
    name = 'globospider'
    start_urls = ['https://g1.globo.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': 1.5 ,
        'DEPTH_LIMIT': 8
    }

    def parse(self, response):
        manchetes = list(response.xpath(".//div[@class='_et']/a[@href]/text()").extract())
        links = list(response.xpath(".//div[@class='_et']/a/@href").extract())

        for manchete, link in zip(manchetes, links):
            yield {
                'Manchete': manchete ,
                'Link': link ,
            }

        next_page = response.xpath(".//div[@class='load-more gui-color-primary-bg']/a/@href").extract_first()

        if (next_page):
            yield scrapy.Request(
                response.urljoin(next_page), 
                callback=self.parse
            )