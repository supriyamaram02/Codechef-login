# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser

class SpiderNameSpider(scrapy.Spider):
    allowed_domains = ['codechef.com']
    start_urls = ['https://www.codechef.com']

    def parse(self, response):
        data = {'name': 'usernamw','pass': 'password'}
        return scrapy.FormRequest.from_response(response, formdata=data,callback=self.after_login)
        

    def after_login(self,response):
        open_in_browser(response)
        
        
        
