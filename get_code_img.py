import requests
from urllib.request import urlretrieve
url = 'http://mathe.neu.edu.cn/code.action'
for i in range(1400):
    img_name = './image/' + str(i) + '.jpg'
    response = requests.get(url)
    print(img_name + '\n')
    with open(img_name, 'wb') as f:
        f.write(response.content)
f.close()