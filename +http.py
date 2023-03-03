import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mode","-m",help="指定添加的协议 http/https/all(http and https)...或者其他特定的",required=False,default='http')
parser.add_argument("--input","-i",help="指定含输入内容的文件",required=True)
parser.add_argument("--output","-o",help="指定输出的文件名",required=False)
parser.add_argument("--path","-p",help="生成的url路径,默认为'/'",required=False,default="/")

args=parser.parse_args()


f_input=open(args.input,'r',encoding='utf-8')
date_input = list()

for i in f_input.readlines():
    if i.strip() not in date_input:
        date_input.append(i.strip())
f_input.close()
        



result=""

if args.mode == 'all':
    for i in date_input:
        result+='https://'+i+args.path+'\n'
        result+='http://'+i+args.path+'\n'
    
else:
	for i in date_input:
		result+=args.mode+'://'+i+args.path+'\n'
		result+=args.mode+'://'+i+args.path+'\n'
                
print(result)

if args.output:
    f_output = open(args.output,'w',encoding='utf-8')     
    f_output.write(result)     
    f_output.close()
    print("down! Results are saved in {}".format(args.output))