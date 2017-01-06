#!/bin/sh

top_ops=25

modules/aviasales_scrape.py | modules/aviasales_range.py  | sort -rnk1  | head -n "$top_ops" | ./formatter.sh
