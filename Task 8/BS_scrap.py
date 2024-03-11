import requests
from bs4 import BeautifulSoup

base_url = "https://www.pinko.com/en-gb/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

r = requests.get("https://www.pinko.com/en-gb/sale/")

soup = BeautifulSoup(r.content, "html.parser")

product_list = soup.find_all("div", class_ ="col=12")

#product_links = []

#for item in product_links:
    #for link in item.find_all("a", href=True):
        #print(link["href"])


print(product_list)