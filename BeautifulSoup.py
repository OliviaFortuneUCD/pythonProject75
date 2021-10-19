from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions'
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.text,"html.parser")
soup.prettify()
#print(soup)

row1 = soup.find('tr')
print(row1)