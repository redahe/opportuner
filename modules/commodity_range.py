#!/usr/bin/python

import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


min_price = 2000
big_price = 6000

for line in sys.stdin.readlines():
    data = json.loads(line)
    name = data.pop('name').replace(' ', '_')
    try:
        price = float(data.get('price', 1000000) or 1000000)
    except Exception as e:
        sys.stderr.write(str(e) + '\n')
        sys.stderr.write(data['price'])
        sys.stderr.write('\n')
        price = 1000000
    score = 1000000/price
    if price < min_price:
        score -= 2000
    if price > big_price:
        score += 2000

    print score, name, json.dumps(data)
