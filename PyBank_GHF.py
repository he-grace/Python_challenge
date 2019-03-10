import csv

#1st Answer
count = len(open("C://Users//grace//Desktop//TECMC201902DATA2//02-Homework//03-Python//Instructions//PyBank//Resources//budget_data.csv").readlines(  ))
print(count)

#2nd Answer
csvpath = "C://Users//grace//Desktop//TECMC201902DATA2//02-Homework//03-Python//Instructions//PyBank//Resources//budget_data.csv"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])
    print(total)

#3rd Answer
sum_change = 0
data= []
import sys, argparse, os
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        data += csvreader

    for i in range(len(data)):
        if i >= 1:
            data[i].extend([int(data[i][1]) - int(data[i-1][1])])
            sum_change += data[i][2]
            mean_change= sum_change/count
    print(mean_change)
            
#4th Answer
    for i in range(len(data)):
        if i >= 1:
            changes= data[i].extend([int(data[i][1]) - int(data[i-1][1])])
            changes.max()
    


       
