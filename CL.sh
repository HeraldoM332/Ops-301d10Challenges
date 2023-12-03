#!/bin/bash
# Script Name:                  Clearing Logs
# Author:                       Heraldo Morales
# Date of latest revision:      12/03/23
# Purpose:                      Clears log files for you


# Timestap is given with this command
timestamp=$(date '+%Y%m%d%H%M%S')


# Prints title that is being perfomed and then displays /var/log/syslog and /var/log/wtmp
# Print file sizes before compression
echo "File sizes before compression:"
sudo du -h /var/log/syslog
sudo du -h /var/log/wtmp


# Stores path to backup directory where log files are archived
# Define backup directory
backup_dir="/home/desktop/Backuptest"  

# Uses tar to create a compresshed archive and saves with timestap fn in backup directory
# Create the backup directory with appropriate permissions
sudo mkdir -p "$backup_dir"
sudo chmod 755 "$backup_dir"  # Adjust permissions as necessary

# Compress log files to backup directory
sudo tar -czvf "$backup_dir/syslog-$timestamp.tar.gz" -C / /var/log/syslog /var/log/wtmp

# Clear the contents of the log files with appropriate permissions
sudo sh -c 'echo > /var/log/syslog'
sudo sh -c 'echo > /var/log/wtmp'
sudo chmod 644 /var/log/syslog /var/log/wtmp  # Example: Set permissions to read-write for owner, read-only for group and others

# Print file size after compression
echo "File size after compression:"
sudo du -h "$backup_dir/syslog-$timestamp.tar.gz"


# Uses ls -1h to display information for original log and created archive
# Compare sizes of original and compressed files
echo "Comparison of file sizes:"
echo "Original syslog size:"
ls -lh /var/log/syslog
echo "Original wtmp size:"
ls -lh /var/log/wtmp
echo "Compressed syslog size:"
ls -lh "$backup_dir/syslog-$timestamp.tar.gz"



# Done






