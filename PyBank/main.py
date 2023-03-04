import csv
import os
from datetime import datetime

# Get the path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')
# Initialize variables
total_months = 0
total_profit_loss = 0
profit_loss_changes = []
previous_profit_loss = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Read the input file and calculate the required values
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skip the header row
    
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Calculate net total amount of profit/losses
        total_profit_loss += int(row[1])
        
        # Calculate change in profit/losses from the previous month
        if previous_profit_loss != 0:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
        
            # Determine the greatest increase in profits
            if profit_loss_change > greatest_increase_amount:
                greatest_increase_amount = profit_loss_change
                greatest_increase_date = row[0]
        
            # Determine the greatest decrease in profits
            if profit_loss_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_change
                greatest_decrease_date = row[0]
        
        previous_profit_loss = int(row[1])

# Calculate average change in profit/losses over the entire period
average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Write the results to a text file
output_path = os.path.join('financial_analysis.txt')
with open(output_path, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit_loss}\n")
    outfile.write(f"Average Change: ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print(f"Results written to file: {output_path}")    