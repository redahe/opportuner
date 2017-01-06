#!/bin/sh


echo 'RANK   ID        SCORE           DATA'
echo '-------------------------------------'
awk '{printf "%-6s %-9s %-15s",  NR, $2, $1; $1=""; $2=""; print $0}'
