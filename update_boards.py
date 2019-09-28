#!/usr/bin/env python3
import csv
import urllib.request as urlrequest
import json
from urllib.parse import urlparse
tsv_file = 'crowdsourced.tsv'
alldata = []
with open(tsv_file) as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter="\t")
    rows = [row for row in reader]
    for row in rows:
        datarow = []
        #print(row)
        hostname = row['Installation hostname']
        country = row['Country']
        continent = row['Continent']
        gdcc_member = row['GDCC member']
        board_html = row['Project board under IQSS']
        board_json = row['Project board API URL']
        if board_html and board_json:
            #print(board)
            hostname = row['Installation hostname']
            datarow.append(board_html)
            datarow.append(board_json)
            datarow.append(hostname)
            alldata.append(datarow)
        doi_authority = row['DOI authority']

outfile = open('./boards.tsv','w')
writer=csv.writer(outfile, delimiter='\t')
writer.writerow(['Board URL HTML', 'Board URL JSON', 'Installation hostname'])
writer.writerows(alldata)
