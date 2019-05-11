import csv
import os

# Files to load and output
budget_data = "budget_data.csv"
budget_analysis = "budget_analysis.txt"

# Read the csv and convert it into a list of dictionaries    
with open(budget_data) as budget_data:
    reader = csv.reader(budget_data)

    # Read the header row
    header = next(reader)    
    
    # Initialize a variable called total_months (the count of all month values in the CSV)
    total_months = 1
    
    # First row advances the reader by one line. Without this, the first % change calculation will have 0 as divisor, generating an error. 
    first_row = next(reader)
    
    # Initialize a variable called net_total (the sum of all postive/negative 'profit/loss' values in the CSV)
    net_total = int(first_row[1])

    # Initialize a variable for "previous row".
    previous_row = int(first_row[1])

    # Define list called Net Change list
    net_change_list = []
    
    # Calculate net total of profits and losses. Note: row[1] is the 'Profit/Loss' value, and it is a STRING, thus needing a conversion. int() converts whatever is passed into to an integer
    for row in reader:
        net_total = net_total + int(row[1]) 
    
    # Count total number of months in the data sets. Also the unique values in first column after the header. 
        total_months = total_months + 1

    # Calculate changes in profits/losses over period. First track the net change. Keep moving "previous row" forward.
        net_change = int(row[1]) - previous_row
        previous_row = int(row[1])
        net_change_list = net_change_list + [net_change]

# Calculate average percent change
    averageChange = sum(net_change_list) / len(net_change_list)

# From your net_change_list, find the largest value and date of the largest value. Same for smallest value and month.
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)

# Print out the data points of interest as the final budget analysis
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: ", {total_months})
    print("Total: ", {net_total})
    print("Average Change: ", {averageChange})
    print("Greatest Increase in Profits: ", {greatest_increase})
    print("Greatest Decrease in Profits: ", {greatest_decrease})

# Specify the file to write to
output_path = os.path.join("budget_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    txtwriter = csv.writer(txtfile, delimiter=' ', escapechar = " ", quoting = csv.QUOTE_NONE)

    # Write the first line
    txtwriter.writerow(["Financial Analysis"])
    # Write the second line
    txtwriter.writerow(["-------------------"])
    # Write the third line
    txtwriter.writerow(["Total Months: ", {total_months}])
    # Write the fourth line
    txtwriter.writerow(["Total: ", {net_total}])
    # Write the fifth line
    txtwriter.writerow(["Average Change: ", {averageChange}])
    # Write the sixth line
    txtwriter.writerow(["Greatest Increase in Profits: ", {greatest_increase}])
    # Write the seventh line
    txtwriter.writerow(["Greatest Decrease in Profits: ", {greatest_decrease}])