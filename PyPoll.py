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
electionPath = os.path.join("Resources","election_results.csv")

#Assign a variable to save teh file to a path
fileToWriteIn = os.path.join("Analysis", "election_analysis.txt")

#add variable, list, and dictionaries needed
totalVotes = 0
candidates = []
candidateVotes = {}
winner = ""
winningCount = 0
WinningPerc = 0.0

#Open the election results and read the file.
with open(electionPath) as electionFile:

#Read and Analyze data here
    #set variable to read csv file
    ElectionData = csv.reader(electionFile)

    headers = next(ElectionData)


    #print each row in the CSV file and count for total votes
    for row in ElectionData:
        totalVotes += 1
        #get candidate name
        candidateName = row[2]
        
        #adding candidate names by checking if it is in the list already and adding to dictionary
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 0

    
        #Add a vote to that candidate's name
        candidateVotes[candidateName] += 1

    for candidates in candidateVotes:
        votes = candidateVotes[candidates]
        voteperc = round(float(votes) / float(totalVotes) * 100, 1)
        
        print(f"{candidates}: received {voteperc}% meaning they received {votes:,} votes out of {totalVotes:,}\n")
        
        if (votes > winningCount) and (voteperc > WinningPerc):
            winningCount = votes
            WinningPerc = voteperc
            winner = candidates

    winnerSummary = (
        f"----------------------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winningCount: ,} \n"
        f"Winning Percentage: {WinningPerc}% \n"
        f"----------------------------------------\n \n CONGRATULATIONS!!!"
    )
    print(winnerSummary)





