"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T05 - Capstone Project 1

Compulsory Task 1:

The user chooses the type of calculation they want to do from:
- investment - to calculate the amount of interest you'll earn on 
    your investment
- bond - to calculate the amount you'll have to pay on a home loan
    
The user is able to capitalise their selection without affecting how
the program proceeds. i.e. 'Bond', 'bond', 'BOND' or 'investment', 
'Investment', 'INVESTMENT', etc., are all be recognised as valid 
entries. 

If the user doesn't type in a valid input, an appropriate error message 
is shown.
==================================
If the user selects 'investment':
==================================
Inputs:
  - The amount of money that they are depositing (P)
  - The annual interest rate (as a percentage) (R). Only the number of  
  the interest rate should be entered - don't worry about having to 
  deal with the added '%', e.g. The user should enter 8 and not 8%.
  - The number of years they plan on investing (t).
  - Whether they want "simple" or "compound" interest 

Outputs: 
  - prints the inputs and the appropriate amount that they will 
  get back after the given period, at the specified interest rate (A).
  
Formulae for interest types: 
  r = R / 100.0
  Simple interest: A = P(1 + r x t)
  Compound interest: A = P(1 + r)^t
  
===========================
If the user selects 'bond':
===========================
Inputs: 
  - The amount of money that they borrow (P)
  - The annual interest rate (as a percentage)(R). Only the number of
  the interest rate should be entered - don't worry about have to 
  deal with the added '%', e.g. The user should enter 8 and not 8%. 
  - The number of months they are planning on borrowing over (t).

Outputs:
  - prints the inputs and the amount they will have to pay back each 
  month to repay the bond (A)

Formula: 
  r = (R/100.) / 12.0
  A = (r * P)/(1 - (1 + r)**(-t))
  
