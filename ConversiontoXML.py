import re

f = open('C:/Users/Meher/Desktop/dataset/sample1.txt','r')
k = open('C:/Users/Meher/Desktop/dataset/sample.xml','w+')

data = []
comments = []

for line in f:
    if (re.findall("[##]",line)):
        comments.append(line.strip().split(','))
    else:
        data.append(line.split(';'))

def changeToXML(row):
    return """<Time="%s">
    <Type>%s</Type>
    <Trial>%s</Trial>
    <L POR X [px]>%s</L POR X [px]>
    <L POR Y [px]>%s</L POR Y [px]>
    <R POR X [px]>%s</R POR X [px]>
    <R POR Y [px]>%s</R POR Y [px]>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
k.writelines(comments)
k.writelines('\n'.join([changeToXML(row) for row in data[1:]]))