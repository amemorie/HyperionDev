"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T07 - Beginner control structures - While loop 

Compulsory Task 3:
- Write a program that always asks the user to enter a number.
- When the user enters -1, the program should stop requesting the user to
enter a number,
- The program must then calculate the average of the numbers entered,
excluding the -1.
- Make use of the while loop repetition structure to implement the
program.
- Compile, save, and run your file.
"""
# Create a string of = characters.
output_hline = "="*72

# Print the instructions for the user.
print(output_hline)
print("Calculate and print the mean average of a list of user-input "
        "numbers")
print("      that are greater than or equal to zero.")
print("Numbers can be integers or floating point.")
print("Numbers cannot be negative or complex.")
print("Press return after each number in the list.")
print("Input -1 when you have input all the numbers you want to "
      "include in the ")
print("    calculation.")
print(output_hline)

# Initialise variables.
output_list = []
number = False
output = None

# Exit the loop when the user types in -1.
while number != -1: 
    # If not the first iteration or a user-input invalid number 
    # add the input value to the output list. 
    if number != False : output_list.append(number)
    try: 
        # Requst user input.
        number = float(input("Enter a number that is greater "
                             "than or equal to zero (-1 to exit): "))
        # If the number is not valid raise an error. 
        if (number < 0 and number != -1): raise ValueError         
    except (TypeError, ValueError): 
        # If the input value is not valid, let the user know. 
        print("That was not a valid number, please try again.")
        number = False 

if len(output_list) != 0: 
    # If the user has input any valid values 
    # print out the mean average.
    output = sum(output_list)/len(output_list)
    print(f"The mean average of your input values is: {output}")
else: 
    # Else print out an infomation message. 
    print("No valid inputs given.")
