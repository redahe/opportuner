#!/bin/sh

top_ops=52
echo 'RANK   SCORE          PERFORMER                  DATA'
echo '-----------------------------------------------------------'
modules/concerts_scrape.py | modules/concerts_range.py  | sort -rnk1  | head -n "$top_ops" |\
	awk '{printf "%-6s %-14s %-30s",  NR, $1, $2; $1=""; $2=""; print $0}'

