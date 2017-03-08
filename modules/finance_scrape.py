#!/usr/bin/python

import urllib2
import json

symbols = ['GOOG', 'AAPL', 'NVDA', 'TSLA', 'IBM', 'KO', 'MCD', 'TWX', 'DIS',
           'FB', 'YUM', 'TWTR', 'VIA', 'PYPL', 'AMZN', 'NFLX']


request_url = 'http://finance.yahoo.com/d/quotes.csv?s=' +\
    ','.join(symbols) + '&f=rp6p5ys'


response = urllib2.urlopen(request_url).read()

for q in response.splitlines():
    q = q.split(',')
    result = {}
    result['PE'] = q[0]
    result['PB'] = q[1]
    result['PS'] = q[2]
    result['DY'] = q[3]
    result['SYMBOL'] = q[4]
    print json.dumps(result)
