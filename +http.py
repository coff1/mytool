import sys

f = open(sys.argv[1],'r', encoding='UTF-8')
sub = [line.strip() for line in f.readlines()]
f.close()
for i in sub:
	if 'http' not in i:
		url = 'http://'+i+'/'
		urls = 'https://'+i+'/'
		with open(sys.argv[2], 'a') as o:
			o.write(url)
			o.write("\n")
			# o.write(urls)
			# o.write("\n")
			o.close()