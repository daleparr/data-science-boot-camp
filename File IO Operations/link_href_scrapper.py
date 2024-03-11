"""
#scrapping table data
import requests
from bs4 import BeautifulSoup

base_url = "https://structuresoflegacy.substack.com/"

responce = requests.get(base_url)
soup = BeautifulSoup(responce.text, "html.parser")

rows = soup.select("tbody > tr")
print(rows[0])


#scrapping links from a site
import requests
from bs4 import BeautifulSoup

base_url = "https://www.pinko.com/en-gb/"

responce = requests.get(base_url)
soup = BeautifulSoup(responce.text, "html.parser")

for item in soup.find_all("a"):
    print(item.get("href"))

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.pinko.com/en-gb/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


r = requests.get(f"https://www.pinko.com/en-gb/clothing/")

soup = BeautifulSoup(r.content, "html.parser")

product_list = soup.find_all('div', class_ = "col-6")

# for loop to extract all links on a page and place in a list
product_links = []   

for item in product_list:
            for link in item.find_all("a", href=True):
                product_links.append(base_url + link["href"])

#print(len(product_links))

#test_link = "https://www.pinko.com/en-gb/double-breasted-full-milano-blazer-100154A15MZ99.html"

for link in product_links:
    r1 = requests.get(link, headers=headers)

    soup = BeautifulSoup(r1.content, "html.parser")

    product_name = (soup.find("h1", class_= "h3").text.strip())
    description_care = (soup.find('div', class_ = "product-detail__description").text.strip())
    price = (soup.find('span', class_ = "sales__value"))

    pinko = {
            'Name': product_name,
            'Description': description_care,
            'Product Price': price
            }

    print("Saving ", pinko['Name'])
    
df = pd.DataFrame(pinko)
print(df.head)
