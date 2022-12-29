# -*- coding: UTF-8 -*-
import requests
import socket
import multiprocessing
from multiprocessing import Process,Pool

#发包检测状态码
def test(i):
    try:
        headers={
            'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Media Center PC 4.0)',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1'
        }
        x = requests.get(i,headers=headers,timeout=1,allow_redirects=False)
        if x.status_code in [200] and len(x.text)>50000:
            print('find!!!!\t'+i+'\t'+str(x.status_code))
            print(len(x.text))
    except BaseException:
        return 0

if __name__ =='__main__': 
    f = open('dict1.txt','r',encoding='utf-8')
    dict1=list()
    for i in f.readlines():
        dict1.append(i.replace('\n',''))
    f.close()

    f = open('dict2.txt','r',encoding='utf-8')
    dict2=list()
    for i in f.readlines():
        dict2.append(i.replace('\n',''))
    f.close()

    f = open('输入.txt','r',encoding='utf-8')
    url_list=list()
    for i in f.readlines():
        url_list.append(i.replace('\n',''))
    f.close()

    #生成字典
    dict=list()
    for i in dict1:
        for j in dict2:
            dict.append(i+j)

    #拼接url
    url=list()
    for i in url_list:
        for j in dict:
            url.append(i+j)
            # print(i+j)

    print("预计发包"+str(len(url))+'次')
    
    pool = Pool(processes = 10) #最多允许n个进程

    process_list = list() #生成进程列表
    for i in url:
        pool.apply_async(test,(i,))

    pool.close()
    pool.join()