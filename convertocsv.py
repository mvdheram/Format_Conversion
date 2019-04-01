import csv

with open('C:/Users/Meher/Desktop/dataset/sample1.txt','r') as file :
    file.seek(0,0)
    comments = []
    lines = []
    for line in file:
        if '##' in line:
            comments.append(line.strip().split(','))
        elif (line) :
            lines.append(line.strip().split(';'))
print(lines)
with open('C:/Users/Meher/Desktop/dataset/convertedtoCSV.csv','w') as out:
    out.seek(0)
    writer = csv.writer(out)
    writer.writerows(comments)
    writer.writerows(lines)#writer.writerows(lines)## appending rows to the file

out.close()
file.close()
