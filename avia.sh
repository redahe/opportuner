#!/bin/sh

top_ops=25

cat modules/aviasales_dest | modules/aviasales_scrape.py | modules/aviasales_range.py  | sort -rnk1  | head -n "$top_ops" | ./show_in_browser.sh
