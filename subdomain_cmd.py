import sys
domain=sys.argv[1]
# filename=domain+'_commend.txt'
# f=open('filename','w')
commend_list=[
    'python rapiddns.py '+domain,
    'python securitytrails.py '+domain,
    './xray subdomain --target '+domain+' --text-output '+domain+'_xray.txt',
    './subfinder -d '+domain+' -all -o '+domain+'_subfinder.txt'
]
for i in commend_list:
    print(i)

# f.close()