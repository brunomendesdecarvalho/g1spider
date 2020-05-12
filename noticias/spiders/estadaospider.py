# -*- coding: utf-8 -*-
import scrapy


class EstadaospiderSpider(scrapy.Spider):
    name = 'estadaospider'
    start_urls = ['http://https://www.estadao.com.br//']

    custom_settings = {
        'DOWNLOAD_DELAY': 1.5 ,
        'DEPTH_LIMIT': 8 ,
        'ITEM_PIPELINES': {
            'noticias.pipelines.EstadaoPipeline': 400
        }
    }

    def parse(self, response):
        manchetes = list(response.xpath(".//figcaption[@class='title']/a/text()").extract())
        links = list(response.xpath(".//figcaption[@class='title']/a/@href").extract())

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
