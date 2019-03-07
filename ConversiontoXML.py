import re

f = open('C:/Users/Meher/Desktop/dataset/sample1.txt','r')
k = open('C:/Users/Meher/Desktop/dataset/sample.xml','w')

data = []
comments = []

for line in f:
    if '##' in line:
        comments.append(line)
    else:
        data.append(line.strip('\n').split(';'))

length = len(data[0])
k.writelines(comments)
k.writelines('<?xml version="1.0"?>' + "\n")
for row in data[1:]:
    k.writelines('<row>\n')
    for x in range(length):
      k.writelines((( """<%s>%s</%s>""" % ((data[0][x],row[x],data[0][x])))))
      k.writelines('\n')
    k.writelines('</row>\n')