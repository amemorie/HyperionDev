"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T02 - The String Data Type

Compulsory Task 1: 
Declare a variable called hero that contains the value "$$$Superman$$$"
Use the string manipulation method strip() and print hero so the output is: Superman
"""

# Declare a variable called hero to contain the value "$$$Superman$$$"
hero = "$$$Superman$$$"

# Strip hero of the leading and trailing $s
hero_strip = hero.strip("$")

# Print the stripped variable
print(hero_strip)
