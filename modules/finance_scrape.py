#!/usr/bin/python

import urllib2
import json

symbols = ['GOOG', 'AAPL', 'NVDA', 'TSLA', 'IBM', 'KO']
request_url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22' +\
          '%22%2C%22'.join(symbols) +\
          '%22)%0A%09%09&format=json&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env&callback='

response = urllib2.urlopen(request_url).read()
data = json.loads(response)
quotes = data['query']['results']['quote']

for q in quotes:
    result = {}
    result['PE'] = q.get('PERatio', None)
    result['PB'] = q.get('PriceBook', None)
    result['PS'] = q.get('PriceSales', None)
    result['DY'] = q.get('DividendYield', None)
    result['SYMBOL'] = q.get('symbol', None)
    print json.dumps(result)
