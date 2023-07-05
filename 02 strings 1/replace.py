"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T02 - The String Data Type

Compulsory Task 2: 
Create a string variable that contains the value "The!quick!brown!fox!jumps!over!the!lazy!dog!."
Create a second string variable in which every "!" exclamation mark is replaced with a blank space using the replace() function. 
Print this sentence as "The quick brown fox jumps over the lazy dog." 
Create a third string variable in which every character of the second string is upper case using the upper() function. 
Print that sentence as: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
Print the third sentence in reverse.
"""

# Create a string variable that contains the value "The!quick!brown!fox!jumps!over!the!lazy!dog!."
sentence1 = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Create a second string variable in which every "!" exclamation mark is replaced with a blank space using the replace() function. 
sentence2 = sentence1.replace("!", " ")

# Fix the extra space that is between "g" in "dog" and the final full stop
index = -2
sentence2 = sentence2[:index] + sentence2[index + 1:]

# Print this sentence as "The quick brown fox jumps over the lazy dog."
print(sentence2)

# Create a third string variable in which every character of the second string is upper case using the upper() function. 
sentence3 = sentence2.upper()

# Print that sentence as: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
print(sentence3)

# Print the third sentence in reverse.
print(sentence2[::-1])
