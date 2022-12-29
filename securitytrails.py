import requests
import json
import sys

name=sys.argv[1]

filename=name+'_securitytrails.txt'

url='https://api.securitytrails.com/v1/domain/'+name+'/subdomains'

kw = {'children_only':'false','include_inactive':'true'}

headers = {"APIKEY": "9MuSQfXJbNwZcfKkIG52mRvp84CfEQSt","Accept":"application/json"}
 
x=requests.get(url,params = kw, headers= headers)

dict = json.loads(x.text)

f=open(filename,'w')

for i in dict['subdomains']:
    i=i+'.'+name
    print(i)
    f.write(i+'\n')
f.close()