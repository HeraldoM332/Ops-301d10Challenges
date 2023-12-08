# Script Name:                  Python File Handling
# Author:                       Heraldo Morales
# Date of latest revision:      12/08/23
# Purpose:                      Open and manipulate an existing file.   







# Opens txt. file and if it doesn't exost creates one and appends 3 lines of file
with open('example.txt', 'a') as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Reads and prints the first line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)

# Deletes example .txt if it exists, if completed prints file deleted and if it doesn't says tje file does not exist
import os
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File deleted.")
else:
    print("The file does not exist.")

# Done

