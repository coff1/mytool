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
    urls.append(i+'a/login')

for i in urls:
    try:
        header = {
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        x = requests.post(i,timeout=0.5,headers=header,data="username=admin&&password=123456",allow_redirects=False)
        if x.status_code == 302 and "rememberMe=deleteMe" in str(x.headers):
            print(i)
            # print(x.headers)
    except BaseException:
        continue
