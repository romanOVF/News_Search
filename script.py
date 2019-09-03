# Created mon 02 sep 2019
# clear && python3 script.py

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re, time

def get_time():
    date_time = time.ctime(time.time())
    time_string = '{} {}'.format(' ', date_time)
    print(time_string)

def get_news_echo_msk():
    
    html = urlopen("https://echo.msk.ru/")
    bs_obj = bs(html, 'lxml')
    time_news = bs_obj.find('div', class_ = 'newspreview').find_all('span', class_ = 'datetime')
    text_news = bs_obj.find('ul', class_ = 'newslist').find_all('h3')
    print('=== ECHO MOSCOW - NEWS ===', end = '')
    get_time()

    for i in text_news:
        print(" ".join(i.text.split()))

    print()

def get_newsru():
    html = urlopen("https://www.newsru.com/allnews/")
    bs_obj = bs(html, 'lxml')
    texts = bs_obj.find('body').find_all('a', class_ = 'index-news-title')
    time_news = bs_obj.find('body').find_all('span', class_ = 'index-news-date')
    print('=== NEWSRU.COM - NEWS ===', end = '')
    get_time()

    time_list = []
    news_list = []

    for j in time_news:
        time_list.append(j.text[13:-47])

    for i in texts:
        news_list.append(i.text[6:-5])

    for k in range(len(time_list)):
        all_string_news = "".join(time_list[k].split()) + ' ' + news_list[k]
        print(all_string_news)

get_news_echo_msk()
get_newsru()