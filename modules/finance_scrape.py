#!/usr/bin/python

import urllib2
import json
import logging
import re
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger('finance_scrape.py')

symbols = ['GOOG', 'AAPL', 'NVDA', 'TSLA', 'IBM', 'KO', 'MCD', 'TWX', 'DIS',
           'FB', 'YUM', 'TWTR', 'VIA', 'PYPL', 'AMZN', 'NFLX']


request_url = 'https://finance.google.com/finance?q={}'
pattern = re.compile('"pe_ratio">P/E.*?val">(.*?)</td>.*?latest_dividend-dividend_yield">Div/yield.*?val">(.*?)</td>', re.DOTALL)

for sym in symbols:
    response = urllib2.urlopen(request_url.format(sym)).read()
    found = pattern.findall(response)
    result = {}
    result['PE'] = found[0][0].strip()
    dy = found[0][1].strip()
    dy = dy.split('/')
    if len(dy) > 1:
        dy = dy[1]
    else:
        dy = ''
    result['DY'] = dy
    result['SYMBOL'] = sym
    print(json.dumps(result))
