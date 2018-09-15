import os
import csv

total_votes = 0

candidate_list = []
candidate_total_data = []

# Path to collect data from the Resources folder
electionCSV = os.path.join("Resources", "election_data.csv")

# Read in the CSV file
with open(electionCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate_list.append(row[2])

    csvfile.close

candidate_list.sort()
candidate_set = set(candidate_list)
sorted_candidate_set = sorted(candidate_set)

#Counting total each candidate
for candidate in candidate_set:
    vote_count = candidate_list.count(candidate)
    candidate_tuple = candidate, vote_count, vote_count/total_votes*100
#    print(candidate_tuple)
    candidate_total_data.append(candidate_tuple)

winner = max(candidate_total_data,key=lambda item:item[1])[0]

# -------- Print Result -------- 
header = "Election Results"
dashes = "-------------------------" 
total_votes_txt = "Total Votes: " + str(total_votes)
winner_txt = "Winner: " + winner

print(header)
print(dashes)
print(total_votes_txt)
print(dashes)
for cand_tuple in candidate_total_data:
    print(cand_tuple[0] + ": " + str( "{:2.3f}".format(cand_tuple[2]))  + "% (" + str(cand_tuple[1]) + ")")

print(dashes)
print(winner_txt)
print(dashes)
    
# -------- Write Result to file-------- 
with open("PyPoll.txt","w") as txtfile:
    txtfile.write(header + "\n") 
    txtfile.write(dashes + "\n") 
    txtfile.write(total_votes_txt  + "\n") 
    txtfile.write(dashes + "\n") 
    
    for cand_tuple in candidate_total_data:
        txtfile.write(cand_tuple[0] + ": " + str( "{:2.3f}".format(cand_tuple[2]))  + "% (" + str(cand_tuple[1]) + ")\n")

    txtfile.write(dashes + "\n") 
    txtfile.write(winner_txt  + "\n") 
    txtfile.write(dashes + "\n") 
 
    txtfile.close()

