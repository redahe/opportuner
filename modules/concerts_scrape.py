#!/usr/bin/python

import urllib2
import re
import json

pattern = re.compile('<div itemscope.*?<img src="(.*?)".*?<time .*?>(.*?)</time>.*?<div itemprop="name">(.*?)</div>.*?<a class="linkBuyTicket" href="(.*?)"', re.DOTALL)

for page in xrange(5):
    request_url = 'http://www.concert.ru/Actions.aspx?ActionTypeID=1&GenreTypeID=2&page={}'.format(page)
    response = urllib2.urlopen(request_url).read()
    lst = pattern.findall(response)
    for t in lst:
        result = {'img': 'http://www.concert.ru/' + t[0],
                  'link': 'http://www.concert.ru/' + t[3],
                  'name': t[2],
                  'time': t[1].strip()}
        print json.dumps(result).encode('utf-8')
