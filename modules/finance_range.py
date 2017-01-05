#!/usr/bin/python

import sys
import json

for line in sys.stdin.readlines():
    data = json.loads(line)
    symbol = data.pop('SYMBOL')
    pe = float(data['PE'] or 1000)
    pb = float(data['PB'] or 1000)
    ps = float(data['PS'] or 1000)
    dy = float(data['DY'] or 0)

    score = 1.0/(pe)*10 + 1.0/pb*4 + 1.0/ps*4 + dy
    print score, symbol, json.dumps(data)
