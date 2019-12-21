import os
import csv
Python_election_data_csv = os.path.join('..', 'election_homework', 'Python_election_data.csv')
candidates = {}

total_votes = 0
vote_percent = 0.0 

with open(Python_election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:  
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1

        else:
            candidates[candidate] = 0
        total_votes = total_votes + 1 

    print("------------------------------")
    print("Election Results")
    print("------------------------------")
    print("total votes" + " " + str(total_votes))

    winner_vote = 0

    for i, num in candidates.items():
        candidate_votes = candidates[i]
        vote_percent = (round(100.0 * candidate_votes/total_votes,2))
        print(i + ": " + str(num) + ": " + "%" + str(vote_percent))

        if candidate_votes > winner_vote:
            winner_vote = candidate_votes
            winner = i
    print("------------------------------")
    print("The winner is..." + winner)
    print("------------------------------")