import csv
import re

f=open('C:/Users/Meher/Desktop/dataset/sample1.txt','r')
csv_reader = csv.reader(f,delimiter = ';')
data = []
comments = []


for row in csv_reader:
    data.append(row)

def convert_row(row):
    return """<Time="%s">
    <Type>%s</Type>
    <Trial>%s</Trial>
    <L POR X [px]>%s</L POR X [px]>
    <L POR Y [px]>%s</L POR Y [px]>
    <R POR X [px]>%s</R POR X [px]>
    <R POR Y [px]>%s</R POR Y [px]>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6])

print ('\n'.join([convert_row(row) for row in data[1:]]))