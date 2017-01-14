#!/bin/sh

top_ops=80

echo 'Please wait'

modules/commodity_scrape.py | modules/commodity_range.py  | sort -rnk1  | head -n "$top_ops" | ./show_in_browser.sh

 # awk '{printf "%-6s %-15s",  NR, $2, $1=""; $2=""; print $0}'
