import requests
import sys
import socket
import multiprocessing
from multiprocessing import Process,Pool

def test(domain,res):
    try:
        headers={
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1'
        }
        target = 'http://'+ domain + '/weaver/bsh.servlet.BshServlet/'
        x=requests.get(target,headers=headers,timeout=1.5)
        print(target+str(x.status_code))
        if x.status_code==200 and 'valuate' in x.text:
            print("find!!!!!!!!!!!!!!!!"+target)
            res.append(target)
        x.close()           
    except BaseException:
        return 0


if __name__ =='__main__':
    f=open(sys.argv[1])
    li=f.readlines()
    li_=list()
    for i in li:
        li_.append(i.replace('\n',''))
    f.close()

    res=multiprocessing.Manager().list()

    pool = Pool(processes = 100) #最多允许n个进程

    process_list = list() #生成进程列表
    for domain in li_:
        pool.apply_async(test,(domain,res))

    pool.close()
    pool.join()
    
    f=open(sys.argv[2],'w')
    for i in res:
        f.write(i+'\n')
    f.close()