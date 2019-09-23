#获取豆瓣网评
from urllib import request
import json
import urllib.request
from bs4 import BeautifulSoup
import requests
url = 'https://movie.douban.com/subject/25890017/reviews?start=20'
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')
review_short = soup.select('.review-short')
for i in range(len(review_short)):
    fp = open('豆瓣影评.txt','a+',encoding='utf-8')
    yingping = ''
    id = review_short[i].get('data-rid')
    newurl = 'https://movie.douban.com/j/review/%s/full'%id
    rsp = request.urlopen(newurl)
    data = rsp.read().decode()
    data = json.loads(data)
    soup = BeautifulSoup(data['body'],'html.parser')
    for i in range(len(soup.select('p'))):
        via = soup.select('p')[i]
        if(len(via) == 0 or via.string is None):
            continue
        print(soup.select('p')[i].string)
        fp.write(soup.select('p')[i].string)
