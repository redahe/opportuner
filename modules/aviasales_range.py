#!/usr/bin/python

import sys
import json

for line in sys.stdin.readlines():
    data = json.loads(line)
    dest = data.pop('DST')
    price = float(data['price'] or 1000000)
    changes = int(data['changes'] or 0)
    clazz = int(data['class'] or 0)

    score = (10000.0/price)*(1+clazz*0.5)/(1+changes*0.3)
    print score, dest, json.dumps(data)
