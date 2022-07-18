import pymongo
from scrapy.exceptions import DropItem
 
class MongoDBPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = connection["dcml"]
        self.collection = db["item_dmcl"]
 
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item

class DienmaycholonPipeline:
    def process_item(self, item, spider):
        return item