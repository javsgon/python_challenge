# Pypoll Instructions
# Create a Python script that analyzes the votes and calculates
# each of the following values:
# - The total number of votes cast
# - A complete list of candidates who received votes
# - The percentage of votes each candidate won
# - The total number of votes each candidate won
# - The winner of the election based on popular vote
# - final script should both print the analysis to the terminal
# and export a text file with the results.

# import necessary modules
import os
import csv

# Path to open the file from the Resources folder
# The election_data_csv is in the folder Resources that is in the same level
# as main.py (all in Pybank folder)
election_csv = os.path.join('Resources', 'election_data.csv')

# setup the initial variables
votescast = 0
votespercentage = 0
winnervotecount = 0

# save the info
listcandidates = []
candidatevotecount = {}

# Read the csv file as we saw in the class
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip the header row
    header = next(csvreader)

# Looping through each row in the data after the header to get the total votes
    for row in csvreader:
        votescast += 1

        # Get the candidate name in column 3 from each row
        candidatename = (row[2])

        if candidatename not in listcandidates:
            listcandidates.append(candidatename)

            # Count each candidate's votes
            candidatevotecount[candidatename] = 0

        # Add a vote to the candidate's count
        candidatevotecount[candidatename] += 1

    # save the total vote results and print with f string
    # https://docs.python.org/3/tutorial/inputoutput.html
    results = (
        f"Election Results\n"
        f"-------------------------------\n"
        f"Total Votes: {votescast}\n"
        f"-------------------------------\n")
    print(results)  # to terminal

    candidatesfinals = []
    # Calculate the percentage of votes for each candidate with the loop
    for candidatename in candidatevotecount:

        # Retrieve vote count and percentage with 3 decimals
        votesbycandidate = candidatevotecount[candidatename]

        votespercentage = round(
            (float(votesbycandidate) / float(votescast) * 100), 3)

        # print with f string
        # https://docs.python.org/3/tutorial/inputoutput.html
        final_results = (
            f"{candidatename}: {votespercentage}% ({votesbycandidate})\n")
        print(final_results)  # to terminal
        candidatesfinals.append(final_results)

        # Determine the winner
        if votesbycandidate > winnervotecount:
            winnervotecount = votesbycandidate
            winnername = candidatename
            winnerpercentage = votespercentage
    # save the election winner and print with f string
    # https://docs.python.org/3/tutorial/inputoutput.html
    electionwinner = (
        f"-------------------------------\n"
        f"Winner: {winnername}\n"
        f"-------------------------------\n")
    print(electionwinner)  # to terminal

# this loop will store the final results in candidatesfinals
# and add the names of the candidates,votes percentage and votes by candidate
summary = ""
for value in candidatesfinals:
    summary += value

# Print to a text file
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# The text file will be saved in the Analysis folder

# I used the some logic to open but now to write the file using "os" and "with open"
Elections_Results = os.path.join('Analysis', 'Elections_Results.txt')

with open(Elections_Results, 'w') as output:
    output.write(results)
    output.write(summary)
    output.write(electionwinner)

# End
