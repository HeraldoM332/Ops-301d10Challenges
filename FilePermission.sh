#!/bin/bash
# Script Name:                  File Permissions
# Author:                       Heraldo Morales
# Date of latest revision:      11/29/23
# Purpose:                      Create A Bash Script That Alters File Permissions of Everything In A Directory.

#!/bin/bash


# Overall while loop is meant to keep prompting user in case of invalid input 
# While loop that asks user to input a directory path, if true will then goto the next step is not it will repeat the instruction
while true; do
    read -p "Please Enter Path: " directory_path

    if [ -d "$directory_path" ]; then
        echo "Valid directory path entered: $directory_path"

# This part is another while loop that asks user to input a permissions number, if true then it will accept it, if not it will ask again
        while true; do
            read -p "Please Enter Permissions Number: " permission_number

            if [[ $permission_number =~ ^[0-7]{3}$ ]]; then
                echo "Valid permissions number entered: $permission_number"

                # Once Permission Number has been enter correctly it will then make it so it changes all permissions in the directory and sub directories. Displaying a successful message at the end 
                chmod -R "$permission_number" "$directory_path"

                echo "Permissions changed successfully for all files inside the directory."

                echo "Contents of $directory_path with permissions:"
                
               
                # This portion will list contents of directory and permissions using stat
                ls -l "$directory_path" | while read -r line; do
                    file=$(echo "$line" | awk '{print $9}')
                    
                    # Retrieve permissions using stat and display alongside file name
                    permissions=$(stat -c "%A" "$directory_path/$file")
                    echo "$permissions $line"
                done

                break
            else
                echo "Invalid permissions number. Please enter a valid 3-digit number."
            fi
        done

        break
    else
        echo "Invalid directory path. Please try again."
    fi
done


# Done 
