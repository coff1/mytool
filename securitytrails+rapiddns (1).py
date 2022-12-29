import requests
import json
import sys
import requests
from bs4 import BeautifulSoup
import sys
subdomain=list()

file=sys.argv[1]

def test(name):
    #爬取securitytrails.com的信息
    url='https://api.securitytrails.com/v1/domain/'+name+'/subdomains'

    kw = {'children_only':'false','include_inactive':'true'}

    headers = {"APIKEY": "9MuSQfXJbNwZcfKkIG52mRvp84CfEQSt","Accept":"application/json"}
    
    x=requests.get(url,params = kw, headers= headers)

    dict = json.loads(x.text)

    for i in dict['subdomains'] :
        i=i+'.'+name
        if name+'.' not in i:
            subdomain.append(i)

    #爬取rapiddns.io的信息
    url = 'https://rapiddns.io/subdomain/' + name + '?full=1'

    x=requests.get(url)
    x.close()

    pagesoup = BeautifulSoup(x.text,'lxml')
    for i in pagesoup.text.split('\n'):
        if name in i and 'RapidDNS' not in i and name+'.' not in i:
            subdomain.append(i)

    #去重/写入文件
    f = open((sys.argv[2]),'a',encoding='utf-8')
    subdomain_res=list()
    for i in subdomain:
        if i not in subdomain_res:
            subdomain_res.append(i)
            print(i)
            f.write(i+'\n')
    print(name+'总共获取域名：',len(subdomain_res))
    f.close()

f=open(file)
names=[i.replace('\n','') for i in f]
print(names)
f.close()

for i in names:
    test(i)
