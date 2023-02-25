import requests
import json
import sys
import requests
from bs4 import BeautifulSoup
import sys
# 爬取网站的域名信息
# python +program.py +doamin
subdomain=list()

name=sys.argv[1]

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
f = open((name+'_subdomain.txt'),'w',encoding='utf-8')
subdomain_res=list()
for i in subdomain:
    if i not in subdomain_res:
        subdomain_res.append(i)
        print(i)
        f.write(i+'\n')
print('总共获取域名：',len(subdomain_res))
print('域名保存在文件：'+name+'_subdomain.txt')
f.close()

