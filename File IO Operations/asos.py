import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.asos.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


r = requests.get(f"https://www.asos.com/men/new-in/cat/?cid=27110")

soup = BeautifulSoup(r.content, "html.parser")

product_list = soup.find_all('a', class_ = "href")

print(product_list)
