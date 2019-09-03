# Created mon 02 sep 2019
# clear && python3 script.py

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html = urlopen("https://echo.msk.ru/")
bs_obj = bs(html, 'lxml')

texts = bs_obj.find('ul', class_ = 'newslist').find_all('h3')

for i in texts:
    print(i.text)
