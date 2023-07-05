def alternative():
    """
    Request user type in a string. 
    Print:
    - The string with alternating letters in upper and lower case.
    - The string with alternating words in upper and lower case.
    """

    while True:
        input_string = input("Enter a string or type \".\" "
                             "to use the standard string: ")
        if input_string.strip() == ".": 
            input_string = ("This is my Dummy String to TEST the "
                            +"full RANGE OF cHanges to the Strings.")
        if len(input_string.strip()) == 0:
            print("No string input, please try again.")
        else:
            break
    
    alternative_letters = ""
    counter = 0 
    for i in range(len(input_string)):
        if (input_string[i] in ["\n","\t","\s"]) is True:
            # Do not include \n, \t, \s as a letter for alternation.
            # Do put them back into the output string.
            alternative_letters += input_string[i]
            continue
        if counter % 2 == 0: # Even index letters upper case.
            alternative_letters += input_string[i].upper()
        else:  # Odd index letters lower case.
            alternative_letters += input_string[i].lower()
        counter += 1
        
    print(alternative_letters)

    alternative_words_list = []
    input_string_list = input_string.split(" ")
    counter = 0
    for j in range(len(input_string_list)):
        if input_string_list[j] in ["\n","\t","\s",]:
            # Do not include \n, \t, \s as a word for alternation.
            # But do put them back into the output string.
            alternative_words_list.append(input_string_list[j])
            continue
        if counter % 2 == 0: # Even index words upper case.
            alternative_words_list.append((input_string_list[j]).upper())
        else: # Odd index words lower case.
            alternative_words_list.append((input_string_list[j]).lower())
        counter += 1
        
    alternative_words = " ".join(alternative_words_list)
    print(alternative_words)

if __name__ == "__main__":
    alternative()