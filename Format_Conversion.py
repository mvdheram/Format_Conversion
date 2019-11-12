import os
import json
import csv
import re


def dump(fname):
    file, file_extension = os.path.splitext(fname)
    return file_extension


def converTxtTocsv(fname):
    with open(fname, 'r') as file:
        file.seek(0, 0)
        comments = []
        lines = []
        for line in file:
            if '##' in line:
                comments.append(line.strip().split(','))
            elif (line):
                lines.append(line.strip().split(';'))
    with open('convertedToCSV.csv', 'w') as out:
        out.seek(0)
        writer = csv.writer(out)
        writer.writerows(comments)
        writer.writerows(lines)  # writer.writerows(lines)## appending rows to the file

    out.close()
    file.close()
def converTxtTojson(fname):
    comments = []
    content = []
    file = open(fname, 'r')
    jsonfile = open('convertedToJSONfile.json', 'w')

    count = 0
    for line in file:
        count += 1
        if '##' in line:
            comments.append(line)
        else:
            content.append(line)
    fieldnames = content[0].split(';')
    jsonfile.writelines(comments)
    reader1 = csv.DictReader(content, fieldnames, delimiter=';')  # check whether delimiter is workink
    jsonfile.write('[')
    for idx, row in enumerate(reader1, start=1):
        json.dump(row, jsonfile)
        jsonfile.writelines('\n')
        if (idx != count):
            jsonfile.write(',')
    jsonfile.write(']')


def converTxtToXML(fname):
    f = open(fname, 'r')
    k = open('convertedToXMLfile.xml', 'w')

    data = []
    comments = []

    for line in f:
        if '##' in line:
            comments.append(line)
        else:
            data.append(line.strip().split(';'))
    k.writelines(comments)
    k.writelines('<?xml version="1.0"?>' + "\n")
    for row in data[2:]:
        k.writelines('<row>\n')
        for x in range(len(data[1])):
            k.writelines((("<%s>%s</%s>" % ((data[1][x], row[x], data[1][x])))))
            k.writelines('\n')
    k.writelines('</row>\n')

def convertCsvToJson(fname):
    csvData = open(fname, 'r')
    converted = open('convertedToJson.json', 'w')

    fieldnames1 = ('participantID', 'age', 'sexMale', 'visionAid', 'experienceHours', 'randomSeed')
    fieldnames = ('Location X', 'Location Y', 'Timestamp', 'Validity')
    converted.writelines('[')
    converted.writelines("\n")

    def dump(list):
        for i in range(len(list) - 1):
            z = '"' + fieldnames[i % 4] + '"' + ":" + '"' + list[i] + '"'
            converted.writelines(z)
            if ((i + 1) % 4 != 0):
                converted.write(",")
            if ((i + 1) % 4 == 0):
                converted.writelines("\n")
                converted.writelines("}")
            if ((i + 1) % 4 == 0 and i <= len(list) - 4):
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
            json.dump(dict(striped[i].strip().split(":") for i in range(0, len(striped))), converted)
            converted.writelines(",")
            converted.writelines("\n")
        if 'Target' in line:
            striped = line.strip().split(' ', 1)
            i = [(striped[i], striped[i + 1]) for i in range(0, len(striped), 2)]
            converted.writelines("\n")
            json.dump(dict(i), converted)
            converted.writelines(",")
            converted.writelines("\n")
        if 'Active' in line or 'Passive' in line or 'Pressed' in line:
            striped = line.strip().split(":")
            i = [(striped[i], striped[i + 1]) for i in range(0, len(striped), 2)]
            converted.writelines("\n")
            json.dump(dict(i), converted)
            converted.writelines(",")
            converted.writelines("\n")
        if 'Gazepoints: (Location X; Location Y; Timestamp; Validity)' in line and 'Selection of (final) Stimulus is done, Confirmation or following' not in line:
            firstline = line
            stripped = firstline.split(":")
            i = [(stripped[i], stripped[i + 1]) for i in range(0, len(stripped), 2)]
            json.dump(dict(i), converted)
            converted.writelines('\n')
            converted.writelines(",{")
            nextline = next(csvData)
            comments = nextline.strip().split(';')
            dump(comments)
        if 'Selection of (final) Stimulus is done, Confirmation or following Gazepoints: (Location X; Location Y; Timestamp; Validity' in line:
            firstline1 = line
            strippedfirst = firstline1.split(":")
            converted.write(",{")
            converted.write('"' + strippedfirst[0] + '"' + ':' + '"' + strippedfirst[1].strip() + '"')
            converted.write("}")
            converted.writelines("\n")
            converted.writelines(",{")
            nextline = next(csvData)
            lines = nextline.strip().split(';')
            dump(lines)
        if "Trial completed" in line:
            converted.writelines(',')
            converted.writelines('{')
            converted.writelines('"' + 'Trial' + '"' + ':' + '"' + 'completed' + '"')
            converted.writelines('}')

    converted.writelines("]")


