import csv
import pandas
import statistics

tottemp=0
recct=0
# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline='')
csv_reader = csv.reader(csvfile)
header = next(csv_reader, None)

line = csvfile.readline()
print(line, "readline1")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
#print(line, "readline1")

line = csvfile.readline()
print(line, "readline2")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
#print(line, "readline2")

line = csvfile.readline()
print(line, "readline3")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
#print(line, "readline3")

line = csvfile.readline()
print(line, "readline4")
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
#print(line, "readline4")

totavg = tottemp/recct
print("Totavg" ,totavg)