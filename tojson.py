import json
csvFile = ''
xmlFile = 'myData.xml'

converted = open('C:/Users/Meher/Desktop/dataset/sample.xml', 'w')
csvData = open('C:/Users/Meher/Desktop/dataset/csvfiles/full.csv', 'r')

fieldnames1 = ('participantID','age','sexMale','visionAid','experienceHours','randomSeed')
fieldnames = ('Location X', 'Location Y', 'Timestamp', 'Validity')
converted.writelines('<?xml version="1.0"?>' + "\n")


def dump(list):
    for i in range(len(list)-1):
        z ='<'+fieldnames[i%4]+'>'+list[i]+'</'+fieldnames[i%4]+'>'
        converted.writelines('\n')
        converted.writelines(z)
        converted.writelines('\n')
for line in csvData:
    if "----------" not in line and 'T' not in line and 'A' not in line and 'P' not in line:
        striped = line.strip().split(";")
        for x in range(0, len(fieldnames1)):
            converted.writelines("<%s>%s</%s>" % (fieldnames1[x],striped[x].strip(","),fieldnames1[x]))
            converted.writelines("\n")
    if "----------," in line:
        continue
    if 'TrialID' in line:
        striped = line.strip().split(";")
        converted.writelines('\n')
        for i in range(0, len(striped)):
            splitting = striped[i].strip().split(":")
            converted.write("<%s>%s</%s>"%( splitting[0],splitting[1].strip(','),splitting[0]))
            converted.writelines('\n')
    if 'Target' in line:
        striped = line.strip().split(' ', 1)
        converted.writelines("<%s>%s</%s>" % (striped[0],striped[1].strip(','),striped[0]))
        converted.writelines("\n")
        converted.writelines("\n")
    if 'Active' in line or 'Passive' in line or 'Pressed' in line:
        striped = line.strip().split(":")
        converted.writelines("<%s>%s</%s>" % (striped[0],striped[1].strip(",;"),striped[0]))
        converted.writelines("\n")
    if 'Gazepoints: (Location X; Location Y; Timestamp; Validity)' in line and 'Selection of (final) Stimulus is done, Confirmation or following ' not in line :
        firstline1 = line
        strippedfirst = firstline1.split(":")
        converted.writelines('\n')
        converted.writelines("<!--%s>%s<%s-->" % (strippedfirst[1],strippedfirst[0],strippedfirst[1]))
        nextline = next(csvData)
        converted.writelines('\n<row>\n')
        lines = nextline.strip().split(';')
        dump(lines)
        converted.writelines('</row>\n')
    if 'Selection of (final) Stimulus is done, Confirmation or following Gazepoints: (Location X; Location Y; Timestamp; Validity' in line:
        firstline1 = line
        strippedfirst = firstline1.split(":")
        converted.writelines('\n')
        converted.writelines("<!--%s>%s<%s-->" % (strippedfirst[1], strippedfirst[0], strippedfirst[1]))
        converted.writelines('\n<row>\n')
        nextline = next(csvData)
        lines = nextline.strip().split(';')
        dump(lines)
        converted.writelines('</row>\n')
    if "Trial completed" in line:
        converted.writelines('<'+'Trial'+'>'+'completed'+'</'+'Trial'+'>')
        converted.writelines('\n')