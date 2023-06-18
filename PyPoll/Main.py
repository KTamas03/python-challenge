#PyPoll Analysis to create output to terminal and to text file

import os                                                           #import OS module to allow to create file paths accross operating systems
import csv                                                          #import csv module for reading CSV files

csvpath=os.path.join('Resources','election_data.csv')               #source file and location in network folder

output_folder = os.path.join('analysis','election_results.txt')     #name of the output text file and location in network folder 

with open(csvpath) as csvfile, open(output_folder, "w") as output:
    csvreader=csv.reader(csvfile,delimiter=',')                     #csv reader specifies delimiter and variable that holds contents
    csv_header=next(csvreader)                                      #skip header row

    row_count=0                                                     #create variable row_count excluding the header row
    vote_counts={}                                                  #create empty library to add count of votes per candidate
    
    for row in csvreader:
        row_count = row_count + 1                                   #increment row count for each row processed
        candidate = row[2]                                          #column C in cvs file holds candidate names
    
        if candidate in vote_counts:
            vote_counts[candidate] = vote_counts[candidate] + 1     #increment vote count for each vote processed by candidate
        else:
            vote_counts[candidate]= 1
    
    #print output to terminal
    print()
    print("Election Results")
    print()
    print("----------------------------------")
    print()
    print(f"Total Votes: {row_count}")                              #print total votes counted in csv file
    print()
    print("----------------------------------")
    print()

    #following 2 variables created to keep track of the candidate with the maximum votes
    max_votes=0
    winner=""

    for candidate, count in vote_counts.items():                    #print the vote counts for all the candidates listed in col C of cvs file
        percentage=(count/row_count)*100                            #percentage of votes by candidate
        print()
        print(f"{candidate}: {percentage:.3f}%, ({count})")         #print candidate name, % of votes won to 3 decimals and count of votes
        print()

        if count > max_votes:                                       # calculate which candidate has the most votes
            max_votes = count     
            winner = candidate
    print("----------------------------------")
    print()
    print(f"Winner: {winner}")                                      #winner's name is printed based on rows 52 to 54
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