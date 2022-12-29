import socket
import multiprocessing
from multiprocessing import Process,Pool
import time
import sys
# f=open('domain.txt','r')
# host_list=list()
# for i in f.readlines():
#     host_list.append(i.replace('\n',''))

# for host in host_list:
#     try:
#         ip = socket.gethostbyname(host)
#         print(ip)
#     except socket.error as e:
#         pass

def get_ip(host,res):
    try:
        ip = socket.gethostbyname(host)
        res[host]=ip
        print('%-50s\t%-2s\n'%(host,str(ip)))
    except socket.error as e:
        pass

if __name__ =='__main__': 

    f=open('domain.txt','r')
    host_list=list()
    for i in f.readlines():
        host_list.append(i.replace('\n',''))

    
    res= multiprocessing.Manager().dict() 

    pool = Pool(processes = 10) #最多允许n个进程

    process_list = list() #生成进程列表

    for host in host_list:
        pool.apply_async(get_ip,(host,res))

    pool.close()
    pool.join()



    f=open('res_domain_to_ip.csv','w')
    f_=open('res_ip.txt','w')
    
    ip_list=list()
    for i in res:
        ip_list.append(res[i])
        f.write(i+','+str(res[i])+'\n')
    
    for ip in ip_list:
        f_.write(str(ip)+'\n')

    print('end!!! total:'+str(len(ip_list)))

    f.close()
    f_.close()