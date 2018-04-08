#!/bin/bash

ffmpeg -loop 1 -f image2 -r 1 -i tmp/%d.png -i tmp/sun.mp3 -r 50 -b:v 5M -t 42.5 video.mpg 
