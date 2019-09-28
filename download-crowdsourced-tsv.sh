#!/bin/sh
ID=''
GID=''
FORMAT='tsv'
curl -s "https://docs.google.com/spreadsheets/d/$ID/export?gid=$GID&format=$FORMAT" > crowdsourced.tsv
