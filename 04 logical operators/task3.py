"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T04 - Logical programming - operators

Compulsory Task 1:

This is a program that determines the award a person competing in a
triathlon will receive.
It reads in the times (in minutes) for all three events of a triathlon, 
namely swimming, cycling, and running, 
and then calculates and displays the total time taken to complete the 
triathlon.

The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.

The program displays the award that the participant will receive based 
on the following criteria:

| Total time                                |  Award                  |
|-------------------------------------------|-------------------------|
| Within qualifying time.                   | Provincial Colours      |
| Within 5 minutes of qualifying time.      | Provincial Half Colours |
| Within 10 minutes of qualifying time.     | Provincial Scroll       |
| More than 10 minutes of qualifying time.  | No award                |

"""

#====================================================
# Prompt the user to enter their three segment times
#====================================================
# request times in whole minutes, using an input function
swimming_time = int(input("Please enter the time (in whole minutes) that you completed your swimming segment: "))
cycling_time = int(input("Please enter the time (in whole minutes) that you completed your cycling segment: "))
running_time = int(input("Please enter the time (in whole minutes) that you completed your running segment: "))

# check that none of the times is too short to be real
if (swimming_time < 10) or (cycling_time < 10) or (running_time < 10):
    print("*******************************")
    print("One of your times is too short!")
    print("Did you make a mistake?")
    print("*******************************")

#======================================================================
# Calculate and display the total time taken to complete the triathlon.
#======================================================================
# calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# display the total time taken to complete the triathlon
print()
print(f"Total time taken to complete the triathlon: {str(total_time)} minutes")
print()

#===============================================================
# Define the qualifying time variable.
# NB. The competitor has qualified if they complete the 
# triathlon in LESS THAN OR EQUAL TO the qualifying time.
# Also define variables for the time boundaries of the other 
# awards. 
# Within qualifying time: Provincial Colours
# Within 5 minutes of the qualifying time: Provincial Half Colours
# Within 10 minutes of the qualifying time: Provincial Scroll
# More than 10 minutes above the qualifying time: No award
#===============================================================
qualifying_time = 100  # minutes, integer variable
scroll_time = 5        # minutes, integer variable
noaward_time = 10      # minutes, integer variable

#======================================================================
# Test the competitor time against the total time 
# and print out the award the competitor has received. 
#======================================================================
# NB. This solution uses the order of tests within the control 
# structure to create the correct branches using only a single  
# arithmetic operator in each test.  
# An alternative solution would be to use arithmetic and logical 
# operators together for each conditions. This solution would be 
# more explicit (cf zen of python) but would be less efficient 
# (cf zen of python).    
print("**************************************************************")
if total_time > (qualifying_time + noaward_time):  # No award
    print("You have not received an award because you completed the "
          "triathlon\nin more than 10 minutes over the qualifying time "
          "of 100 minutes.\n\nGood luck next time! Keep up the training."
          "\n")
elif total_time > (qualifying_time + scroll_time): # Provincial scroll
    print("Congratulations!\nYou completed the triathlon in less than " 
          "or equal to 10 minutes over the qualifying time of 100 "
          "minutes\nand have received an award of a Provincial Scroll!"
          "\n\nKeep up the training. Good luck getting to the "
          "qualifying time next time!\n")
elif total_time > (qualifying_time):               # Provincial Half Colours
    print("Congratulations!\nYou completed the triathlon in less than "
          "or equal to 5 minutes over the qualifying time of 100 minutes"
          "\nand have been awarded Provincial Half Colours!"
          "\n\nKeep up the training. Good luck getting to the "
          "qualifying time next time!\n")
else:                                               # Provincial Colours 
    print("Congratulations!\nYou completed the triathlon in less than "
          "or equal to the qualifying time of 100 minutes\nand have"
          " been awarded Provincial Colours! \n\nKeep up the "
          "training. Good luck qualifying again next time!\n")
print("**********************************************************************")
print()
