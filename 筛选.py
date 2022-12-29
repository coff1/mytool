import sys
f1 = open(sys.argv[1],'r',encoding='utf8')
f2 = open(sys.argv[1]+'_res.txt','w',encoding='utf8')

src=f1.readlines()
for i in src:
    if sys.argv[2] in i:
        f2.write(i)

f1.close()
f2.close()