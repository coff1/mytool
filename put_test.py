import requests
import sys
import multiprocessing
from multiprocessing import Pool
# put请求是否开放？

def test(url,res):
    try:
        headers={"Connect":"close"}
        target = url.replace('\n','').rstrip('/') + '/6428484.txt'
        x=requests.put(target,data='hello84536nsaiogrhwokoqguAGG_',headers=headers,timeout=0.1)
        x.close()
        try:
            y=requests.get(target,timeout=0.1)
            print("%-50s\t%-10s\t%-10s\t" %(target,str(y.status_code),str(len(y.text))),end='\n')
            if  'hello84536nsaiogrhwokoqguAGG_' in y.text:
                res.append(target)
                print('find!\t'+target + '\t' + str(y.status_code))
        except BaseException:
            return 0                    
    except BaseException:
        return 0


if __name__ =='__main__': 

    f=open(sys.argv[1],"r")
    res=open("res.txt","w")

    list=f.readlines()
    f.close()

    res= multiprocessing.Manager().list()
    pool = Pool(processes = 10) #最多允许n个进程

    for url in list:
        pool.apply_async(test,(url,res))

    pool.close()
    pool.join()


    f=open('res.txt','w')
    for i in res:
        f.write(i.replace('\n','')+'\n')
    f.close()
