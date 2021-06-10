import requests
import config
url = config.URL
login = config.LOGIN
password = config.PASSWORD
s = requests.Session()
r = s.get(url, auth=(login, password))
