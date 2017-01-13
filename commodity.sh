#!/bin/sh

top_ops=80
echo 'RANK   ID                   DATA'
echo '-------------------------------------'

modules/commodity_scrape.py | modules/commodity_range.py  | sort -rnk1  | head -n "$top_ops" |\
	modules/commodity_web.py > tmp.html 
uzbl tmp.html
rm tmp.html
# w3m -T text/html
 # awk '{printf "%-6s %-15s",  NR, $2, $1=""; $2=""; print $0}'
