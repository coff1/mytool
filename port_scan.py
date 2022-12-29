import socket
import multiprocessing
from multiprocessing import Process,Pool
import time
import sys

def TCP_connect(ip,port_list,delay,res):
    res_={}
    for port in port_list:
        #初始化套接字
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # TCP_sock.setsockopt(socket.SOL_SOCKET, 1)
        TCP_sock.settimeout(delay)
        try:
            result = TCP_sock.connect_ex((ip, int(port)))

            #握手成功端口开放，否则关闭
            if result == 0:
                res_[port] = '\033[0;31;40mopen\033[0m'
            else:
                res_[port] = 'close'

            TCP_sock.close()

        except socket.error as e:

            res_[port] = 'close'
            pass
    res[ip]=res_

    print(ip,end='\t')
    for i in port_list:
        print(str(i)+':'+str(res_[i]),end='  ')
    print('')



if __name__ =='__main__': 

    ip_list=list()
    port_list=list()
    
    f=open(sys.argv[1],'r')
    for i in f.readlines():
        ip_list.append(i.replace('\n',''))
    f.close()

    # ip_list=['101.34.85.116','192.168.169.162']
    port_list=[22,80,443,445]
    thread_num = 100
    delay = 0.1
    
    print("\033[0;34;40mstaring port scan\033[0m")

    res= multiprocessing.Manager().dict()

    
    pool = Pool(processes = 10) #最多允许n个进程

    process_list = list() #生成进程列表
    for ip in ip_list:
        pool.apply_async(TCP_connect,(ip,port_list,delay,res))

    pool.close()
    pool.join()

    print(res)



