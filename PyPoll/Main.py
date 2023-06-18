#PyPoll Analysis to create output to terminal and to text file

#Import OS module to allow to create file paths accross operating systems
import os

#Module for reading CSV files
import csv

#source file and location in network folder
csvpath=os.path.join('Resources','election_data.csv')

#Name of the output text file and location in network folder
output_folder = os.path.join('analysis','election_results.txt') 

with open(csvpath) as csvfile, open(output_folder, "w") as output:
    # csv reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip header row
    csv_header=next(csvreader)

    #Create variable row_count excluding the header row
    row_count=0
    vote_counts={}  #create empty library to add count of votes per candidate
    
    for row in csvreader:
        row_count=row_count+1   #increment row count for each row processed
        candidate = row[2]      #column C is Candidate Names
    
        if candidate in vote_counts:
            vote_counts[candidate] = vote_counts[candidate] + 1
        else:
            vote_counts[candidate]=1
    
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

    max_votes=0
    winner=""

    for candidate, count in vote_counts.items(): # Print the vote counts per candidate
        percentage=(count/row_count)*100
        print()
        print(f"{candidate}: {percentage:.3f}%, ({count})")
        print()


        if count > max_votes:
            max_votes = count
            winner = candidate
    print("----------------------------------")
    print()
    print(f"Winner: {winner}")
    print()
    print("----------------------------------")

    #Print output to "election_results.txt" file
    output.write("Election Results\n")
    output.write("\n")
    output.write("----------------------------------\n")
    output.write("\n")
    output.write(f"Total Votes: {row_count}\n")
    output.write("\n")
    output.write("----------------------------------\n")
        
    for candidate, count in vote_counts.items():
        percentage = (count / row_count) * 100

        output.write("\n")
        output.write(f"{candidate}: {percentage:.3f}%, ({count})\n")
        output.write("\n")
        
    output.write("----------------------------------\n")
    output.write("\n")
    output.write(f"Winner: {winner}\n")
    output.write("\n")
    output.write("----------------------------------\n")
