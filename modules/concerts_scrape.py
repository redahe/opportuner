#!/usr/bin/python

import urllib2
import re
import json
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger('concerts_scrape.py')

pattern = re.compile('<div class="event event_horizontal">.*?<a href="(.*?)".*?src="(.*?)".*?class="event__name">(.*?)</a>.*?<div class="event__date">(.*?)</div>', re.DOTALL)
# pattern = re.compile('<div class="event event_horizontal">.*?<a href="(.*?)".*?src="(.*?)"', re.DOTALL)


for page in range(5):
    request_url = 'http://www.concert.ru/Home/Events?Page={}&ActionTypeID=1&GenreTypeID=2'.format(page)
    response = urllib2.urlopen(request_url).read()
    lst = pattern.findall(response)
    for t in lst:
        result = {'img': 'http://www.concert.ru' + t[1],
                  'link': 'http://www.concert.ru' + t[0],
                  'name': t[2],
                  'time': t[3].strip()}
        print(json.dumps(result).encode('utf-8'))
