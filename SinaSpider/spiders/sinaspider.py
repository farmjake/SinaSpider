# -*- coding: utf-8 -*-
import scrapy


class SinaspiderSpider(scrapy.Spider):
    name = "sinaspider"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
        'http://www.sina.com.cn/',
    )

    def parse(self, response):
        pass
