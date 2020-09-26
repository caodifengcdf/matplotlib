# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.parse import urlparse
from scrapy.pipelines.files import FilesPipeline
from os.path import basename, dirname, join

class MatplotlibExamplesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        #request.url返回请求链接，urlparse(request.url)返回ParseResult(scheme='https', netloc='matplotlib.org', path='/examples/animation/animate_decay.html', params='', query='', fragment='')
        path = urlparse(request.url).path #返回'/examples/animation/animate_decay.py'
        file_name = path.split('/')[-1]
        return file_name

