# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class PythonToMongodbPipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient(host='127.0.0.1',
                                         port=27017)
        self.db = self.connection['test']  # 获得数据库的句柄
        self.coll = self.db['collection']  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写
