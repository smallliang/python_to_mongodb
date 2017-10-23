# -*- coding: utf-8 -*-
import scrapy
from python_to_mongodb.items import PythonToMongodbItem

class StackSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/']

    link_url = 'https://stackoverflow.com'

    def parse(self, response):
        ques_list = response.xpath('//*[@id="question-mini-list"]/div')
        print(len(ques_list))
        for question in ques_list:
            item = PythonToMongodbItem()
            title = question.xpath('div[2]/h3/a/text()')[0].extract()
            url = self.link_url + question.xpath('div[2]/h3/a/@href')[0].extract()
            print(title, url)
            item['title'] = title
            item['url'] = url
            yield item