#!/usr/bin/python

import urllib2
import json
import sys
import datetime

origin = 'MOW'

destinations = {}
for l in sys.stdin.readlines():
    dst, name = l.split(' ', 1)
    destinations[dst] = name


period = (datetime.date.today()+datetime.timedelta(20)).strftime("%Y-%m-%d")

request_url = 'https://map.aviasales.ru/prices.json?origin_iata={}&period={}:season&one_way=false&price=500000&no_visa=true&schengen=true&\
need_visa=true&locale=ru&min_trip_duration_in_days=10\
&max_trip_duration_in_days=15'.format(origin, period)


response = urllib2.urlopen(request_url).read()
data = json.loads(response)
# sys.stderr.write(str(data))

for t in data:
    result = {}
    if not t['actual']:
        continue
    dst = t.pop('destination')
    if dst not in destinations:
        continue
    result['DST'] = destinations[dst].strip().replace(' ', '_')
    result['price'] = t['value']
    result['ttl'] = t['ttl']
    result['ret_date'] = t['return_date']
    result['depart_date'] = t['depart_date']
    result['changes'] = t['number_of_changes']
    result['class'] = t['trip_class']
    print json.dumps(result)
