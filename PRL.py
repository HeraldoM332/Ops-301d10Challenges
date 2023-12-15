# Script Name:                  Python Requests Library
# Author:                       Heraldo Morales
# Date of latest revision:      12/15/23
# Purpose:                      Performing HTTP GET requests using the requests Python library



# Imports requests library
import requests

# Prompts user to input URL for HTTP request
destination_url = input("Please enter the destination URL: ")

# Requests user to input X options for different HTTP methods
http_methods = {
    '1': requests.get,
    '2': requests.post,
    '3': requests.put,
    '4': requests.delete,
    '5': requests.head,
    '6': requests.patch,
    '7': requests.options
}

# Display available HTTP methods
print("\nAvailable HTTP Methods:")
for key, value in http_methods.items():
    print(f"{key}. {value.__name__.upper()}")

# Get user input for HTTP method
selected_option = input("Enter the number of your choice for the HTTP method: ")

# Check if the input is valid using an IF statement 
if selected_option in http_methods:
    selected_method = http_methods[selected_option]
    print(f"You've chosen {selected_method.__name__.upper()} method.")

    # Prepare the request details
    request = selected_method.__name__.upper()
    request += f" request to URL: {destination_url}"

    # Display the request to the user
    print("\nThe request about to be sent:")
    print(request)

    # Ask for confirmation
    confirm = input("Do you want to proceed? (yes/no): ").lower()

    if confirm == "yes":
        # Perform the request based on the selected method using the user-input URL
        response = selected_method(destination_url)

        # Print response header information
        print("\nResponse headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Define the status code to message mapping
        status_messages = {
            200: 'OK',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            # Add more status codes and their messages as needed
        }

        # Check if the request was successful with an IF status as well if not will give different responses accordingly
        if response.status_code in status_messages:
            print(f"\nResponse status code: {response.status_code} - {status_messages[response.status_code]}")
            print("Response content:")
            print(response.text)
        else:
            print(f"\nResponse status code: {response.status_code} - Unknown Status")
    else:
        print("Request canceled by the user.")
else:
    print("Invalid option selected.")

# Done













