import requests

from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
requests.get('https://api.github.com/user', auth=('user', 'pass'))


from requests.auth import HTTPDigestAuth
url = 'https://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))


from requests_oauthlib  import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)


from requests_oauthlib  import OAuth2
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth2('client_id', 'client(Optional Default value = WebApplicationClient)', 'token')
requests.get(url, auth=auth)

