import requests
import re
import base64

# 学生账户信息
user_file = open("D:/user_info/user.txt", 'r')
stuId = user_file.read()
pwd_file = open("D:/user_info/pwd.txt", 'r')
stuPass = pwd_file.read()
for i in range(5):
    stuId = base64.b64decode(stuId)
    stuPass = base64.b64decode(stuPass)
stuId = str(stuId, 'utf-8')
stuPass = str(stuPass, 'utf-8')
# 构造表单数据的网页
index_url = 'https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D3'
page = requests.get(index_url)
page_text = page.text
lt = re.findall(r'id="lt".*?value="(.*?)"', page_text)[0]
execution = re.findall(r'name="execution" value="(.*?)"', page_text)[0]
_eventId = 'submit'
ul = len(stuId)
pl = len(stuPass)
rsa = stuId + stuPass + lt
# 需要提交的数据
post_data = {
    'rsa': rsa,
    'ul': ul,
    'pl': pl,
    'lt': lt,
    'execution': execution,
    '_eventId': _eventId

}
# 模拟登录后的界面
login_page = requests.post(index_url, data=post_data, cookies=page.cookies)
print(login_page.text)
# 因为自己用，就懒得检查是否真的登录成功了
print("登录成功")
