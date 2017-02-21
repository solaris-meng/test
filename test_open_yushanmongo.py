

from pymongo import MongoClient
import pymongo

with MongoClient('mongodb://dds-2ze74067495e13242.mongodb.rds.aliyuncs.com:3717') as client:
    client.yushan.authenticate('yushan','yushan')
    db = client.yushan
    c = db['pvlog']


    for i in c.find({'c1':'cfa8cf5c9dc946d4a49aa4ef94e84654'}):
        print(i)
        break
