#!/usr/bin/python

import sys
import json

min_price = 2000
big_price = 6000

for line in sys.stdin.readlines():
    data = json.loads(line)
    name = data.pop('name')
    price = float(data.get('price', 1000000) or 1000000)
    good = data['good']
    score = 1000000/price
    if price < min_price:
        continue
    if price > big_price:
        score += 2000
    print score, name.encode('utf-8'), json.dumps(data).encode('utf-8')
