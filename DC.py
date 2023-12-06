# Script Name:                  Directory Creation
# Author:                       Heraldo Morales
# Date of latest revision:      12/05/23
# Purpose:                      Create a Python script that utilizes a function from the os library to generate directory information.







# Imports the OS Library
import os


# Defines the function Process Directory using User_path as a parameter

def process_directory(user_path):

    # Check if the provided path exists and is a directory
    if os.path.exists(user_path) and os.path.isdir(user_path):

        # Walk through the directory tree
        for root, directories, files in os.walk(user_path):
            print(f"Current directory: {root}")
            print(f"Directories: {directories}")
            print(f"Files: {files}")

# If path is not found will say the following:             
    else:
        print("The provided path is not a valid directory.")

# Asks user to input a directory path
user_input = input("Enter the directory path: ")

# Calls process_directory with the user-provided path
process_directory(user_input)

# Done 

