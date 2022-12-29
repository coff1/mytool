import requests
import re
import sys
import argparse
parse = argparse.ArgumentParser()
parse.add_argument("--ip",'-i',type=str,required=False)
parse.add_argument("--list",'-l',type=str,required=False)
parse.add_argument("--output",'-o',type=str,required=False)
args = parse.parse_args()

def test(ip):
    proxies={
        'http':'127.0.0.1:7890',
        'https':'127.0.0.1:7890'
    }
    # https://www.bing.com/search?q=ip%3A8.8.8.8
    # f=open(r"C:\Users\user\Desktop\1 (1).txt",encoding="utf-8")
    # data=f.read()
    url="https://www.bing.com/search?q=ip%3A"+ip
    # print(url)
    headers = {
                "Content-Type":"application/x-www-form-urlencoded",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            }
    x=requests.get(url,headers=headers,proxies=proxies)
    # print(x.text)
    data=x.text

    # 使用find()方法提取数据例子：

    from bs4 import BeautifulSoup
    # # 引入bs库
    
    # res = requests.get('https:www.example.com')
    # # 获取https:www.example.com网页信息
    # print(res.status_code)
    # # 检查请求是否成功
    # string = res.text
    # # 将数据转换为字符串格式
    soup = BeautifulSoup(data,'html.parser')
    # 解析数据至可读懂格式
    data = soup.find_all('cite')
    # 提取首个<div>元素，并命名变量为data
    res=list()
    for i in data:
        i=str(i)
        i=i.replace("<cite>","")
        i=i.replace("</cite>","")
        res.append(i)
        print(i)
    return res


ip=args.ip
test(ip)