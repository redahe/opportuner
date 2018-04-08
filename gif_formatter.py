#!/usr/bin/env python

import sys
import json
import os
import urllib
import cStringIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

rank = 0

output_directory = 'tmp'

for line in sys.stdin.readlines():
    rank += 1
    score, name, dat = line.split(' ', 2)
    data = json.loads(dat)
    imgURL = data.pop('img', None)
    price = data.pop('price', '')
    name = unicode(name, "utf-8")
    price = unicode(price, "utf-8")
    fl = cStringIO.StringIO(urllib.urlopen(imgURL).read())
    img = Image.open(fl).convert('RGBA')
    basewidth = 800
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("DejaVuSans.ttf", 16)
    draw.text((10, 10), name, (0, 255, 0, 200), font=fnt)
    draw.text((10, 60), price, (0, 255, 0, 200), font=fnt)
    img.save(fp=output_directory + os.sep + str(rank-1)+'.png', format='png')
