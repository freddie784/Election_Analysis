#The Data we need to retrieve
#The total number of votes cast
#A complete List of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#the winner of the election based on popular vote.


#import needed modules
import csv
import os

#assign a variable for the file to load and the path
electionFile = os.path.join("Resources","election_results.csv")

#Assign a variable to save teh file to a path
fileToSave = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(electionFile) as electionData:

#Read and Analyze data here
    ElectionReader = csv.reader(electionData)

    headers = next(ElectionReader)
    print(headers)

#    for row in ElectionReader:
#        print(row[0])


