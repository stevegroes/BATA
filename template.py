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
    start_offline_tweets('data/bata_2014.txt', time_factor=10000000)
	
	
def clip(lower, value, upper):
	return max(lower, min(value, upper))

positief = []
negatief = ['slecht']
begindata = {'previous':0.0}
pattern = re.compile('\W+')

def words(message):
    result = pattern.split(message)
    return result

@event('tweet')
def generate_sample(ctx, e):
	tweet = e.data
	print (ctx.count)
	sample = 0
	ctx.count += 1
	if ctx.count % 50 == 0:
		emit('debug', {'text': 'Log message #'+str(ctx.count)+'!'})
	
	# base sample on previous one
	
	try:
		print(tweet['text'])	
		if 'batavierenrace' in tweet['text']:
			sample = clip(-100, begindata['previous'] + 0.1, 100)
			print (sample)
		#elif negatief in tweet['text']:
			#sample = clip(-100, begindata['previous'] - 0.1, 100)
		#else:
			#sample = clip(-100, begindata['previous'], 100)
			#print("Error")
	except TypeError:
		pass
		print("Error2")
		
	# emit to outside world
	emit('sample',{
		'action': 'add',
		'value': sample
	})
	begindata = {'previous':sample}
	print (begindata)
	#try:
	#	tweet.pop(0)
	#except TypeError:
	#	pass
	# chain event
	#fire('tweet', delay=0.05)

