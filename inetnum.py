#!/usr/bin/env python

import argparse
import netaddr
import json
import requests

parser = argparse.ArgumentParser(description='Search RIPE database')
parser.add_argument('search_term', help='Search term used to search the RIPE database. Eg: facebook')
args = parser.parse_args()


# Search the RIPE database
# There is an issue with RIPE. When making a request and including
# the type-filter inetnum, the JSON response also includes other types.
request = requests.get('http://rest.db.ripe.net/search.json', params={
    'query-string': args.search_term,
    'type-filter': 'inetnum'
})

json = json.loads(request.text)

# Filter any object that doesn't have the type 'inetnum'
ranges = [x['primary-key']['attribute'][0]['value'] for x in json['objects']['object'] \
            if x['type'] == 'inetnum']

# Turn the IP range string into CIDR
cidrs = [];
for _range in ranges:
    _range = _range.split(' - ');
    cidrs.append(netaddr.iprange_to_cidrs(_range[0], _range[1]))

# Print the CIDR's
for cidr in cidrs:
    print str(cidr[0])
