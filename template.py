from eca import *
from eca.generators import start_offline_tweets

import random
import datetime
import textwrap
import pprint
import re

@event('init')
def setup(ctx, e):
	
	
	fire('tweet', start_offline_tweets('batatweets.txt', time_factor=100000))
	
@event('tweet')
def echo(c,e):
	emit('tweet', e.data)
	
## rolling chart

from eca import *

import random

def add_request_handlers(httpd):
    httpd.add_content('/lib/', 'template_static/lib')
    httpd.add_content('/style/', 'template_static/style')
@event('init')
def setup(ctx, e):
    ctx.count = 0
    ctx.samples = {
        'sensor0': 0.0,
        'sensor1': 0.0
    }

    fire('sample', {
        'previous': 0.0,
        'name': 'sensor0',
        'failure-chance': 0.0,
        'reboot-chance': 1.0,
        'delay': 0.05
    })

    fire('sample', {
        'previous': 0.0,
        'name': 'sensor1',
        'failure-chance': 0.05,
        'reboot-chance': 0.1,
        'delay': 0.05
    })

    fire('sample', {
        'previous': None,
        'name': 'sensor2',
        'failure-chance': 0.2,
        'reboot-chance': 0.8,
        'delay': 0.1
    })

    fire('tick')


def clip(lower, value, upper):
    return max(lower, min(value, upper))

@event('sample')
@condition(lambda c,e: e.get('previous') is not None)
def generate_sample(ctx, e):
    sample = e.get('previous')
    if e.get('failure-chance') > random.random():
        sample = None
        del ctx.samples[e.get('name')]
    else:
        sample = clip(-100, e.get('previous') + random.uniform(+5.0, -5.0), 100)
        ctx.samples[e.get('name')] = sample

    data = dict(e.data)
    data.update({'previous': sample})
    fire('sample', data, delay=e.get('delay'))

@event('sample')
@condition(lambda c,e: e.get('previous') is None)
def try_reboot(ctx, e):
    sample = e.get('previous')
    if e.get('reboot-chance') > random.random():
        sample = random.uniform(100,-100)
        ctx.samples[e.get('name')] = sample

    data = dict(e.data)
    data.update({'previous': sample})
    fire('sample', data, delay=e.get('delay'))


@event('tick')
def tick(ctx, e):
    emit('sample',{
        'action': 'add',
        'values': ctx.samples
    })
    fire('tick', delay=0.05);


