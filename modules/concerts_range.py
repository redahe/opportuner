#!/usr/bin/python

import sys
import re
import json

ln = 0
pattern = re.compile('.*[A-Z|a-z]+.*')

for line in sys.stdin.readlines():
    ln += 1
    data = json.loads(line)
    name = data.pop('name')
    name = name.replace(' ', '_')
    score = (100 - ln)
    if pattern.match(name):
        score += 15
    print score, name.encode('utf-8'), json.dumps(data, ensure_ascii=False).encode('utf-8')
