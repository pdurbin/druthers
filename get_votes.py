#!/usr/bin/env python3
import csv
from urllib.request import Request, urlopen
import json
import os
from urllib.parse import urlparse

def main():
    tsv_file = 'boards.tsv'
    final = {}
    bar = {}
    alldata = []
    cache_dir = 'cache'
    with open(tsv_file) as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t")
        rows = [row for row in reader]
        for row in rows:
            datarow = []
            #print(row)
            board = row['Board URL HTML']
            board_json = row['Board URL JSON']
            print(board_json)
            project_id = board_json.split('/')[4]
            print(project_id)
            print(board)
            hostname = row['Installation hostname']
            print(hostname)
            #if board:
            #    print(board)
            #    hostname = row['Installation hostname']
            datarow.append('FIXME')
            datarow.append(board)
            datarow.append(hostname)
            alldata.append(datarow)
            hostname_path = os.path.join(cache_dir, 'installations', hostname)
            if not os.path.exists(hostname_path):
                os.makedirs(hostname_path)
            org = board.split('/')[4]
            foo_path = os.path.join(cache_dir, 'boards', org)
            if not os.path.exists(foo_path):
                os.makedirs(foo_path)
            #org_url = 'https://api.github.com/orgs/' + org + '/projects'
            #print('fetching ' + org_url)
            boards_for_org_out  = '{}'
            #req = Request(org_url)
            #req.add_header('Accept', 'application/vnd.github.inertia-preview+json')
            #response = urlopen(req)
            #boards_for_org_out = get_remote_json(response)
            boards_for_org_filename  = 'boards.json'
            with open(foo_path + os.sep + boards_for_org_filename, 'w') as outfile:
                json.dump(boards_for_org_out, outfile, indent=4)

            # curl -H 'Accept: application/vnd.github.inertia-preview+json' https://api.github.com/projects/2783568/columns
            # {
            #  "message": "Requires authentication",
            #  "message": "Must have admin rights to Repository.",
            #  "documentation_url": "https://developer.github.com/v3/projects/columns/#list-project-columns"
            #}
            columns_url = 'https://api.github.com/projects/' + project_id + '/columns'
            print('fetching ' + columns_url)
            columns_out = '{}'
            req = Request(columns_url)
            req.add_header('Accept', 'application/vnd.github.inertia-preview+json')
            token = ''
            req.add_header('Authorization', 'token ' + token)
            response = urlopen(req)
            columns_out = get_remote_json(response)
            columns = 'columns.json'
            with open(hostname_path + os.sep + columns, 'w') as outfile:
                json.dump(columns_out, outfile, indent=4)
            #break
            #cards_out = '[]'
            #cards = 'cards.json'
            #with open(path + os.sep + cards, 'w') as outfile:
            #    json.dump(cards_out, outfile, indent=4)
            ## FIXME: remove this break

    outfile = open('votes.tsv','w')
    writer=csv.writer(outfile, delimiter='\t')
    writer.writerow(['Issue URL', 'Board URL', 'Installation hostname'])
    #writer.writerows(list_of_rows)
    writer.writerows(alldata)

def get_remote_json(response):
    return json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))

if __name__ == '__main__':
    main()
