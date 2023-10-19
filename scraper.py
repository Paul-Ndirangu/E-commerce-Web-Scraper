import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

page = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')


soup = BeautifulSoup(page.content,'html.parser')

results = soup.find_all('div', attrs= {'class': 'product-grid__item'})

for element in results:
    print(element, end="\n"*2)