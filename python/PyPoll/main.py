#Import modules and define the CSV we want to read
import os
import csv
csvpath = r"C:\Users\grant\Desktop\python-challenge\PyPoll\resources\election_data.csv"

#Print the beginning
print("\nElection Results\n-------------------------\n")

#Initialize the counter variables
total_votes = 0
candidate_null = ""
candidates = []
vote_counts = {}

#Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #Iterate through the rows
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] != candidate_null and row[2] not in candidates:
            candidates.append(row[2])

        candidate = row[2]        
        if candidate not in vote_counts:
            vote_counts[candidate] = 1
        else: 
            vote_counts[candidate] = vote_counts[candidate] +1
    
    print(f"Total Votes: {total_votes}\n\n-------------------------\n")
    
    for candidate, count in vote_counts.items():
        percentage = (count / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({vote_counts[candidate]})\n")
        
    
    winner = max(vote_counts, key=vote_counts.get)
    print(f"-------------------------\n\nWinner: {winner}\n\n-------------------------")

#Print as a text file
subdirectory = "analysis"
output_file = os.path.join('', subdirectory, "PyPoll_Results.txt")

with open(output_file, 'w') as f:
    f.write("Election Results\n-------------------------\n\n")
    f.write(f"Total Votes: {total_votes}\n\n-------------------------\n")
    for candidate, count in vote_counts.items():
        percentage = (count / total_votes) * 100
        f.write(f"{candidate}: {percentage:.3f}% ({count})\n")
    f.write(f"-------------------------\n\nWinner: {winner}\n\n-------------------------")



