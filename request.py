import sys
import requests
x = requests.get(sys.argv[1])
print(x.text+'\n'+str(x.status_code))