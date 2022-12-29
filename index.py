f=open('index.txt','r',encoding='utf-8')
li=f.read()
li=li.split('\n')

res=list()
for i in li:
    for j in ['1','2','3','4','5','6','7','8','9','0',',','.','"','、']*2:
        i=i.strip(j)
    if len(i)>1 and i not in res:
     res.append(i)


f=open('res.txt','w')
for i in res:
    print(i)
    f.write(i+'\n')
f.close()
print('处理前：'+str(len(li))+'行')
print('提取出：%s个问题'%str(len(res)))