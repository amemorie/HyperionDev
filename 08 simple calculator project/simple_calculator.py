def simple_calculator():
    """
    Perform an arithmetical operation on two floating point 
    numbers, print the output to a file and to the screen. 
    
    Numbers and operations can be
    - interactively input by the user or 
    - from an input file.
    """
    
    valid_operators_string_list = ["+","-","*","/","%","//","**"] # All built-in arithmetic operators
    default_input_file = ("T09-simple-calculator-input.txt")
    default_output_file = ("T09-simple-calculator-output.txt")
    file_does_not_exist_message = (" does not exist. "
                          "\nEnter a new filename or . for default filename. "
                          "\nPress C-c to exit.")

    #------------------------------------------------------------------
    # Welcome splash screen text.
    #------------------------------------------------------------------
    print("Please choose from the following 2 options:")
    print("1) \"simple\" -"
          "\n   Simple calculator prints the result of arithmetic "
          "operations on" 
          "\n   two numbers input by the user interactively and "
          "outputs them to "
          "\n   a file with a name input by the user interactively.") 
    print("2) \"filename\" -" 
          "\n   Reads calculations from a file called filename."
          "\n   Performs the calculations and outputs to the"
          " screen and to a new file "
          "\n   called filename+output."
          "\n   Input file should have a single calculation per line"
          "\n   with the format \"number operator number\" "
          "\n   anything after the second number will be ignored"
          " so comments can be used."
          "\n   Type \".\" to use the default filenames.")
    #------------------------------------------------------------------

    calculation_option = input("Enter \"simple\" or the filename you wish to use:")
    
    if calculation_option.lower().strip() == "simple":
        # Simple calculator, interactively input calculation values.       
        operand_string = [[]]
     
        for i in [0,1]:  # Request input of two values.
            while True : # Loop the request until a valid number is input.
                input_value = input("Enter a number: ") 
                try:
                    test_input = float(input_value)
                    break
                except ValueError:
                    print("Not a valid number. Please try again "+
                        "or press C-c to exit.")

            operand_string[0].append(input_value) 
            
            print("Valid operators to perform on these numbers are: ")
            print(" ".join(valid_operators_string_list))
            
            while i == 0: # Request input of operation to perform.
                operator_string = input("Enter an operation to perform: ")
                operator_string = "".join(operator_string.split()) # Remove whitespace from operator.
                if operator_string not in valid_operators_string_list: 
                    print("Not a valid operation from "
                          +" ".join(valid_operators_string_list)
                          +"\nPlease try again "    
                          +"or press C-c to exit.")   
                else:
                    operator_string = [operator_string]
                    break
                
            while i == 1: # Request an output filename.
                filename_output = input("Enter the output filename or \".\" "
                                 "to use the default value: ")
                if filename_output == ".": 
                    filename_output = default_output_file
                elif filename_output == "None":
                    filename_output = None
                    break
                # else: pass
                
                try:
                    file_object = open(filename_output,"a") 
                    break
                except FileNotFoundError:   
                    print(filename_output+file_does_not_exist_message)
    else:
        # Calculations from an input file.
        while True:
            if calculation_option == ".": 
                filename_input = default_input_file
            else:
                filename_input = calculation_option 
            # Test the filename and repeat the request if the filename is not valid. 
            try:
                file_object = open(filename_input,"r") 
                break
            except FileNotFoundError:   
                calculation_option = input(filename_input
                                           +file_does_not_exist_message)

        operand_string = []
        operator_string = []
        
        for line in file_object:
            test_string = line
            # Add extra spaces around all valid_operators_string_list characters
            # so that the split works even if no spaces are present.
            for m in valid_operators_string_list:
                # For operators in the input string that are built from 
                # two characters, don't add a space between the operators.
                endofline_boolean = False
                n = 0
                while endofline_boolean is not True : 
                    if test_string[n] == m: 
                        if test_string[n+1] == m: 
                            test_string = (test_string[:n]+" "
                                           +test_string[n:n+2]+" "
                                           +test_string[n+2:])
                            n+=4
                        else:
                            test_string = (test_string[:n]+" "
                                           +test_string[n]+" "
                                           +test_string[n+1:])
                            n+=3
                    else:
                        n+=1                    
                    if n >= len(test_string)-1: # Don't need to check forward from the last character. 
                        endofline_boolean = True                    
            
            input_string = test_string.split()
            if len(input_string) < 3 :
                print("skipping "+line+" : does not have correct "
                      "amount of information ")
                continue
            if input_string[1] not in valid_operators_string_list:
                print("skipping "+line+" : does not have a valid operator"
                      )
                continue
            try: 
                operand_number = float(input_string[0])
                operand_number = float(input_string[2])
            except ValueError:
                print("skipping "+line+" : does not have numeric operands"
                      )
                continue
            operand_string.append([input_string[0],input_string[2]])           
            operator_string.append(input_string[1])            
        
        file_object.close()

        # Output filename is the input filename with output added.
        filetype_index = filename_input.index(".")
        filename_output = (filename_input[:filetype_index]
                           +"-output"
                           +filename_input[filetype_index:])
        file_object = open(filename_output,"a")

    for k in range(len(operator_string)):
        try:
            # Evaluate the calculation, return a number. 
            result_number = eval(operand_string[k][0]+
                                operator_string[k]+
                                operand_string[k][1])
            
            # Create an output string to print. 
            print_string = (operand_string[k][0]+" "
                            +operator_string[k]+" "
                            +operand_string[k][1]+" = "
                            +f"{result_number}\n")

            # Print the result to the screen.
            print(print_string)
            print(f"{result_number}")
            
            file_object.write(print_string)
        except Exception as e:
            print_string = (operand_string[k][0]+" "
                            +operator_string[k]+" "
                            +operand_string[k][1])
            print("skipping "+print_string+" : calculation error ")
            print(e)
            
    file_object.close()        
                
if __name__ == "__main__":
    simple_calculator()