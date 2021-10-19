#https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
from bs4 import BeautifulSoup
import requests
import pandas as pd

import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
print(soup.find_all('p'))