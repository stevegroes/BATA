from eca import *
from eca.generators import start_offline_tweets

import datetime
import textwrap

'''@event('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('data/batatweets.txt', 'chirp', time_factor=10000000)

@event('chirp')
def tweet(ctx, e):

'''  


 
@event('init')
def setup(ctx, e):
	fire('tweet', start_offline_tweets('data/bata_2014.txt', time_factor=10000000))
	
@event('tweet')
def echo(c,e):
    # we receive a tweet
    tweet = e.data
    #tweet['entities']
    media_items = tweet.get('entities', {}).get('media', [])
    #for mi in media_items:
        #if "media_url" in mi:
          
            #emit('tweet', mi['media_url'])
    #try:
    #    emit('tweet',tweet)
    #except UnicodeDecodeError:
    #    pass
	#emit('tweet', e.data)
	