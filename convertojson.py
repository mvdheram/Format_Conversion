import json
import re
import csv


comments = []
content = []
file = open('C:/Users/Meher/Desktop/dataset/sample1.txt', 'r')
jsonfile = open('C:/Users/Meher/Desktop/dataset/file.json', 'w')

fieldnames = ("Time","Type","Trial","L POR X [px]","L POR Y [px]","R POR X [px]","R POR Y [px]")

for line in file:
    if (re.findall("[##]", line)):
        comments.append(line)
    else:
        content.append(line)

jsonfile.writelines(comments)
reader1 = csv.DictReader(content,fieldnames,delimiter = ';')

for row in reader1:
    json.dump(row, jsonfile)
    jsonfile.write('\n')