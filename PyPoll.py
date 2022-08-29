    # The data we need to retrieve.
    # 1. The Total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candiate won
    # 4. The total number of votes each candiate won
    # 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

#     Print the file object.
#      print(election_data)

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     Write some data to the file.
#     txt_file.write("Hello World") """
#       Write three counties to the file.
#     txt_file.write("Arapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson")

#     Write three counties to the file.
#     txt_file.write("Arapahoe, Denver, Jefferson")

#     Write three counties to the file.
#      txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

#  # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)
#     for row in file_reader:
#         print(row[0])


