import json

from clint import resources
from clint.textui import colored, puts

from requests_oauthlib import OAuth1Session

base_url = 'https://ulsterbank.openbankproject.com/'
bank_id = 'ulster'
account_id = 'charity1'

client_key = "1ks4oso52fbhcurkvtrsjejzkmzwlqb0f2mgfnv3"
client_secret = "2svdaxpdk5qdg0ptjhmp3xmxdfrzen1ouu515xjj"

def oauth_login(base_url, key_file):

    openbank = None

    # Make Oauth
    if not key_file:
        request_token_url = "{}oauth/initiate".format(base_url)
        authorization_base_url = "{}oauth/authorize".format(base_url)
        access_token_url = "{}oauth/token".format(base_url)

        openbank = OAuth1Session(
            client_key,
            client_secret=client_secret,
            callback_uri='http://127.0.0.1/cb'
        )

        openbank.fetch_request_token(request_token_url)

        authorization_url = openbank.authorization_url(authorization_base_url)

        puts(colored.blue('Please go here and authorize:'))
        puts(colored.green(authorization_url))
        puts()

        redirect_response = input('Paste the full redirect URL here:')
        openbank.parse_authorization_response(redirect_response)
        oauth_tokens = openbank.fetch_access_token(access_token_url)
        resources.user.write('config.ini', json.dumps(oauth_tokens))
    else:
        keys = json.loads(key_file)
        openbank = OAuth1Session(
            client_key,
            client_secret=client_secret,
            resource_owner_key=keys.get('oauth_token'),
            resource_owner_secret=keys.get('oauth_token_secret')
        )

    puts(colored.yellow("Login Done"))

    return openbank