

#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
#Financial Analysis
#--------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Read in CSV #
# Store the Header Row
# Print To terminal

import os
import csv
csvpath = os.path.join('budget_data.csv')
# Create lists to store the values   
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    total_months =[]
    net_profit =[]
    average_changes_in_profit = [] 
#loop through the csv and add them to the lists
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
#cast you string to an integer as csv is all strings
    for i in range(len(net_profit)-1):
        average_changes_in_profit.append(net_profit[i+1]-net_profit[i])

#Query the greatest increase and greatest decrease from my list    

greatest_increase = max(average_changes_in_profit)
greatest_decrease = min(average_changes_in_profit)

#using index() method to map month greatest increase and greatest decrease happened. +1 for header

greatest_increase_month = average_changes_in_profit.index(greatest_increase)+1
greatest_decrease_month = average_changes_in_profit.index(greatest_decrease)+1

#print everything
#print(f"CSV Header:{csv_header}")

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total Profit: ${sum(net_profit)}")
print(f"Average Changes in Profit: ${round(sum(average_changes_in_profit)/len(average_changes_in_profit))}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} ${(str(greatest_increase))}")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} ${(str(greatest_decrease))}")

#Once printing is working export to .txt and test
output = os.path.join('output.txt')
with open(output, "w") as newtextfile:
    newtextfile.write("Financial Analysis")
    newtextfile.write("\n")
    newtextfile.write("------------------------")
    newtextfile.write("\n")
    newtextfile.write(f"Total Months:{len(total_months)}")
    newtextfile.write("\n")
    newtextfile.write(f"Total: ${sum(net_profit)}")
    newtextfile.write("\n")
    newtextfile.write(f"Average Change: ${round(sum(average_changes_in_profit)/len(average_changes_in_profit),2)}")
    newtextfile.write("\n")
    newtextfile.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} ${(str(greatest_increase))}")
    newtextfile.write("\n")
    newtextfile.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} ${(str(greatest_decrease))}")





