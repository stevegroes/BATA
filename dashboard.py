from eca import *
from eca.generators import start_offline_tweets

import random
import datetime
import textwrap
import pprint
import re

## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
# root_content_path = 'template_static'


# binds the 'setup' function as the action for the 'init' event
# the action will be called with the context and the event
@event('init')
def setup(ctx, e):
    ctx.count = 0
    fire('tweet', start_offline_tweets('data/bata_2014.txt', time_factor=100000))
	
stopwords = ['hup', 'succes', 'kom op']
@event('tweet')
def echo(c,e):
	tweet = e.data
	try:
		for word in stopwords:
			if word in tweet['text']:
				emit ('tweet', tweet)
	except TypeError:
		pass

	
