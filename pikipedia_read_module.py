import requests

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"


PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}


#DATA = R.json()

#LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
"""

PARAMS_1 = {
    "action": "login",
    "igname": "bot_user_name",
    "igpassword": "bot_password",
    "ig_token": LOGIN_TOKEN,
    "format": "json"

}
"""

#R = S.post(URL, data=PARAMS_1)

PARAMS_2 = {
    "action": "parse",
    "page": "API:Revisions",
    "format": "json"

}

R = S.get(url=URL, params=PARAMS_2)
NewResponse = S.get('https://google.com/', params=PARAMS_2)
DATA = R.json()

print(DATA)

