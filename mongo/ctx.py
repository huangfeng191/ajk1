# -*- coding: utf-8 -*-
from pymongo.mongo_client import MongoClient


def get(ns,key,default_value=None):
    r={
       "sys":{
           "mongodb": {"host": "mongodb://127.0.0.1:27017"},
           "db_prefix": "s_",  # 数据库前缀
       }
    }

    return (r[ns] and r[ns].get(key,default_value)) or default_value

DB_PREFIX = get("sys","db_prefix")

mdb = MongoClient(maxPoolSize=get("sys","maxPoolSize", 128), connect=False, ** get("sys","mongodb")) # Mongodb数据库

def get_db(module):

  return mdb[DB_PREFIX + module]


