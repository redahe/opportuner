#!/usr/bin/python

import sys
import json

colors = ['#CECECE', '#E2E2E2']

print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<style>\n* {\n font-size: 90%;\n font-family: Arial;}'
print '</style>'
print '</head>'
print '<body>'
print '<table border="1">'

rank = 0
for line in sys.stdin.readlines():
    rank += 1
    score, name, dat = line.split(' ', 2)
    data = json.loads(dat)

    print '<tr bgcolor="' + colors[rank % 2] + '">'
    print '<td width="5%"> ' + str(rank) + '</td>'
    link = data.pop('link', None)
    img = data.pop('img', None)
    if link or img:
        print '<td width="25%">'
        print '<a href="' + link + '">' if link else ''
        print '<img src="' + img + '"/>' if img else ''
        print '</a>' if link else ''
        print '</td>'
    print '<td width="25%">' + name.replace('_', ' ') + '</td>'
    price = data.pop('price', '')
    print '<td>' + str(price) + '</td>'
    if data:
        print '<td>'
        for k, v in data.iteritems():
            print '<p>' + str(k) + ': ' + str(v) + '</p>'
        print '</td>'
    print '<td width="15%">' + str(score) + '</td>'
    print '</tr>'

print '</table>'
print '</body>'
print '</html>'
