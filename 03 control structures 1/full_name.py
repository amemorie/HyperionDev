"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T03 - Beginner Control Structures - If, Elif, Else & the Boolean 
    Data type

Compulsory Task 1: 
Validate that a user inputs at least two names when asked to enter
    their full name.
Ask the user to input their full name.
Perform some validation to check that the user has entered a full name.
Give an appropriate error message if they haven't. 

One of the following messages should be displayed based on the user's input:
either “You haven't entered anything. Please enter your full name.”
or “You have entered less than 4 characters. Please make sure that you 
    have entered your name and surname.”
or “You have entered more than 25 characters. Please make sure that you
    have only entered your full name.”
or “Thank you for entering your name.”
"""

#===========================================
# Declare output message variables
#===========================================

#  if length is zero
error_message1 = ("You haven't entered anything. " 
                  "Please enter your full name.")  # ask again

# if length is short
error_message2 = ("You have entered less than 4 characters. "        
                  "Please make sure that you have entered your name "
                  "and surname.")    # ask again

# if length is long
error_message3 = ("You have entered more than 25 characters. "
                  "Please make sure that you have only entered your "
                  "full name.")   # ask again

# if user has entered only one name
error_message4 = ("You have entered only one name. "
                  "Please make sure that you have entered two names.")

# if length is good
final_message = ("Thank you for entering your name.") # stop

#===========================================
# Prompt the user to input their full name
#===========================================
# input() always returns a string even for numeric input
full_name = input("Please enter your full name and press return: ")

#===========================================
# Compute the length of the input string
#===========================================
ll = len(full_name)

#===========================================
# Test the length and output messages based 
# on cases given in error messages
#===========================================
if ll == 0:      # if length is zero
    print(error_message1)
elif ll < 4:     # if length is short
    print(error_message2)
elif ll > 25:    # if length is long
    print(error_message3)
else:
    nn = len(full_name.split())
    if nn < 2:     # if length is good and only one name given
        print(error_message4)
    else:          # if length is good and more than one name is given
        print(final_message)
