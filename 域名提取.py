import sys
from urllib import parse
print('域名提取！\n use:源文件+输出文件')

f1 = open(sys.argv[1])
f2 = open(sys.argv[2],'w')

li_url = list()

for i in f1.readlines():
    li_url.append(i.replace('\n',''))

domain=list()

for url in li_url:
    j = parse.urlparse(url).netloc

    if ':' in j:
        j_=j.split(':')
        if j_[0] not in domain:
            domain.append(j_[0])
    elif j not in domain:
        domain.append(j)


for i in domain:
    f2.write(i+'\n')

f1.close()
f2.close()



