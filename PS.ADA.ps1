# Script Name:                  Powershell AD Automation
# Author:                       Heraldo Morales
# Date of latest revision:      12/116/23
# Purpose:                      Add a new user to AD

# Collect user input
$firstName = Read-Host "Enter First Name:"
$lastName = Read-Host "Enter Last Name:"
$title = Read-Host "Enter Title:"
$department = Read-Host "Enter Department:"
$company = Read-Host "Enter Company:"
$location = Read-Host "Enter Location:"

# Construct email address and UPN
$emailAddress = "$firstName@GlobeXpower.com"
$upn = "$firstName@GlobeXpower.com"

# Create a hashtable for user properties
$userProperties = @{
    Name = "$firstName $lastName"
    SamAccountName = "$firstName$lastName"
    Title = $title
    Department = $department
    Company = $company
    EmailAddress = $emailAddress
    UserPrincipalName = $upn
    Description = "$firstName $lastName is the $title at $company in $location office."
    Path = "OU=$department,OU=GlobeX USA,DC=GlobeXpower,DC=com"
    PasswordNeverExpires = $true
}

# Create new user using New-ADUser cmdlet and the hashtable
New-ADUser @userProperties

# Optional: Display confirmation message
Write-Host "User $firstName $lastName created successfully!"
