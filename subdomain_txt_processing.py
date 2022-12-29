import sys
domain =sys.argv[1]
# domain ='meituan.com'

file_name=(domain+'_sub_all.txt')

# 处理其他结果

file_list = list()
for i in ['subfinder','rapiddns','securitytrails']:
    file_list.append(domain+'_'+i+'.txt')

sub_list=list()

for i in file_list:
    f=open(i,'r')
    for j in f.readlines():
        sub_list.append(j)    
    f.close()


# 处理xray结果
f=open(domain+'_xray.txt')
for i in f.readlines():
    if ',' in i:
        j = i.split(',')
        sub_list.append(j[0])
f.close()


# 去重，去换行符，写入
sub_end = list()
f=open(file_name,'w')
for i in sub_list:
    j=i.replace('\n','')
    if j not in sub_end:
        sub_end.append(j)
        f.write(j+'\n')
f.close()

print(len(sub_list))
print(len(sub_end))