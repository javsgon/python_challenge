# Pybank Instructions:
# Create a Python script that analyzes the PyBank records to
# calculate each of the following:
# - The total number of months included in the dataset
# - The net total amount of "Profit/Losses" over the entire period
# - The average of the changes in "Profit/Losses" over the entire period
# - The greatest increase in profits (date and amount) over the entire period
# - The greatest decrease in losses (date and amount) over the entire period
# - Print the analysis to the terminal and export a text file with the results

# import necessary modules
import os
import csv

# Path to open the file from the Resources folder
# The budget_data_csv is in the folder Resources that is in the same level
# as main.py (all in Pybank folder)
budget_csv = os.path.join('Resources', 'budget_data.csv')

# set the initial variables to 0
totalmonths = 0
total = 0

# Store the data
months = []
monthchange = []
PandL = []

# Read the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)
    # store the header
    # print(header)

    # Looping through each row in the data after the header
    for row in csvreader:
        totalmonths += 1
        total += int(row[1])
        PandL.append(row[1])
        months.append(row[0])

# set the value of the first month Profit and Loss
firstmonthPandL = int(PandL[0])

# loop in the new value of Profit and Losses to check for the changes
for i in range(1, len(PandL)):

    monthchange.append(int(PandL[i])-firstmonthPandL)
    firstmonthPandL = int(PandL[i])
    i += 1

# get the max and min increases in the data
highchange = max(monthchange)
lowchange = min(monthchange)

for i in range(len(monthchange)):
    if monthchange[i] == highchange:
        highindex = (i + 1)
    elif monthchange[i] == lowchange:
        lowindex = (i + 1)
    else:
        i += 1

# assign the index column value to a variable for printing
highmonth = months[highindex]
lowmonth = months[lowindex]

# Calculate the average change
Av_change = round((sum(monthchange)/(totalmonths-1)), 2)

# Print the analysis
print("Financial Analysis \n")
print("-------------------------------\n")
print(f"Total Months: {totalmonths}\n")
print(f"Total: $" + str(total) + "\n")
print(f"Average Change is: $" + str(Av_change) + "\n")
print(f"Greatest Increase in Profits: " + str(highmonth) +
      "  ($" + str(highchange) + ")" + "\n")
print(f"Greatest Decrease in Profits: " + str(lowmonth) +
      "  ($" + str(lowchange) + ")")

# Print to a text file
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# The text file will be saved in the Analysis folder
# I used the same logic as when opening a file with os

Financial_Analysis = os.path.join('Analysis', 'Financial_Analysis.txt')

# I used "\n" at the end of each sentence to create a new line
with open(Financial_Analysis, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-------------------------" + "\n")
    output.write(f"Total Months: {totalmonths}\n")
    output.write(f"Total: ${total}\n")
    output.write(f"Average Change: ${Av_change}\n")
    output.write(f"Greatest Increase in Profits: {highmonth} (${highchange})\n")
    output.write(f"Greatest Decrease in Profits: {lowmonth} (${lowchange})")

# End
