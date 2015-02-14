# -*- coding: utf-8 -*-
import csv

from clint import resources

from utils import oauth_login, base_url, bank_id, account_id

resources.init('openbankproject', 'evmakesgeo')
key_file = resources.user.read('config.ini')

openbank = oauth_login(base_url, key_file)

# Get transactions ids
response = openbank.get("{}obp/v1.3.0/banks/{}/accounts/{}/owner/transactions".format(base_url, bank_id, account_id))
#print "{}obp/v1.2.1/banks/{}/accounts/{}/owner/transactions".format(base_url, bank_id, account_id)
transactions = [ each['id'] for each in response.json()['transactions']]

print transactions



# Get transfer

#/banks/BANK_ID/accounts/ACCOUNT_ID/

print "transfer methods"

response = openbank.get("{}obp/v1.3.0/banks/{}/accounts/{}/transfer-methods".format(base_url, bank_id, account_id))
#print "{}obp/v1.2.1/banks/{}/accounts/{}/owner/transactions".format(base_url, bank_id, account_id)
#methods = [ each['id'] for each in response.json()['transfer-methods']]


print response.json()








# 1.3.0
url = "{}obp/v1.3.0/banks/{}/accounts/{}/owner/transactions".format(base_url, bank_id, account_id)

bank_id = 'ulster'
other_account_id = "personal5"
amount = 100

payload = '{"account_id" : "' + other_account_id + '", "bank_id": "' + bank_id + '", "amount": "' + str(amount) + '"}'


print 'url is: %s' % url
print 'payload is: %s' % payload


headers = {'content-type': 'application/json'}
print ('before post')

res = openbank.post(url, data=payload, headers=headers)

print res
