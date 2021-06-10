import requests
import config
from pprint import pprint


S = requests.Session()

URL = config.API_ENDPOINT
#URL = 'https://www.mediawiki.org/w/api.php'

PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
pprint(LOGIN_TOKEN)

PARAMS_1 = {
    "action": "query",
    "igname": config.IG_NAME,
    "igpassword": config.IG_PASSWORD,
    "ig_token": LOGIN_TOKEN,
    "format": "json"
}


R = S.post(URL, data=PARAMS_1)
DATA = R.json()
pprint(DATA)

PARAMS_2 = {
    "action": "parse",
    "page": "Welcome_to_ПИК-Проект",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()
pprint(DATA)



