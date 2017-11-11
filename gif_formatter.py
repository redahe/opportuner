#!/usr/bin/env python

import sys
import json
import urllib
import cStringIO
from PIL import Image

rank = 0
frames = []

for line in sys.stdin.readlines():
    rank += 1
    score, name, dat = line.split(' ', 2)
    data = json.loads(dat)
    imgURL = data.pop('img', None)
    price = data.pop('price', '')

    fl = cStringIO.StringIO(urllib.urlopen(imgURL).read())
    img = Image.open(fl).convert('RGBA')
    print(img.size)
    print(img)
    frames.append(img)

frames[0].save(fp='out.gif', format='gif', save_all=True, duration=800, append_images=frames[1:])
# writeGif('out.gif', frames)
print("Done")
