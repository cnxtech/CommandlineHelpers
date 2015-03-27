# -*- coding: utf-8 -*-

from clint import resources

from utils import oauth_login, base_url, bank_id, account_id

resources.init('openbankproject', 'evmakesgeo')
key_file = resources.user.read('config.ini')

print "key file is:"
print key_file

openbank = oauth_login(base_url, key_file)

#  Check root

url = "{}obp/v1.2.1".format(base_url)
print "url is: %s" % url
response = openbank.get(url)
print "response is:"
print response.json()
