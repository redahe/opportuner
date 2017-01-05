top_ops=15
echo 'RANK   ID        SCORE           DATA'
echo '-------------------------------------'
modules/finance_scrape.py | modules/finance_range.py  | sort -rnk1  | head -n "$top_ops" | awk '{printf "%-6s %-9s %-15s %-50s\n",  NR, $2, $1, $0}'
