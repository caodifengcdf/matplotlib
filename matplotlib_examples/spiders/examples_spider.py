# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import ExampleItem

class ExamplesSpiderSpider(scrapy.Spider):
    name = 'examples_spider'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index']

    def parse(self, response):
        sel = response.css('div.toctree-wrapper.compound')
        #le = LinkExtractor(restrict_css='div.toctree-wrapper.compound')  532个链接包含小标题的链接，需要去除

        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='index.html')
        urls = le.extract_links(response)   #总共506个文件链接，点击文件链接后，获取下载链接
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_download)

    def parse_download(self,response):
        le = LinkExtractor(restrict_css='a.reference.external')
        urls = le.extract_links(response)

        example = ExampleItem()
        example['file_urls']= urls[0]
        return example

        
         
