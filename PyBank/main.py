import os
import csv

total_month = 0
total_profit_loss = 0
prev_profit_loss = 0
total_change = 0.0
average_change = 0.0

diff_list = []

# Path to collect data from the Resources folder
budgetCSV = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:

        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss
        diff_profit_loss = 0
        
        if total_month > 0:
            diff_profit_loss = current_profit_loss - prev_profit_loss
            
            #Put the diffrencein list of tuples
            diff_tuple = row[0], diff_profit_loss
            diff_list.append(diff_tuple)


        total_month += 1
        prev_profit_loss = current_profit_loss

    csvfile.close

#Finding Average 
for i in range(len(diff_list)):
    total_change += diff_list[i][1]

average_change = total_change/len(diff_list)

#Finding Greatest Increase or Decrease in Profits  
greatest_increase = max(diff_list,key=lambda item:item[1])[1]
greatest_increase_date = max(diff_list,key=lambda item:item[1])[0]

greatest_decrease = min(diff_list,key=lambda item:item[1])[1]
greatest_decrease_date = min(diff_list,key=lambda item:item[1])[0]

# -------- Print Result -------- 
header = "Financial Analysis\n----------------------------" 
total_month_txt = "Total Months: " + str(total_month)
total_txt = "Total: $" +  str(total_profit_loss)
average_change_txt = "Average Change: $" +  str(round(average_change, 2))
greatest_increase_txt = "Greatest Increase in Profits:  " + greatest_increase_date + " ($" + str(greatest_increase) + ")" 
greatest_decrease_txt = "Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")" 

print (header)
print (total_month_txt)
print (total_txt)
print (average_change_txt)
print (greatest_increase_txt)
print (greatest_decrease_txt)
    
# -------- Write Result to file-------- 
with open("PyBank.txt","w") as txtfile:
    txtfile.write(header + "\n") 
    txtfile.write(total_month_txt  + "\n") 
    txtfile.write(total_txt  + "\n") 
    txtfile.write(average_change_txt  + "\n") 
    txtfile.write(greatest_increase_txt  + "\n") 
    txtfile.write(greatest_decrease_txt  + "\n") 
 
    txtfile.close()