"""
def main():
    
    # =============
    # Import block.
    # =============
    import math

    # =============================================================
    #  Print the welcome splash screen.
    # =============================================================
    print("==================================================")      
    print("          Welcome to the finance calculator!      ")
    print("==================================================")      
    print("The finance calculator can compute interest on    ")
    print("two types of financial transactions:              ")
    print("\ninvestment - to calculate the amount of interest you'll earn on"
        " your investment")
    print("bond - to calculate the amount you'll have to pay on a home "
        "loan\n")
    print("==================================================")      



    # =============================================================
    # Prompt the user to chose investment or bond calculation type.
    # =============================================================
    # User choice input variable to control the branch taken.
    isinput = input("Enter either 'investment' or 'bond' from the menu "
                    "above to proceed: ")

    # Lower case input to get calculation option variable.
    calculation_option = isinput.strip().lower()

    # If the user inputs a value that cannot be used in the calculation
    # because it is the wrong data type, print the following error message.
    error_message = ("You did not enter a valid amount. Please input a "
                    " number. If you would like to quit the calculation"
                    " program press Ctrl + c (windows) or Cmd + c "
                    "(macOS)")

    # ================================================================
    # Make the finance calculation.
    # ================================================================
    if calculation_option == "investment":
        # Calculate the amount of interest you'll earn on your investment.
        print("\nThank you for choosing to calculate the amount of "
            "interest you'll earn on your investment.\n")
        # Prompt the user to input the investment balance, interest rate
        # and duration.
        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            # user to enter a number or exit the program.
            try:
                principal = float(input("Enter the amount you are investing"
                                        "in £ :"))
                break
            except ValueError:
                print(error_message)
                
        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            # user to enter a number or exit the program.
            try:
                interest_rate = float(input("Enter the annual interest rate, do "
                                            "not include the '%' sign: "))
                break
            except ValueError:
                print(error_message)
                
        # The interest rate is input in %. 
        # The calculation is carried out on the interest rate in decimal format.
        # Convert between the two by dividing by 100 as a floating point number. 
        rate = interest_rate / 100.
        
        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            # user to enter a number or exit the program.
            try:
                years = float(input("Enter the number of years you will be "
                                    "investing over: "))
                break
            except ValueError:
                print(error_message)
                
        # User inputs choice of interest calculation.
        ii = input("Would you like to calculate 'simple' or 'compound' interest?\n"
                        "(See docstring for definitions of the "
                        "calculations used.)\n"
                        "Enter 'simple' or 'compound':")
        interest = ii.strip().lower()

        if interest == "simple" or interest == "compound":
            # If interest is a valid option calculate the
            # return on the investment using the functions given in the
            # docstring.
            if interest == "simple":
                return_on_investment = (principal*(1+(rate*years)))
            elif interest == "compound":
                return_on_investment = (principal * 
                                        math.pow((1+rate),years))
                
            # Return on investment calculation can produce an amount that
            # has non zero digits in more than two decimal places. 
            # The output is in currency which is to two decimal places. 
            # To round this correctly this program converts the return on 
            # the investment to a value in pence (p) by multiplying by 100,
            # the amount is rounded, then it is convert back to pounds 
            # (£) by dividing by 100.
            rounded_roi = round(return_on_investment*100.)/100.
            # Convert to string format for the output.
            roi = '%.2f' % rounded_roi 
            
            # Print the inputs and the output. 
            print("==================================================")
            print("The total amount you will receive on              ")
            print(f"your initial investment of       £{'%.2f' % principal}")
            print(f"at an interest rate of            {interest_rate} %")
            print(f"after                             {years} years") 
            print(f"with {interest} interest is:                      ")
            print("===================================================")
            print(f"                                 £{roi}")
            print("===================================================") 
            # The program finishes here.     
        else:
            # If the input for choice of interest calculation is not a 
            # valid option, do nothing and exit the program.
            # It was a choice not to allow the user to input again from the
            # options to exhibit this as a different way of doing things
            # within this example program, but it could be done with a 
            # while statement as above depending on requirements. 
            print(f"{interest} is not a valid option.")
            print("Please start again and choose a valid option from "
                "\'simple\' or \'compound\'.")
            # The program finishes here. 
            
    elif calculation_option == "bond":
        # Calculate the amount of the repayments due on a bond due to interest
        # for a bond taken out over an input time period. 
        print("\nThank you for choosing to calculate the repayment amount "
            "you'll have to pay back each month on a home loan.\n")       

        # Prompt the user to input the present value of the bond, the 
        # annual interest rate and the number of months over which the bond
        # will be repaid.
        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            # user to enter a number or exit the program.
            try:
                principal = float(input("Enter the present value of the bond in £ "
                                ":"))
                break
            except ValueError:
                print(error_message)

        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            # user to enter a number or exit the program.
            try:           
                interest_rate = float(input("Enter the annual interest rate, do "
                                        "not include the '%' sign: "))
                if interest_rate < 0: raise ValueError
                break
            except ValueError:
                print(error_message)

        # The interest rate is input as an annual rate in %. 
        # The calculation is carried out on the interest rate per month in 
        # decimal format.
        # Convert between the two by dividing by 100 as a floating point 
        # number and dividing by months per year (12.) as a floating point 
        # number. 
        rate = (interest_rate/100.)/12.0
        
        while True:
            # If the user inputs a value that is not able to be converted
            # to a valid float data type, the control structure allows the 
            #  user to enter a number or exit the program.
            try:
                months = float(input("Enter the number of months over which you"
                                    " plan to repay the bond: "))
                if months < 0: raise ValueError
                break
            except ValueError:
                print(error_message)

        # Calculate the monthly repayment amound using the 
        # function given in the docstring.
        # The function given in the task document leads to 
        # a ZeroDivisionError if rate is zero 
        # The function doesn't calculate the correct 
        # amount if months is zero
        if (rate > 0 and months > 0):
            repayment_per_month = (
                (rate * principal)/
                (1 - (1 + rate)**(-months))
                )
        elif (months != 0): 
            # If the rate is zero and the number of 
            # months is not zero, repay the principal
            # over the given number of months.
            repayment_per_month = (principal / months)
        else: 
            # If the interest rate is zero and the number
            # of months is zero then repay the principal
            # in the first month
            repayment_per_month = principal
            
        # Repayment per month calculation can produce an amount that
        # has non zero digits in more than two decimal places. 
        # The output is in currency which is to two decimal places. 
        # To round this correctly this program converts the repayment
        # per month into a value in pence (p) by multiplying by 100, 
        # the amount is rounded, then converts it back to pounds (£) 
        # by dividing by 100. 
        rounded_rpm = round(repayment_per_month*100.0)/100.0
        # Convert to string format for the output.
        rpm = '%.2f' % rounded_rpm

        # Print the inputs and the output.          
        print("==================================================")
        print("The amount you will pay back each month on        ")
        print(f"your bond of                     £{'%.2f' % principal}")
        print(f"at a annual interest rate of      {interest_rate} %")
        print(f"over                              {months} months") 
        print("is:                                               ")
        print("===================================================")
        print(f"                                 £{rpm}")
        print("===================================================")  
        # The program finishes here.    
    else: 
        # If the calculation type is not a valid option do nothing.
        print(f"{calculation_option} is not a valid option.")
        print("Please start again and choose a valid option from "
            "\'investment\' or \'bond\'.")
        # The program ends here 
        
if __name__ == '__main__':
    main()