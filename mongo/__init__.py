# -*- coding: utf-8 -*-
from mongo.ctx import *
from mongo.excel import *
import json

nms=get_db("nms")

class MongoDeal():
    def __init__(self,db):
        self.db=db

    def get(self,collection):
        c=self.db[collection]
        one=c.find_one()
        print(1)
    def find(self,collection,query={}):
        c=self.db[collection]
        l=c.find(query)
        return l

class MongoTest():
    def __init__(self, db,module):
        self.crud =MongoDeal(db)
        self.module=module
    def find(self,query={}):
        return self.crud.find(self.module,query)

if __name__ == "__main__":
    c=MongoTest(nms,"misc_house_mark")
    data=list(c.find({"marked":"store"}))
    doExcel(data)
    print (11)
    # json.dumps(c.find())

