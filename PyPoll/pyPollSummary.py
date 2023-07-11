#Election Results of PyPoll election_data.csv

#import dependencies
import os
import csv

#import data
electionData = os.path.join("Resources", "election_data.csv")

#read the csv file
with open(electionData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csvheader = next(csvreader)

    #set baseline values
    totalVotes = 0
    candidates = {}

    for row in csvreader:
        #count the total votes
        totalVotes += 1

        #add each candidate to the list and count their votes
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

#Find the winner of the election
winner = max(candidates, key=candidates.get)

#Calculate election results and format
electionSummary = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
"""
for candidate, voteCount in candidates.items():  # Candidate Results
    percentage = (voteCount / totalVotes * 100)
    electionSummary += f"{candidate}: {percentage:.3f}% ({voteCount})\n"
electionSummary += f"""-------------------------
Winner: {winner}
-------------------------"""

#Print summary to terminal
print(electionSummary)

#create text file for summary
with open("pyPollSummary.txt","w") as summaryfile:
    summaryfile.write(electionSummary)