import os
import csv

# Establish data input file and output. 
budget_data_csv = os.path.join("budget_data.csv")
budget_analysis_txt = os.path.join("budget_analysis.txt")

# Read the CSV and convert it into a list of dictionaries.
        # Open the csv file with open; then open the csv file wit csv.reader:
with open(budget_data_csv) as budget_data:
    reader = csv.reader(budget_data)

    # Read the header row
    header = next(reader)

    # Print header
    print(header)

    # Initialize a variable called total_months (count of all month values in the CSV)
    total_months = 0 

    # Count total number of months in the data sets. Also the unique values in first column after the header.
    total_months = len(list(budget_data)).unique()

    print('total_months is:', total_months)

    # Initialize a variable called net_total (sum of all positive/negative 'profit/loss' values in the CSV)
    net_total = 0

    #Run a For Loop that will constantly add each row's profit/loss value to net_total
    for row in reader:
        # Row [1] is the 'Profit/Loss' value which is a string. Thus this needs a conversion into an integer. Use int(), which converts whatever is passed into it into an integer.
        print(row)
        net_total = net_total + int(row[1])

    print('net_total is:', net_total)



    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Define the function as "Print Analysis". Have it accept "budget_data" as its sole parameter
    def print_analysis(budget_data):

        # For readability, assign values to variables with descriptive names
        date = str(budget_data[0])
        profit = int(budget_data[1])

        # Total number of months in the dataset. Count the rows in Column 1 (**but how to know they aren't duplicates?):
        totalMonths = len(list(budget_data)).unique()

        # Net total of profits and losses (sum of numbers in column B, aka "2")
        totalNet = total += int(row[2])
        prevRow = [0,0]

        # Changes in profits and losses over period, while rows exist in the csv (From row i to end):
        for row in csvreader:
            percentChange = (((row[1] + 1 profit) - (row i profit)) / (row i profit)) * 100
            
            print list of values = percentChangeList

        # Calculate average change
        averageChange = percentChangeList * (totalMonths - 1)

        # Print out the data points of interest as the final budget analysis:
        print("Financial Analysis")
        print("-------------------")
        print(f"Total Months:" {totalMonths})
        print(f"Total:" {str(totalNet)})
        print(f"Average Change:" {str(averageChange)})
        print(f"Greatest Increase in Profits:" {str(increaseProfits)}) - GREATEST VALUE IN PERCENTCHANGEALL LIST
        print(f"Greatest Decrease in Profits:" {str(decreaseProfits)}) - LOWEST VALUE IN PERCENTCHANGEALL LIST

# Expected: prints to screen and txt file.

