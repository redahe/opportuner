#!/bin/sh


echo 'Please wait'

./web_formatter.py > tmp.html 
uzbl tmp.html
rm tmp.html

