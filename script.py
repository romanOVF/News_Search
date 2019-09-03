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
    
    html_echo = urlopen("https://echo.msk.ru/")
    bs_obj = bs(html_echo, 'lxml')
    text_news_echo = bs_obj.find('ul', class_ = 'newslist').find_all('h3')
    print('=== ECHO MOSCOW - NEWS ===', end = '')
    get_time()

    for i in text_news_echo:
        print(" ".join(i.text.split()))

    print()

def get_newsru():
    html_newsru = urlopen("https://www.newsru.com/allnews/")
    bs_obj = bs(html_newsru, 'lxml')
    text_news_newsru = bs_obj.find('body').find_all('a', class_ = 'index-news-title')
    time_news_newsru = bs_obj.find('body').find_all('span', class_ = 'index-news-date')
    print('=== NEWSRU.COM - NEWS ===', end = '')
    get_time()

    time_list_newsru = []
    news_list_newsru = []

    for j in time_news_newsru:
        time_list_newsru.append(j.text[13:-47])

    for i in text_news_newsru:
        news_list_newsru.append(i.text[6:-5])

    for k in range(len(time_list_newsru)):
        all_string_news = "".join(time_list_newsru[k].split()) + ' ' + news_list_newsru[k]
        print(all_string_news)

get_news_echo_msk()
get_newsru()