#PyPoll Analysis to create output to terminal and to text file

#Import OS module to allow to create file paths accross operating systems
import os

#Module for reading CSV files
import csv

csvpath=os.path.join('Resources','election_data.csv')

# Name of the output text file
output_folder = os.path.join('analysis','election_results.txt') 

column_index=2
unique_strings=set()

with open(csvpath) as csvfile, open(output_folder, "w") as output:
    # csv reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip header row
    csv_header=next(csvreader)

    #Create variable row_count excluding the header row
    row_count=0
    previous_value=0
    
    for row in csvreader:
        if len(row) > column_index:  # Check if the row has enough columns
            unique_strings.add(row[column_index])

print("List of unique strings:")
for string in unique_strings:
    print(string)

    #Print output to terminal
    print()
    print("Election Results")
    print()
    print("----------------------------------")
    print()
    print(f"Total Votes: {row_count}")
    print()
    print("----------------------------------")
    print()
    print("candidate1:23.049% (85213)")
    print()
    print("candidate1:23.049% (85213)")
    print()
    print("candidate1:23.049% (85213)")
    print()
    print("----------------------------------")
    print()
    print("Winner: max candidate")
    print()
    print("----------------------------------")

