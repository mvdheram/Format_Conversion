import re

f = open('C:/Users/Meher/Desktop/dataset/sample1.txt','r')
k = open('C:/Users/Meher/Desktop/dataset/sample.xml','w+')

data = []
comments = []

for line in f:
    if (re.findall("[##]",line)):
        comments.append(line.strip().split(','))
    else:
        data.append(line.strip('\n').split(';'))

q = len(data[0])

k.writelines(comments)
for row in data[1:]:
    k.writelines('<row>\n')
    for x in range(q):
      k.writelines((( """<%s>%s</%s>""" % ((data[0][x],row[x],data[0][x])))))
      k.writelines('\n')
    k.writelines('</row>\n')