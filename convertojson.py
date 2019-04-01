import json
import re
import csv


comments = []
content = []
file = open('C:/Users/Meher/Desktop/dataset/sample1.txt', 'r')
jsonfile = open('C:/Users/Meher/Desktop/dataset/file.json', 'w')

count = 0
for line in file:
    count += 1
    if '##' in line:
        comments.append(line)
    else:
        content.append(line)
fieldnames = content[0].split(';')
jsonfile.writelines(comments)
reader1 = csv.DictReader(content,fieldnames,delimiter = ';') #check whether delimiter is workink
jsonfile.write('[')
for idx,row in enumerate(reader1,start = 1):
    json.dump(row, jsonfile)
    jsonfile.writelines('\n')
    if (idx != count):
        jsonfile.write(',')
jsonfile.write(']')