import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join("Resources", "budget_data.csv")


# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    #print(f"CSV Header: {header}")
    
    total_month = 0
    total_profit_loss = 0
    prev_profit_loss = 0
    total_change = 0.0
    average_change = 0.0
    
    greatest_increase = 0
    greatest_decrease = 0
    
    #Print Header
    print ("Financial Analysis")
    print ("----------------------------")
    
    for row in csvreader:
        #print (f"Month: {row[0]}, Profit/Loss: {row[1]}")
        total_month += 1   
        total_profit_loss += int(row[1])

    print (f"Total Months: {total_month}")
    print (f"Total: ${total_profit_loss}")
    print (f"Average Change: ${average_change}")
    print (f"Greatest Increase in Profits: {greatest_increase}")
    print (f"Greatest Decrease in Profits: {greatest_decrease}")
    
    