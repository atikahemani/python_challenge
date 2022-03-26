

# reading in the budget_data.csv file

#import packages needed to read csv file
from calendar import c
import os
import csv
print(os.path.abspath('.'))

csvpath = os.path.join('', 'Resources', 'election_data.csv')




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidates = {}
    total_votes=0
    most_votes=0
    votes=0



    for row in csvreader:
        candidate_name=row[2]
        total_votes+=1

        if candidate_name in candidates.keys():
            candidates[candidate_name] +=1
        else:
            candidates[candidate_name]=1

    for candidate_name in candidates:

        percent_of_votes = (candidates[candidate_name])/(total_votes) * 100
        #print(f"{candidate_name}: {int(percent_of_votes)}% {total_votes}")
        
        if candidates[candidate_name] > most_votes:
            most_voted=candidate_name
            most_votes=candidates[candidate_name]

print(candidates)
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
for candidate_name in candidates:
    percent_of_votes = (candidates[candidate_name])/(total_votes) * 100
    print(f"{candidate_name}: {int(percent_of_votes)}% {list(candidates.values())}")
print("-------------------------------")
print(f"Winner: {most_voted}")
        
#with open('election_results.txt', 'w') as text:
    #text.write("Election Results\n")
    #text.write("-------------------------------\n")
    #text.write(f"Total Votes: {total_votes}\n")
    #text.write("-------------------------------\n")
    #for candidate_name in candidates:
        #percent_of_votes = (candidates[candidate_name])/(total_votes) * 100
        #text.write(f"{candidate_name}: {int(percent_of_votes)}% {total_votes}\n")
   # text.write("-------------------------------\n")
    #text.write(f"Winner: {most_voted}\n")
