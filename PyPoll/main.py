# Reading / Processing CSV
import csv
import os

# Files to load and output
election_data = "election_data.csv"
election_analysis = "election_analysis.txt"
candidate_name_list = []

# STEP1: Read the csv 
with open(election_data) as election_data:
    reader = csv.reader(election_data)

    # Read the header row
    header = next(reader)    

    # Initialize a variable called total_votes (to count of all voter IDs in the CSV)
    total_votes = 0 

    # Create list(space) for collecting unique_name & every single name in csv file
    unique_candidate_list = []
    candidate_name_list = []

    # STEP 2: Open 'for loop' for analysis. 
    for row in reader:
        # Count total number of votes cast by tallying number of voter IDs in the data set.
        total_votes = total_votes + 1

        # To count all of the unique values in column C, loop through the reader and add candidate value to list if new. 
        name = row[2]

        # STEP 3: Collect every single name & unique name
        candidate_name_list.append(name)

        # Create if statement to add candidate name if NOT already in the candidate list
        if name not in unique_candidate_list:
            unique_candidate_list.append(name)

# Count total votes per candidate
total_khan = (candidate_name_list.count(unique_candidate_list[0]))
total_correy = (candidate_name_list.count(unique_candidate_list[1]))
total_li = (candidate_name_list.count(unique_candidate_list[2]))
total_otooley = (candidate_name_list.count(unique_candidate_list[3]))

# Count votes per candidate over total votes. Format into % at the end (when you print)
p_khan = total_khan / total_votes 
p_correy = total_correy / total_votes
p_li = total_li / total_votes
p_otooley = total_otooley / total_votes

# Create a list of all totals to find the winner. Find the index of the largest value.
total_votes_by_candidate = [total_khan, total_correy, total_li, total_otooley]
max_value = max(total_votes_by_candidate)
index_max = total_votes_by_candidate.index(max_value)

print("Election Results")
print("-------------------")
print("Total Votes: ", total_votes)
print("-------------------")
print(f"Khan: {p_khan:.2%} {total_khan}")
print(f"Correy: {p_correy:.2%} {total_correy}")
print(f"Li: {p_li:.2%} {total_li}")
print(f"O'Tooley: {p_otooley:.2%} {total_otooley}")
print("-------------------")
print(f"Winner: {unique_candidate_list[index_max]}" )
print("-------------------")

# Specify the file to write to
output_path = os.path.join("election_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    txtwriter = csv.writer(txtfile, delimiter=' ', escapechar = " ", quoting = csv.QUOTE_NONE)

    # Write the first line
    txtwriter.writerow(["Election Results"])
    # Write the second line
    txtwriter.writerow(["-------------------"])
    txtwriter.writerow(["Total Votes: ", total_votes])
    txtwriter.writerow(["-------------------"])
    txtwriter.writerow([f"Khan: {p_khan:.2%} {total_khan}"])
    txtwriter.writerow([f"Correy: {p_correy:.2%} {total_correy}"])
    txtwriter.writerow([f"Li: {p_li:.2%} {total_li}"])
    txtwriter.writerow([f"O'Tooley: {p_otooley:.2%} {total_otooley}"])
    txtwriter.writerow(["-------------------"])
    txtwriter.writerow([f"Winner: {unique_candidate_list[index_max]}"])
    txtwriter.writerow(["-------------------"])
