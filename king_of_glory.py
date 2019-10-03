import json
import requests
import urllib.request
hero_list_url = 'http://pvp.qq.com/web201605/js/herolist.json'
hero_list_page = requests.get(hero_list_url).text
my_json = json.loads(hero_list_page)
# json.loads将字符串转为字典， json.dumps将字典转为字符串
for i in range(len(my_json)):
    hero_id = my_json[i]['ename']
    hero_name = my_json[i]['cname']
    hero_img_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/' \
                   + str(hero_id) + '/' + str(hero_id) + '.jpg'
    urllib.request.urlretrieve(hero_img_url,hero_name + '.jpg')
