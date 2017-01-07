#!/usr/bin/python

import urllib2
import re
import json

for page in xrange(5):
    request_url = 'http://www.concert.ru/Actions.aspx?ActionTypeID=1&GenreTypeID=2&page={}'.format(page)
    pattern = re.compile('<time .*?>(.*?)</time>.*?<div itemprop="name">(.*?)</div>', re.DOTALL)
    response = urllib2.urlopen(request_url).read()
    lst = pattern.findall(response)
    for t in lst:
        result = {'name': t[1], 'time': t[0].strip()}
        print json.dumps(result).encode('utf-8')
