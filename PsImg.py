import requests
from urllib import request
import json
import urllib.request
for i in range(20):
    url = 'http://www.51sjsj.com/home/Contest/ajaxWorks.html?p=%d&size=16&works_type=3&rank=0'%i
    rsp = request.urlopen(url)
    data = rsp.read().decode()
    data = json.loads(data)
    data = data['list']
    for item in data:
        id = item['id']
        newurl = 'http://www.51sjsj.com/home/contest/getWorks.html?id='
        newurl = newurl + str(id)
        response = request.urlopen(newurl)
        newdata = response.read().decode()
        newdata = json.loads(newdata)
        img = newdata['pic'][0]
        path = 'D:\PythonProject\PsImg' + '\\' + item['title'] + '.jpg'
        urllib.request.urlretrieve(img,path)
