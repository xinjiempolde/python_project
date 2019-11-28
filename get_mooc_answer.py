import requests

url = 'https://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getHomeworkPaperDto.dwr'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'content-type': 'text/plain',
    'cookie': 'EDUWEBDEVICE=bce0e07695934b5195d8260de9c11999; MOOC_PRIVACY_INFO_APPROVED=true; bpmns=1; WM_TID=lrbropfxA0tBBUUAVUNorBW1VtGwpvLx; __utmz=63145271.1572160986.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); P_INFO=18228258627|1572161009|1|imooc|00&99|null&null&null#lin&210100#10#0|&0|null|18228258627; WM_NI=hXYpk6UrlwUs3J3nTf%2FWTLWc4UxGFnVQS5LKBD55maKxbDtAo3qycgsewX464EUCycOYX0g8RFOn8s99wiMS4qwB69IEmOEtLtt%2F0S9gtuOPoFEdGUV21xdpW%2BPVVQPAN3g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2bb6db0b6a5d1ef4fb5e78ba6d84e939a9baaf33d8e8ef885f23af1ea99b0e82af0fea7c3b92aac889791ea3e97aea498d879f196fd8fd76eed899cadd669f88bb8a8c566968f9dd6cf41829cfbd6f06b89a8aea5f74badedbf9ae26db1bbb9b9b73ef89b9ba4fc698d8798d1e634929a818fbb79fbe7b98ad059f8afb9a3b5338b9ba3b0c88090acbcd0b359fbb9bc96ce5cad9a8b85c65f96eeff99e77c95f5a0b7d55b949f82d4e637e2a3; NTESSTUDYSI=e72d6a129df44c8187a0f87f72aab156; STUDY_INFO="yd.109f410f995642d89@163.com|8|1035979024|1574246310858"; STUDY_SESS="uQhAJs3mZYpRRl3HnsHpOQKqy27BztxSi3UaNTxSML1XrkbSxd2Nqc0jJ3o5/6wyvVksWBZaC42dXx0A0WsmhDRu55qB1qukD1qaVCG+E86XzUu7wosIiedSiU5xYZziPwROpSvIcVb+4ZLhJ19JKUr4sYMexnYM6AEZRQ1E9/YLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="W70NtuPsv3QAeLyXjb8NtwlAZA+VZmYk7JyFDYrJSCXRPGQoUWmWW1eMUVjDwmKs5GrmlhUPT67kLCVsI3t1K+iEURWUCqgNCnPKsuYq0mRuC2HNTpfOppIQKUeCf+Qjl5oXF0DZtOKDfcCBtMmnGTCn2nA/nFoXnfuH4DEzkhvl+cBGowGJf0X25yaa7ofY3+Ng5AIlNG9GIIxL21jdoAsWZ5noExNXpZGouYUSWynZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1035979024#|#1516418522396; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1572336090,1574042521,1574212132,1574246314; __utma=63145271.1341410490.1572160986.1574212133.1574246314.9; __utmc=63145271; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1574246325; __utmb=63145271.6.9.1574246322563'
}
post_data = {
    'callCount': '1',
    'scriptSessionId ': '${scriptSessionId}190',
    'httpSessionId': 'e72d6a129df44c8187a0f87f72aab156',
    'c0-scriptName': 'MocQuizBean',
    'c0-methodName': 'getHomeworkPaperDto',
    'c0-id': '0',
    'c0-param0': 'string:1219197310',
    'c0-param1': 'null:null',
    'c0-param2': 'boolean:true',
    'c0-param3': 'number:3',
    'c0-param4': 'number:1401140248',
    'batchId': '1574246527457'
}
response = requests.post(url, headers=header, data=post_data)
print(response.text)
# import requests
#
# url = 'https://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getHomeworkInfo.dwr'
# header = {
#     'content-type': 'text/javascript;charset=UTF-8'
# }
# post_data = {
#     'callCount': '1',
#     'scriptSessionId': '\$\{scriptSessionId\}190',
#     'httpSessionId': '8c540841fe9342d999a3923871d0c580',
#     'c0-scriptName': 'MocQuizBean',
#     'c0-methodName': 'getHomeworkInfo',
#     'c0-id': '0',
#     'c0-param0': 'string:1004125032',
#     'c0-param1': 'null:null',
#     'c0-param2': 'boolean:false',
#     'batchId': '1572103063638',
# }
# response = requests.post(url, data=post_data, headers=header)
# print(response.text)
