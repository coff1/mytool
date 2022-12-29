import sys
f1=open(sys.argv[1])
f2=open(sys.argv[2],'w')

input = list()

for i in f1.readlines():
    input.append(i.replace('\n',''))

for i in input:
    f2.write(i+sys.argv[3]+'\n') 

f1.close()
f2.close()

print('源文件+生成文件+需要添加的后缀')