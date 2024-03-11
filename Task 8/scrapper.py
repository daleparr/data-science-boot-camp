"""

import requests
from bs4 import BeautifulSoup

base_url = "https://structuresoflegacy.substack.com/"

responce = requests.get(base_url)
soup = BeautifulSoup(responce.text, "html.parser")

rows = soup.select("tbody > tr")
print(rows[0])

"""

import requests
from bs4 import BeautifulSoup

base_url = "https://www.pinko.com/en-gb/"

responce = requests.get(base_url)
soup = BeautifulSoup(responce.text, "html.parser")

for item in soup.find_all("a"):
    print(item.get("href"))