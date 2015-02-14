# -*- coding: utf-8 -*-
import csv

from clint import resources

from utils import oauth_login, base_url, bank_id, account_id

resources.init('openbankproject', 'evmakesgeo')
key_file = resources.user.read('config.ini')

openbank = oauth_login(base_url, key_file)

# Parse cords from csv
reader = csv.reader(open('static/ireland_points.csv'))
firstline = True
csv_data = []
for row in reader:
    if firstline:    #skip first line
        firstline = False
        continue
    csv_data.append((row[0], row[1]))

# Get transactoin ids
response = openbank.get("{}obp/v1.2.1/banks/{}/accounts/{}/owner/transactions".format(base_url, bank_id, account_id))
transactions = [ each['id'] for each in response.json()['transactions']][0:len(csv_data)]


# Create for a list of transactions id geo metadata
for index, transaction in enumerate(transactions):
    url = "{}obp/v1.2.1/banks/{}/accounts/{}/public/transactions/{}/metadata/where".format(base_url, bank_id, account_id, transaction)
    payload = '{"where": { "latitude":' + csv_data[index][1] + '"longitude": ' + csv_data[index][0] + ' } }'
    headers = {'content-type': 'application/json'}
    print ('lalala')
    #res = openbank.post(url, data=payload, headers=headers)
