#!/usr/bin/env python
from bs4 import BeautifulSoup
from collections import OrderedDict
from tqdm import tqdm 
import code
import json
import pandas as pd
import re
import requests

home = 'https://vulgate.org/'
home_page = requests.get(home)
soup = BeautifulSoup(home_page.text, 'lxml')
bible = OrderedDict()
strip = lambda s: re.sub(' +', ' ', s.strip()).replace('\n','')
as_ = soup.find('div', {'id':'masterdiv'}).find_all('a')
for a in tqdm(as_):
    chapter_page = requests.get(home+a['href' ])
    soup2 = BeautifulSoup(chapter_page.text, 'lxml')
    spans = soup2.find_all('span', {'class':'Jerome'})
    try:
        bookname, chapter = strip(soup2.find('div', {'class':'BookName'}).text).split(' - ')
    except:
        bookname = soup2.find('div', {'class':'BookName'}).text
        chapter = 'Chapter'
    chapter = re.search(r'Chapter(.*)', chapter).group(1).strip()
    if re.match(r'\d+', chapter):
        chapter = int(chapter)
    for i,span in enumerate(spans):
        stripped = strip(span.text)
        if bookname not in bible:
            bible[bookname] = OrderedDict()
        if chapter not in bible[bookname]:
            bible[bookname][chapter] = []
        bible[bookname][chapter] += [stripped]
json.dump(bible, open('bible.json', 'w'))
