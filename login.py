# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser
import math

class SpiderNameSpider(scrapy.Spider):
    name="login_spider"
    allowed_domains = ['codechef.com']
    start_urls = ['https://www.codechef.com']

    def parse(self, response):
        data = {'name': 'username','pass': 'password'}
        return scrapy.FormRequest.from_response(response, formdata=data,callback=self.after_login)
        

    def after_login(self,response):
        open_in_browser(response)
        
    def power(a,b):
        #return sum of two numbers
        return pow(a,b)
    
    def Factorial(n):
        #return the factorial of a number
        return math.factorial(n)
        
        
        
