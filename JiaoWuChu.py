#!/usr/bin/python
#coding:utf-8
import requests
from bs4 import BeautifulSoup
import http.cookiejar
import re
import json
url = 'https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2F219.216.96.4%2Feams%2FhomeExt.action'
newurl = 'http://219.216.96.4/eams/courseTableForStd!courseTable.action'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '98',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'pass.neu.edu.cn',
    'Referer': 'http://219.216.96.4/eams/localLogin!tip.action',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
newheaders = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '86',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'semester.id=30; JSESSIONID=E48C7C11DEA7BCF447D5CC12E9103A62; SERVERNAME=xk3; GSESSIONID=E48C7C11DEA7BCF447D5CC12E9103A62',
    'Host': '219.216.96.4',
    'Origin': 'http://219.216.96.4',
    'Referer': 'http://219.216.96.4/eams/courseTableForStd.action',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
#该data为登陆页面提交的表单数据
data = {
    'rsa': '20184569218112LT - 19358 - hXIPDxqadpN3q7zOOg3Vxtgz0RBi2Q - tpass',
    'ul': '8',
    'pl': '6',
    'lt': 'LT - 19358 - hXIPDxqadpN3q7zOOg3Vxtgz0RBi2Q - tpass',    'execution': 'e22s3',
    '_eventId': 'submit'
}
#newdata是课表界面提交的表单数据
newdata = {
    'ignoreHead': '1',
    'showPrintAndExport': '1',
    'setting.kind': 'std',
    'startWeek': '',
    'semester.id': '30',
    'ids': '48340'
}
#提交表单，并将Cookie保存到Mycookie.txt文件中
def SaveCookie():
    session = requests.Session()
    session.cookies = http.cookiejar.LWPCookieJar("Mycookie.txt")
    SourceHtml = requests.get(url=url);
    soup = BeautifulSoup(SourceHtml.content.decode("utf-8"), "html.parser")
    data['rsa'] = '20184569218112' + soup.select('#lt')[0].get('value')
    data['lt'] = soup.select('#lt')[0].get('value')
    data['execution'] = soup.select('[name=execution]')[0].get('value')
    session.post(url, data=data, headers=headers)
    session.cookies.save(ignore_discard=True, ignore_expires=True)
    print()
#带着Cookie进行登陆
def LoginWithCookie():
    session = requests.Session()
    session.cookies = http.cookiejar.LWPCookieJar("Mycookie.txt")
    session.cookies.load('Mycookie.txt', ignore_discard=True, ignore_expires=True)
    content = session.post(newurl,data=newdata,headers=newheaders)
    ContentHtml = content.content.decode('utf-8');
    fp = open('CourseTableHtml.html','w')
    fp.write(ContentHtml)
    print(content.text)
#整理获取的HTML中的数据
def TideDate():
    fp = open("CourseTableHtml.html",'r')
    OriginData = fp.read()
    rule = r'var teacher([\w\W]+?)activity;'
    patter = re.compile(rule)
    TeacherDate = patter.findall(OriginData,re.I|re.S|re.M)
    Task = [None for i in range(len(TeacherDate))]
    OneDate = {'course':'','room':'','week':'','col':'','row':''}
    for j in range(len(Task)):
        Task[j] = dict(OneDate)
    for i in range(len(TeacherDate)):
        CourseRule = r'(?<=\")[\u4e00-\u9fa5_a-zA-Z(①-⑦)㈠-㈦]{1,}(?=\()'
        CoursePatter = re.compile(CourseRule)
        Course = CoursePatter.findall(TeacherDate[i])
        Task[i]['course'] = Course[0]
        RoomRule = r'(?<=\")[\u4e00-\u9fa50-9A-Z()（）]{1,}(?=\(浑南校区)|(?<=\")[\u4e00-\u9fa50-9A-Z()（）]{1,}(?=\(南湖校区)'
        RoomPatter = re.compile(RoomRule)
        Room = RoomPatter.findall(TeacherDate[i])
        WeekRule = r'(?<=\")[\d]{40,}(?=\")'
        WeekPatter = re.compile(WeekRule)
        Week = WeekPatter.findall(TeacherDate[i])
        Task[i]['week'] = Week[0]
        if(len(Room) == 0):
            Room.append("无")
        Task[i]['room'] = Room[0]
        colRule = r'(?<=\=)[0-7]{1}(?=\*unitCount\+)'
        colPatter = re.compile(colRule)
        col = colPatter.findall(TeacherDate[i])
        Task[i]['col'] = col[0];
        rowRule = r'(?<=\+)[\d]{1,}(?=;)'
        rowPatter = re.compile(rowRule)
        row = rowPatter.findall(TeacherDate[i])
        Task[i]['row'] = row[0];
    print(Task)
    jsonobj = json.dumps(Task,ensure_ascii=False)
    jsonfile = open('jsonfile.json','w')
    jsonfile.write(jsonobj)
    jsonfile.close()
if __name__ == "__main__":
    SaveCookie()
    LoginWithCookie()
    TideDate()
