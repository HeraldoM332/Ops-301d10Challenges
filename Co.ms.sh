#!/bin/bash
# Script Name:                  Conditionals in Menu Systems
# Author:                       Heraldo Morales
# Date of latest revision:      11/30/23
# Purpose:                      Conditionals are highly useful in evaluating user input, and thereby letting us setup responsive menu systems in our tooling.



# The function provided is what displays the main menu
# Contains a while loop that makes the Main Menu Display continuously until said otherwise
function show_main_menu() {
    while true; do

    # PS3 Variable allows users to Select
        PS3='Please enter your choice: '
        options=("Hello World!" "Ping Self" "IP info" "Exit")

        # Select allows user to choose from "Hello World, Ping Self, IP info and Exit"

        # The loops contained within allow users to select option and bring them to the option chosen, simultaneously it will also send user back to main menu after option is completed.
        select opt in "${options[@]}"
        do
            case $opt in
                "Hello World!")
                    echo "Hello World!"
                    break  # Break out of the case block and return to main menu
                    ;;
                "Ping Self")
                    echo "Pinging Self..."
                    ping -c 1 127.0.0.1 >/dev/null  # Ping the loopback address

                    # Contains and if statement where if ping is prodused correctly it will say successful if not it will sau failed
                    # Check the ping exit status using $?
                    if [ $? -eq 0 ]; then
                        echo "Ping successful!"
                    else
                        echo "Ping failed!"
                    fi
                    break  # Break out of the case block and return to main menu
                    ;;
                "IP info")
                    echo "Displaying IP information..."
                    # Use ip command to show network interfaces and their configurations
                    ip addr show
                    break  # Break out of the case block and return to main menu
                    ;;
                "Exit")

                # Return allows user to break out of loop and exit Main Menu entirely 
                    return 0  # Return 0 to exit the function and loop
                    ;;
                *) 
                    echo "Invalid option $REPLY"
                    ;;
            esac
        done
    done
}
# This part brings the user back to the Main Menu if Exit is not chosen
# Call the function to start the main menu
show_main_menu
# When user Exits, it will display this
echo "Exiting script"


# Done
