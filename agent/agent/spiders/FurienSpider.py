# -*- coding: utf-8 -*-
import scrapy


class FurienspiderSpider(scrapy.Spider):
    name = 'FurienSpider'
    allowed_domains = ['furien.jp']
    start_urls = ['http://furien.jp/']

    def parse(self, response):
        pass
