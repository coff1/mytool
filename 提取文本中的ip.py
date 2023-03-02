import re,sys
f=open(sys.argv[1])
data=f.read()
f.close()

ip=re.findall(r"[\d]+[.][\d]+[.][\d]+[.][\d]+",data)
for i in ip:
    print(i) 