#!/bin/sh

top_ops=25

modules/finance_scrape.py | modules/finance_range.py  | sort -rnk1  | head -n "$top_ops" | ./show_in_browser.sh
