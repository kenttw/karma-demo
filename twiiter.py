# -*- coding: utf-8 -*-
'''
Created on 2014年12月23日

@author: kent
'''
import twitter ,json , mongo_tool

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = '6HIso4B87aVs3Xn2fivg9SAPt'
CONSUMER_SECRET ='RIUaMqK8GGpFzrxrJ6KHwpaDU5kE1grLTKnYp4HWU27JZEfiNZ'
OAUTH_TOKEN = '1574625410-nHrGzqfxHqtcmFLQ07XAcuXjKJzZ63znw09wGWF'
OAUTH_TOKEN_SECRET = 'v6alkphj79URiRb85TM7w6CtRgGBM5kBfExG3R4OYuHnY'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print twitter_api

def getTrend():
    # The Yahoo! Where On Earth ID for the entire world is 1.
    # See https://dev.twitter.com/docs/api/1.1/get/trends/place and
    # http://developer.yahoo.com/geo/geoplanet/
    
    WORLD_WOE_ID = 1
    US_WOE_ID = 23424977
    
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special case keyword argument.
    
    world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
    us_trends = twitter_api.trends.place(_id=US_WOE_ID)
    
    
    import json
    
    print json.dumps(world_trends, indent=1)
    print
    print json.dumps(us_trends, indent=1)
    
    world_trends_set = set([trend['name'] 
                            for trend in world_trends[0]['trends']])
    
    us_trends_set = set([trend['name'] 
                         for trend in us_trends[0]['trends']]) 
    
    common_trends = world_trends_set.intersection(us_trends_set)
    
    print common_trends

def search(q = '#MentionSomeoneImportantForYou'):
    # XXX: Set this variable to a trending topic, 
    # or anything else for that matter. The example query below
    # was a trending topic when this content was being developed
    # and is used throughout the remainder of this chapter.
    
    count = 100
    
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    
    search_results = twitter_api.search.tweets(q=q, count=count)
    
    statuses = search_results['statuses']
    
    
    # Iterate through 5 more batches of results by following the cursor
    
    for _ in range(5):
        print "Length of statuses", len(statuses)
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more results when next_results doesn't exist
            break
            
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
    
    # Show one sample search result by slicing the list...
#     print json.dumps(statuses[0], indent=1)
    return statuses

def extract(statuses , num=5 ):
    status_texts = [ status['text'] 
                 for status in statuses ]

    screen_names = [ user_mention['screen_name'] 
                     for status in statuses
                         for user_mention in status['entities']['user_mentions'] ]
    
    hashtags = [ hashtag['text'] 
                 for status in statuses
                     for hashtag in status['entities']['hashtags'] ]
    
    # Compute a collection of all words from all tweets
    words = [ w 
              for t in status_texts 
                  for w in t.split() ]
    
    # Explore the first 5 items for each...
    
    print json.dumps(status_texts[0:num], indent=1 ,ensure_ascii=False )
    print json.dumps(screen_names[0:num], indent=1 , ensure_ascii=False) 
    print json.dumps(hashtags[0:num], indent=1 , ensure_ascii=False)
    print json.dumps(words[0:num], indent=1 , ensure_ascii=False)
    
if __name__ == "__main__":
#     statuses = search(q='馬英九')
#     extract(statuses=statuses,num=5)
#     mongo_tool.insert_post(statuses)
    mongo_tool.query('aaa')

    pass
        
