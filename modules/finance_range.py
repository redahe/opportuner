#!/usr/bin/python

import sys
import json

for line in sys.stdin.readlines():
    data = json.loads(line)
    symbol = data.pop('SYMBOL')
    try:
        pe = float(data['PE'] or 1000)
    except:
        pe = 1000
    try:
        dy = float(data['DY'] or 0)
    except:
        dy = 0

    score = 1.0/(pe)*10 + dy
    data['PE'] = pe
    data['DY'] = dy
    print score, symbol, json.dumps(data)
