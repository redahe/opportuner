#!/bin/sh

top_ops=100
modules/concerts_scrape.py | modules/concerts_range.py  | sort -rnk1  | head -n "$top_ops" | ./show_in_browser.sh
	# awk '{printf "%-6s %-14s %-30s",  NR, $1, $2; $1=""; $2=""; print $0}'

