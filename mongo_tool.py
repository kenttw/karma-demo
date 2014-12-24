# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日

@author: kent
'''


from pymongo import MongoClient
import datetime

host = '210.63.38.217'
client = MongoClient( host , 27017)


db = client.test_database
# collection = db.test_collection
# print collection
def query(key):
#     res = td.find({"text":"\\馬英九\\"})
    res = db.runCommand('text', 'healthmap', search='馬英九')
    print res.count()

def insert_post(posts):
#     post = {"author": "Mike",
#              "text": "My first blog post!",
#              "tags": ["mongodb", "python", "pymongo"],
#              "date": datetime.datetime.utcnow()}
    for post in posts:
        td = db.test_database
        post_id = td.insert(post)
        print post_id