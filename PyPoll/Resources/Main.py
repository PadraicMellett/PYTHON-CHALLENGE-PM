# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# store contents in variables, lists, and dictionaries;
# iterate through basic data structures;

# Read in CSV 
import os
import csv
# Create dictionary to store pairs of the values  
election ={}
# Starts the count at zero
total_votes = 0

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
# Store the Header Row 
     csv_header = next(csvreader)
     for row in csvreader:
        total_votes += 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1 

    
     candidates = []
     vote_count = []

#Populate the lists with the dicitonary keys and values by candidate and vote

for key, value in election.items():
    candidates.append(key)
    vote_count.append(value)

#Populate the lists with the dicitonary keys and values by candidate and vote

for key, value in election.items():
    candidates.append(key)
    vote_count.append(value)
   
#Create percentages

voting_percent =[]
for i in vote_count:
    voting_percent.append((i/total_votes)*0.01)

#zip results into tuples
 Results =list(zip(candidates, vote_count, voting_percent))

 Winner = []
 
 ## ran out of time to work through this and get it working. 



  

