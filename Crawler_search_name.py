# Get html
import requests
# Crawl and classify
from bs4 import BeautifulSoup
# Regular Expression
import re
# Download img
from urllib.request import urlretrieve
import os


def s_crawler(search_name='', PAGE=1, result={}):
    if(search_name == " " or search_name == ""):    # will get ' ' at first
        return
    url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    for round in range(PAGE):
        # Get .html file.
        res = requests.get(url)
        # 'soup' is equivalent to a factory of html.
        soup = BeautifulSoup(res.text, 'html.parser')
        tag_name = 'div.title a'
        articles = soup.select(tag_name)
        # art['href'] 是要回傳的網址
        for art in articles:
            if(search_name in art.text):
                result.setdefault(art.text, "https://www.ptt.cc/" + art['href'])    # title and link
                print(art.text, art['href'])

        # 上一頁的網址
        tag2_name = 'div.btn-group.btn-group-paging a.btn.wide'
        paging = soup.select(tag2_name)
        # paging[1]的href
        next_url = 'https://www.ptt.cc'+paging[1]['href']

        url = next_url

if __name__ == "__main__":
    PAGE = 1
    search_name = ""
    result = {}
    s_crawler(search_name, PAGE, result)