def convertCsvToXML(fname):
    csvData = open(fname, 'r')
    converted = open('convertedToXML.xml', 'w')

    fieldnames1 = ('participantID', 'age', 'sexMale', 'visionAid', 'experienceHours', 'randomSeed')
    fieldnames = ('Location X', 'Location Y', 'Timestamp', 'Validity')
    converted.writelines('<?xml version="1.0"?>' + "\n")

    def dump(list):
        for i in range(len(list) - 1):
            z = '<' + fieldnames[i % 4] + '>' + list[i] + '</' + fieldnames[i % 4] + '>'
            converted.writelines('\n')
            converted.writelines(z)
            converted.writelines('\n')

    for line in csvData:
        if "----------" not in line and 'T' not in line and 'A' not in line and 'P' not in line:
            striped = line.strip().split(";")
            for x in range(len(fieldnames1)):
                converted.writelines("<%s>%s</%s>" % (fieldnames1[x], striped[x].strip(","), fieldnames1[x]))
                converted.writelines("\n")
        if "----------," in line:
            continue
        if 'TrialID' in line:
            striped = line.strip().split(";")
            converted.writelines('\n')
            for i in range(0, len(striped)):
                splitting = striped[i].strip().split(":")
                converted.write("<%s>%s</%s>" % (splitting[0], splitting[1].strip(','), splitting[0]))
                converted.writelines('\n')
        if 'Target' in line:
            striped = line.strip().split(' ', 1)
            converted.writelines("<%s>%s</%s>" % (striped[0], striped[1].strip(','), striped[0]))
            converted.writelines("\n")
            converted.writelines("\n")
        if 'Active' in line or 'Passive' in line or 'Pressed' in line:
            striped = line.strip().split(":")
            converted.writelines("<%s>%s</%s>" % (striped[0], striped[1].strip(",;"), striped[0]))
            converted.writelines("\n")
        if 'Gazepoints: (Location X; Location Y; Timestamp; Validity)' in line and 'Selection of (final) Stimulus is done, Confirmation or following ' not in line:
            firstline1 = line
            strippedfirst = firstline1.split(":")
            converted.writelines('\n')
            converted.writelines("<!--%s>%s<%s-->" % (strippedfirst[1], strippedfirst[0], strippedfirst[1]))
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
            converted.writelines('<' + 'Trial' + '>' + 'completed' + '</' + 'Trial' + '>')
            converted.writelines('\n')


def Main():
    fname = 'file'  # please provide the file path here
    type = dump(fname)
    print("The file is of type:" + type)
    if (type == ".txt"):
        txt = input("please press 0 for CSV(;seperated), 1 for JSON, 2 for XML, 3 for all the formats: ")
        print("entered input is : %s " % txt )
        if (txt == '0'):
            converTxtTocsv(fname)
            print("finished")
        if (txt == '1'):
            converTxtTojson(fname)
            print("finished")
        if (txt == '2'):
            converTxtToXML(fname)
            print("finished")
        if (txt == '3'):
            converTxtTocsv(fname)
            converTxtTojson(fname)
            converTxtToXML(fname)
            print("finished")
        else:
         print("please enter a valid input")
    if (type == ".csv"):
        txt = input("please press 1 for JSON, 2 for XML, 3 for all the formats")
        print("entered input is : %s " % txt)
        if (txt == '1'):
            convertCsvToJson(fname)
            print("finished")
        if (txt == '2'):
            convertCsvToXML(fname)
            print("finished")
        if (txt == '3'):
            convertCsvToJson(fname)
            convertCsvToXML(fname)
            print("finished")
        else:
            print("please enter a valid input")


# parser = argparse.ArgumentParser(description='file format changer')
# parser.add_argument('-all','--all',metavar = '', help = 'convert to all formats')
# parser.add_argument('-csv','--csv',metavar = '', help = 'convert to CSV format')
# parser.add_argument('-XML','--XML',metavar = '', help = 'convert to XML formats')
# parser.add_argument('-JSON','--JSON',metavar = '', help = 'Convert to JSON format')
# parser.add_argument('-sh','--show',metavar = '', help = 'show the file extension')
# args = parser.parse_args()
# dump(args.add)


if __name__ == "__main__":
    Main()
