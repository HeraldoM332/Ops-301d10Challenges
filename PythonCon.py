# Script Name:                  Python Conditional
# Author:                       Heraldo Morales
# Date of latest revision:      12/07/23
# Purpose:                      Using “if statements” in Python.



# Assuming a and b are predefined variables
a = 10
b = 5

# If Statement: Checks if a is equal to b. If true, it prints "a is equal to b".
if a == b:
    print("a is equal to b")
# These elif (else if) conditions are checked sequentially if the preceding conditions are not met.  
# Checks if a is not equal to b. If true, it prints "a is not equal to b".
elif a != b:
    print("a is not equal to b")
# Checks if a is less than b. If true, it prints "a is less than b".  
elif a < b:
    print("a is less than b")
# Checks if a is less than or equal to b. If true, it prints "a is less than or equal to b".   
elif a <= b:
    print("a is less than or equal to b")
# Checks if a is greater than b. If true, it prints "a is greater than b"   
elif a > b:
    print("a is greater than b")
# Checks if a is greater than or equal to b. If true, it prints "a is greater than or equal to b".   
elif a >= b:
    print("a is greater than or equal to b")
# else Block: If none of the conditions (if or elif) are true, this block executes and prints "None of the conditions are met".    
else:
    print("None of the conditions are met")



# Done