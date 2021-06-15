import requests
import config
import telebot
url = config.URL
login = config.LOGIN
password = config.PASSWORD
s = requests.Session()
r = s.get(url, auth=(login, password))

