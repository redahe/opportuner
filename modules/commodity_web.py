#!/usr/bin/python

import sys
import json

print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '</head>'
print '<body>'
print '<table border="1">'

rank = 0
for line in sys.stdin.readlines():
    rank += 1
    score, name, dat = line.split(' ', 2)
    data = json.loads(dat)

    print '<tr>'
    print '<td width="5%"> ' + str(rank) + '</td>'
    print '<td width="25%"><a href="' + data['link'] + '"><img src="' + data['img'] + '"/></a></td>'
    print '<td width="35%">' + name.replace('_', ' ') + '</td>'
    print '<td width="20%">' + data['price'] + 'rub. </td>'
    print '<td width="15%">' + score + '</td>'
    print '</tr>'

print '</table>'
print '</body>'
print '</html>'
