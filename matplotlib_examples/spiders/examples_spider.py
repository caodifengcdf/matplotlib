# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibExamplesItem

class ExamplesSpiderSpider(scrapy.Spider):
    name = 'examples_spider'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index']

    def parse(self, response):
        sel = response.css('div.toctree-wrapper.compound')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
        cookies = {
            "_ga": "GA1.2.1097259192.1575111093",
            "__cfduid": "de6aa898697bdf831d95c918d56aa1cea1600614065",
            "_gid": "GA1.2.1993533781.1600614072",
            "cf_chl_1": "148522a2d305c9a; cf_chl_prog=a21",
            "cf_clearance": "34a006819917c51601113f503520c2c4db60bc3f-1600700185-0-1zdfea8b95z23b50a45zb8fb3924-250",
            "_gat": "1"
        }
        #le = LinkExtractor(restrict_css='div.toctree-wrapper.compound')  532个链接包含小标题的链接，需要去除

        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='index.html')
        links = le.extract_links(response)   #总共506个文件链接，点击文件链接后，获取下载链接

        print('################################################################')
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_download,cookies=cookies,headers=headers)

    def parse_download(self,response):
        le = LinkExtractor(restrict_css='a.reference.external')
        links = le.extract_links(response) #此方法无需拼接url
        url = links[0].url
        #url = response.css('a.reference.external::attr(href)')
        #url = response.urljion(url) #scrapy版本1.3.3有这功能，更新后报错，应该是取消了，需要使用ulilib模块

        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        example = MatplotlibExamplesItem()
        example['file_urls']= [url]
        return example

        
         
