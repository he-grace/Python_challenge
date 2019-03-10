#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import csv

#1st Answer
count = len(open("C://Users//grace//Desktop//TECMC201902DATA2//02-Homework//03-Python//Instructions//PyPoll//Resources//election_data.csv").readlines(  ))
print(count)

#2nd Answer
csvpath = "C://Users//grace//Desktop//TECMC201902DATA2//02-Homework//03-Python//Instructions//PyPoll//Resources//election_data.csv"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(csvfile):
        