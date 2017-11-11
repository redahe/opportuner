#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
import json
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger('commodity_scrape.py')

goods = []

for l in sys.stdin.readlines():
    goods.append(l.strip())

pattern = re.compile('(<div class="b-photo">.*?img src="(.*?)".*?)?<h3 class="title item-description-title"> <a class="item-description-title-link".*?href="(.*?)".*?">(.*?)</a>.*?about">(.*?)</div>', re.DOTALL)

for good in goods:
    logger.info(str(good))
    request_url = 'https://www.avito.ru/moskva?q='+good.replace(' ', '+')
    try:
        response = urllib2.urlopen(request_url).read().decode('utf-8')
    except Exception as e:
        logger.error(str(e) + ' on ' + good)
        continue
    lst = pattern.findall(response)
    for item in lst:
        link = 'https://www.avito.ru' + item[2].strip().encode('utf-8')
        name = item[3].strip()
        img = 'https:' + item[1].strip()
        price = item[4].strip().replace(' ', '')
        r = price.find('р')
        if r != -1:
            price = price[:r]
        res = {'name': name, 'price': price, 'link': link, 'img': img,
               'good': good.replace(' ', '_')}
        print json.dumps(res, ensure_ascii=False).encode('utf-8')
