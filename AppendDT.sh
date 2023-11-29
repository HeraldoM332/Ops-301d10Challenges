#!/bin/bash 
# Script Name:                  Append: Date & Time
# Author:                       Heraldo Morales
# Date of latest revision:      11/28/23
# Purpose:                      Copies /var/log/syslog to the current working directory/ Appeds the current date and time to fn


# Declaration of variables
timestamp=$(date +%Y%m%d-%H%M%S)
syslog_file="/var/log/syslog"
copied_file="syslog_$timestamp"

# Copy syslog to the current directory
cp "$syslog_file" "$copied_file"

# End, the script has successfully copied the syslog file to the current directory
# and renamed it to include the current date and time in the filename.

