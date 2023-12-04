# Script Name:                  Bash in python
# Author:                       Heraldo Morales
# Date of latest revision:      12/04/23
# Purpose:                      Execute a Linux terminal commands from within a Python script.


#Variable

User = "Heraldo"

#Displays user name in Terminal

print("User:", User)

# Imports OS and Subprocess Module

import os 
import subprocess

# Bash in Python

os.system("ls -la") 
os.system("ip a")

# Execute 'whoami' command and store the output in the variable 'name'

name = os.popen('whoami').read().strip()

# Display the result
print("Username:", name)


# Run the 'lshw -short' command
result = subprocess.run(['lshw', '-short'], capture_output=True, text=True)

# Check if the command executed successfully
if result.returncode == 0:
    # Display the output
    print(result.stdout)
else:
    # Display an error message if the command failed
    print("Error executing command")

# Done
    