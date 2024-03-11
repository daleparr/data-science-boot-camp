import requests
from bs4 import BeautifulSoup

base_url = "https://www.farfetch.com/uk/"

responce = requests.get(base_url)

print("Your guide to shopping and placing orders" in responce.text)