#Import modules and define the CSV we want to read
import os
import csv

csvpath = r"C:\Users\grant\Desktop\python-challenge\PyBank\Resources\budget_data.csv"

#Initialize the counter variables
month_count = 0
total_PL = 0
prev_month = 0
monthly_changes = []

#Read the CSV file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #Iterate through the rows to find total months, total P&L, and to populate the monthly_change list
    for row in csvreader:
        month_count = month_count + 1
        total_PL = total_PL + int(row[1])

        month_value = int(row[1])
        monthly_change = month_value - prev_month
        monthly_changes.append(monthly_change)
        prev_month = month_value

    #Find the average MoM P&L change and the min/max P&L values
    average_change_PL = sum(monthly_changes[1:]) / (month_count - 1)
    
    max_PL = max(monthly_changes)
    max_PL_row = monthly_changes.index(max_PL)

    min_PL = min(monthly_changes)
    min_PL_row = monthly_changes.index(min_PL)

    #Go back to the top of the CSV file and skip the header
    csvfile.seek(0)
    next(csvreader)

    #Go through the CSV and find the row that has the max/min P&L
    for i, row in enumerate(csvreader):
        if i == max_PL_row:
            max_PL_month = row[0]
        elif i == min_PL_row:
            min_PL_month = row[0]

    #Print Everything
    print('')
    print("Financial Analysis \n--------------------------------\n")   
    print(f"Total Months: {month_count}\n")
    print(f"Total P&L: ${total_PL}\n")
    print(f"Average Change: ${average_change_PL: .2f}\n")
    print(f"Greatest Increase in Profits: {max_PL_month} (${max_PL})\n")
    print(f"Greatest Decrease in Profits: {min_PL_month} (${min_PL})")

#Print as a text file
subdirectory = "analysis"
output_file = os.path.join('', subdirectory, "PyBank_Results.txt")

with open(output_file, 'w') as f:
    f.write("Financial Analysis \n--------------------------------\n")
    f.write(f"Total Months: {month_count}\n")
    f.write(f"Total P&L: ${total_PL}\n")
    f.write(f"Average Change: ${average_change_PL: .2f}\n")
    f.write(f"Greatest Increase in Profits: {max_PL_month} (${max_PL})\n")
    f.write(f"Greatest Decrease in Profits: {min_PL_month} (${min_PL})")



    


    


    
    
    
    

