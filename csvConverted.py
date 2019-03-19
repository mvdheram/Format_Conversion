
import csv
import re
import json
csvFile = ''
xmlFile = 'myData.xml'

converted = open('C:/Users/Meher/Desktop/dataset/sample.json', 'w')
csvData = open('C:/Users/Meher/Desktop/dataset/csvfiles/full.csv', 'r')

fieldnames1 = ('participantID','age','sexMale','visionAid','experienceHours','randomSeed')
fieldnames = ('Location X', 'Location Y', 'Timestamp', 'Validity')
converted.writelines('[')
converted.writelines("\n")

def dump(list):
    for i in range(len(list)-1):
        z ='"'+fieldnames[i%4]+'"'+":"+'"'+list[i]+'"'
        converted.writelines(z)
        if((i+1)%4!= 0):
            converted.write(",")
        if((i+1)%4 == 0):
            converted.writelines("\n")
            converted.writelines("}")
        if((i+1)%4 == 0 and  i <= len(list)-4):
            converted.writelines("\n")
            converted.writelines(',{')
        converted.writelines("\n")
csvData.seek(0, 0)

for line in csvData:
    if "----------\n" not in line and 'T' not in line and 'A' not in line and 'P' not in line:
        striped = line.strip().split(";")
        converted.writelines("\n")
        json.dump(dict(zip(fieldnames1, striped)), converted)
        converted.writelines("\n")
    if "----------\n," in line:
        continue
    if 'TrialID' in line:
        striped = line.strip().split(";")
        converted.writelines("\n")
        converted.writelines(',')
        json.dump(dict(striped[i].strip().split(":") for i in range(0,len(striped))),converted)
        converted.writelines(",")
        converted.writelines("\n")
    if 'Target' in line:
        striped = line.strip().split(' ',1)
        i = [(striped[i], striped[i + 1]) for i in range(0, len(striped), 2)]
        converted.writelines("\n")
        json.dump(dict(i),converted)
        converted.writelines(",")
        converted.writelines("\n")
    if 'Active' in line or 'Passive' in line or 'Pressed' in line:
        striped = line.strip().split(":")
        i = [(striped[i], striped[i + 1]) for i in range(0, len(striped), 2)]
        converted.writelines("\n")
        json.dump(dict(i),converted)
        converted.writelines(",")
        converted.writelines("\n")
    if 'Gazepoints: (Location X; Location Y; Timestamp; Validity)' in line and 'Selection of (final) Stimulus is done, Confirmation or following' not in line :
        firstline = line
        stripped = firstline.split(":")
        i = [(stripped[i], stripped[i + 1]) for i in range(0, len(stripped), 2)]
        json.dump(dict(i),converted)
        converted.writelines('\n')
        converted.writelines(",{")
        nextline = next(csvData)
        comments = nextline.strip().split(';')
        dump(comments)
    if 'Selection of (final) Stimulus is done, Confirmation or following Gazepoints: (Location X; Location Y; Timestamp; Validity' in line:
        firstline1 = line
        strippedfirst = firstline1.split(":")
        converted.write(",{")
        converted.write('"'+strippedfirst[0]+'"'+':'+'"'+strippedfirst[1].strip()+'"')
        converted.write("}")
        converted.writelines("\n")
        converted.writelines(",{")
        nextline = next(csvData)
        lines = nextline.strip().split(';')
        dump(lines)
    if "Trial completed" in line:
        converted.writelines(',')
        converted.writelines('{')
        converted.writelines('"'+'Trial'+'"'+':'+'"'+'completed'+'"')
        converted.writelines('}')

converted.writelines("]")



