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
    urls.append(i+'login.cgi')

for i in urls:
    try:
        x = requests.post(i,timeout=0.5,data="user=admin&password=123")
        if "window.open('/login.html?flag=0','_self')" not in x.text:
            print(i)
            print(x.text)
    except BaseException:
        continue
