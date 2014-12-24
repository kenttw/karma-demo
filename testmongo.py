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
collection = db.test_collection
print collection

def insert_post():
    post = {"author": "Mike",
             "text": "My first blog post!",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()}
    
    posts = db.posts
    post_id = posts.insert(post)
    print post_id