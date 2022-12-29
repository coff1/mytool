import sys
print('链接提取域名,源文件+输出文件名')

f= open(sys.argv[1])
li=f.readlines()
f.close()

li_=list()

for i in li:
    i=i.replace('https://','')
    i=i.replace('http://','')
    i=i.replace('\n','')
    if ':' in i:
        i=i.split(':')
        if i[0] not in li_:
            li_.append(i[0])
    elif '/' in i:
        i=i.split('/')
        if i[0] not in li_:
            li_.append(i[0])
    else:
        if i not in li_:
            li_.append(i)


f=open(sys.argv[2],'w')
for i in li_:
    f.write(i+'\n')
f.close()

