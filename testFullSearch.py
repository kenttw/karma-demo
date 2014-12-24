# -*- coding: utf-8 -*-
'''
Created on 2014年12月24日

@author: kent
'''
from pymongo import Connection
 
if __name__ == '__main__':
  
  # Connect to mongo
  conn = Connection(host='210.63.38.217',port=27017)
  db = conn['test_database']
  
  # Set the search term
  term = 'foo'
  
  # Run the search
  results = db.command('text', 'healthmap', search=term)
  
  # Print the results
  print(results)