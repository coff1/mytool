import requests
from bs4 import BeautifulSoup
import sys

name=sys.argv[1]

filename = name + "_rapiddns.txt"

url = 'https://rapiddns.io/subdomain/' + name + '?full=1'

x=requests.get(url)
x.close()

f=open(filename,'w')

pagesoup = BeautifulSoup(x.text,'lxml')
for i in pagesoup.text.split('\n'):
    if name in i:
        print(i)
        f.write(i+'\n')
        
f.close()
