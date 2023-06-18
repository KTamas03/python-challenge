#PyBank Analysis to create output to terminal and to text file

#Import OS module to allow to create file paths accross operating systems
import os

#Import csv Module for reading CSV files
import csv

#source file and location in network folder
csvpath=os.path.join('Resources','budget_data.csv')

#Name of the output text file and location in network folder
output_folder = os.path.join('analysis','financial_analysis.txt') 

with open(csvpath) as csvfile, open(output_folder, "w") as output:
    # csv reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip header row
    csv_header=next(csvreader)

    row_count=0             #to count rows excluding the header row
    total_sum=0             #sum up profit/losses
    previous_value=0        #previous value in column
    change_list=[]          #list to store change in values from one month to the next
    max_increase=0          #to calculate the greatest increase in profits
    max_increase_month=""   #to return the month with the greatest increase in profits
    max_decrease=0          #to calculate the greatest decrease in profits  
    max_decrease_month=""   #to return the month with the greatest decrease in profits

    for row in csvreader:
    #increment row count for each row processed
        row_count=row_count+1

    #exclude header row from sum calculation
        if row_count>0:
            #convert the value in column B to an integer and add it to the total sum
            total_sum= total_sum+int(row[1])
        total_sum_format="${}".format(total_sum)

    # Calculate the change from the previous value
        change = int(row[1]) - previous_value
        change_list.append(change)      #append each change calc for each row of data to change_list

        # Update the previous value for the next iteration
        previous_value = int(row[1])

        # Check if the change is the greatest increase or greatest decrease
        if change > max_increase:
            max_increase = change
            max_increase_format="${}".format(max_increase)
            max_increase_month=row[0]
        previous_value=int(row[1])

        if change < max_decrease:
            max_decrease = change
            max_decrease_format="${}".format(max_decrease)
            max_decrease_month=row[0]
        previous_value=int(row[1])

    #delete first item in change_list using pop
    #don't want the first difference as it is row 2 minus the header row
    #keeping it in distorts the average_change result   
    change_list.pop(0)
    
    # Calculate the average change
    average_change = sum(change_list) / (row_count-1)
    average_change_format="${:.2f}".format(average_change)

    #Print output to terminal
    print()
    print("Financial Analysis")
    print()
    print("----------------------------------")
    print()
    print(f"Total Months: {row_count}")
    print()
    print(f"Total: {total_sum_format}")
    print()
    print(f"Average Change:{average_change_format} ")
    print()
    print(f"Greatest Increase in Profits: {max_increase_month} ({max_increase_format}) ")
    print()
    print(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_format}) ")

    #Print output to "financial analysis.txt" file
    output.write("Financial Analysis\n")
    output.write("\n")
    output.write("----------------------------------\n")
    output.write("\n")
    output.write(f"Total Months: {row_count}\n")
    output.write("\n")
    output.write(f"Total: {total_sum_format}\n")
    output.write("\n")
    output.write(f"Average Change: {average_change_format}\n")
    output.write("\n")
    output.write(f"Greatest Increase in Profits: {max_increase_month} ({max_increase_format})\n")
    output.write("\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_format})\n")