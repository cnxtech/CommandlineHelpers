# -*- coding: utf-8 -*-

# TODO: add secret key to url (or POST?)
# also look at invalid signature error message (oauth) or if that is part of missing secret key
# (scala obp importer has it working)

#import json
from clint import resources
from utils import oauth_login, base_url

resources.init('openbankproject', 'evmakesgeo')
key_file = resources.user.read('config.ini')

# key file in a place like: /Users/simonredfern/Library/Application\ Support/evmakesgeo/config.ini

print "key file is: %s" % key_file

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
