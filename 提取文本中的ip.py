import re,sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input","-i",help="输入文件",required=True)
parser.add_argument("--output","-o",help="输出文件",required=False)
args=parser.parse_args()



f=open(args.input,encoding='utf-8')
data=f.read()
f.close()

ip=re.findall(r"[\d]+[.][\d]+[.][\d]+[.][\d]+",data)
ip=list(set(ip))

if args.output:
    ip = ('\n').join(ip)
    f = open(args.output,'w',encoding='utf-8')
    f.write(ip)
    f.close()
