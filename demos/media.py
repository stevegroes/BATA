from eca import *
from eca.generators import start_offline_tweets

import datetime
import textwrap

@event('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('data/batatweets.txt', 'chirp', time_factor=None)

@event('chirp')
def tweet(ctx, e):
    
    # we receive a tweet
    tweet = e.data
    #tweet['entities']
    media_items = tweet.get('entities', {}).get('media', [])
    for mi in media_items:
        if "media_url" in mi:
          
            emit('tweet', mi['media_url'])
 