# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from scrapy.exceptions import DropItem
 
class MongoDBPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = connection["dmx"]
        self.collection = db["item_dmx"]
 
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item

class DienmayxanhPipeline:
    def process_item(self, item, spider):
        return item