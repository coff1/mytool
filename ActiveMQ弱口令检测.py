import requests
import re
import sys
from multiprocessing import Process,Pool

# url = "http://162.14.125.50:8161/admin/"
def test(url):
    try:
        headers={
            "Cache-Control":"max-age=0",
            "Authorization":"Basic YWRtaW46YWRtaW4=",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer":"http://162.14.125.50:8161/",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
        }
        x=requests.get(url,headers=headers,timeout=0.5)
        if x.status_code == 200:
            print(url.replace("/admin/",""),end="\t")
            version=(re.findall(r"[0-9]+[.][0-9]+[.][0-9]",x.text))
            print(version)
            for i in ["5.8.","5.9.","5.10.","5.0.11","5.12"]:
                if i in version:
                    print("find !!!!!!!!!!!!!!!!!")
                    break
    except BaseException:
        return 0

if __name__ =='__main__':

    f = open(sys.argv[1])

    input = list()
    for i in f.readlines():
        input.append(i.replace('\n','')+"admin/")
        # print(i.replace('\n','')+"admin/")
    
    f.close()

    pool = Pool(processes=10)

    for url in input:
        # print(url)
        pool.apply_async(test,(url,))

    pool.close()
    pool.join()

    print('end!!!!!!!!!!!!!!!')