import re

f = open("macs.txt",'r')
f_parsed = open("parsed_macs.txt", 'w')
p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
result = []
for line in f:
    result += re.findall(p,line)
result = list(set(result))

for mac in result:
    f_parsed.write(mac+'\n')

f.close()
f_parsed.close()
