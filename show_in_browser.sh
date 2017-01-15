#!/bin/sh

echo 'Please wait'

tmp_file=`mktemp /tmp/opportuner_XXXXX.html`

./web_formatter.py > $tmp_file
uzbl $tmp_file
rm $tmp_file

