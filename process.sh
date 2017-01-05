#!/bin/sh

top_ops=15
echo 'RANK   ID        SCORE           DATA'
echo '-------------------------------------'
modules/finance_scrape.py | modules/finance_range.py  | sort -rnk1  | head -n "$top_ops" |\
       	awk '{printf "%-6s %-9s %-15s",  NR, $2, $1; $1=""; $2=""; print $0}'
