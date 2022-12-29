import sys

num = int(sys.argv[2])

f=open(sys.argv[1],'r')
list=f.readlines()
f.close()

len=len(list)
pages =int(len/num)

for a in range(0,pages):
    filename=str(a)+'.csv'
    f=open(filename,'w')
    for i in range(a*num,(a+1)*num):
        f.write(list[i].replace('\n','')+','+list[i])

filename=str(pages)+'.csv'
f=open(filename,'w')
for i in range(pages*num,len):
    f.write(list[i].replace('\n','')+','+list[i])

print('end!\ttotal:%-5s\tnum:%-5s\tpages:%-5s'%(len,num,pages+1))
