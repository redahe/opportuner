#!/bin/sh

top_ops=180


cat modules/commodity_dest | modules/commodity_scrape.py | modules/commodity_range.py  | sort -rnk1  | head -n "$top_ops" | ./show_in_browser.sh

 # awk '{printf "%-6s %-15s",  NR, $2, $1=""; $2=""; print $0}'
