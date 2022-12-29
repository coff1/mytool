import requests
import multiprocessing
from multiprocessing import Process,Pool
import sys

def returnCode(url,res):
    try:
        headers={
            'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Media Center PC 4.0)',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1'
        }
        x = requests.get(url,headers=headers,timeout=1)
        if x.status_code in [200] and 'error' not in x.text and 'updaterid' in x.text:
            res[url]=x.status_code
        print(url+str(x.status_code))
    except BaseException:
        return 0

if __name__ =='__main__':

    f1 = open(sys.argv[1])
    f2 = open(sys.argv[2],'w')

    input = list()
    for i in f1.readlines():
        input.append(i.replace('\n',''))
    
    f1.close()

    res = multiprocessing.Manager().dict()

    pool = Pool(processes=100)

    for url in input:
        # print(url)
        pool.apply_async(returnCode,(url,res))

    pool.close()
    pool.join()

    for i in res:
        f2.write(str(i)+','+str(res[i])+'\n')

    print('end!!!!!!!!!!!!!!!')

    f2.close()