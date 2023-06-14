#PyBank Analysis to create output to terminal and to text file

#Import OS module to allow to create file paths accross operating systems
import os

#Module for reading CSV files
import csv

csvpath=os.path.join('Resources','budget_data.csv')

# Name of the output text file
output_folder = os.path.join('analysis','financial_analysis.txt') 

with open(csvpath) as csvfile, open(output_folder, "w") as output:
    # csv reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip header row
    csv_header=next(csvreader)

    #Create variable row_count excluding the header row
    row_count=0
    total_sum=0
    previous_value=0
    change_list=[]
    max_increase=0
    max_increase_month=""
    max_decrease=0
    max_decrease_month=""

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
        change_list.append(change)

        # Update the previous value for the next iteration
        previous_value = int(row[1])
        #print(change_list)
        
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

    # Calculate the average change
    average_change = sum(change_list) / (row_count)
    average_change_format="${:,.2f}".format(average_change)

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