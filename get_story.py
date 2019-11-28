from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.duoben.net/book/11893/4101850.html')
s = browser.find_element_by_class_name('content')
print(s.text)
# import requests
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Cookie': 'UM_distinctid=16e159d6d0e356-0a9225d89f589f-7711439-144000-16e159d6d0f9c2; bcolor=; font=; size=; fontcolor=; width=; CNZZDATA1277893032=374020380-1572353443-https%253A%252F%252Fwww.duoben.net%252F%7C1572353443; CNZZDATA1277893031=1052963982-1572318493-https%253A%252F%252Fwww.baidu.com%252F%7C1572352899',
#     'Host': 'www.duoben.net',
#     'Referer': 'https://www.duoben.net/book/11893/27252448.html',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
# }
# url = 'https://www.duoben.net/book/11893/27289596.html'
# response = requests.get(url, headers=headers)
# print(response.text)
