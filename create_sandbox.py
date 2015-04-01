# -*- coding: utf-8 -*-

#import csv
#import json
from pprint import pprint
from clint import resources
from utils import oauth_login, base_url, bank_id, account_id

resources.init('openbankproject', 'evmakesgeo')
key_file = resources.user.read('config.ini')

print "key file is:"
print key_file

openbank = oauth_login(base_url, key_file)

# Load a json file for sandbox creation.
with open('/Users/simonredfern/Documents/OpenBankProject/DATA/BNPP/OBP-sandbox-bnpp-fr_compact.json') as data_file:
    #data = json.load(data_file)
    data=data_file.read().replace('\n', '')

url = "{}obp/vsandbox/v1.0/data-import".format(base_url)
print 'url is: %s' % url
#print 'data is: %s' % data

headers = {
        'content-type': 'application/json',
        'Accept': 'application/json'
        }

res = openbank.post(url, data=data, headers=headers)
print res.text
