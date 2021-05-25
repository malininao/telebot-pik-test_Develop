import requests
import pprint


S = requests.Session()

#URL = "https://pikipedia.pik.ru/api.php"
URL = 'https://www.mediawiki.org/w/api.php'

PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(URL, params=PARAMS_0)
print(R)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
print(LOGIN_TOKEN)

PARAMS_1 = {
    "action": "login",
    "igname": "Malininao@OSIPIA",
    "igpassword": "t2p7a0o4rhijjptu75ch84ionsioms02",
    "ig_token": LOGIN_TOKEN,
    "format": "json"

}


R = S.post(URL, data=PARAMS_1)
DATA = R.json()
print(DATA)

PARAMS_2 = {
    "action": "parse",
    "page": "API:Tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()
print(DATA)


#
NewResponse = S.get('https://google.com/', params=PARAMS_2)
#DATA = NewResponse.json()

#print(DATA)

