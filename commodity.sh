#!/bin/sh

top_ops=50
echo 'RANK   ID                   DATA'
echo '-------------------------------------'

modules/commodity_scrape.py | modules/commodity_range.py  | sort -rnk1  | head -n "$top_ops" |\
awk '{printf "%-6s %-15s",  NR, $2, $1=""; $2=""; print $0}'
