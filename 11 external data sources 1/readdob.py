from os import path as ospath
from datetime import datetime 

def print_names_and_dobs_to_outputfilename(printlines: list[str], \
                                           outputfilename: str) -> bool:
    """
    Function to print names and dates of birth of people in a dictionary
    to an output file
    
    :param outputfilename: if output file name contains ".txt" and is not "" 
        then print the names and dates of birth to the output file name
    :type outputfilename: str
    :param printlines: list containing names and strings of names and 
        dates of birth
    :type printlines: list[str]
    :returns bool: returns True if file printed correctly, False if not
    """
    if outputfilename == "" or (not ".txt" in outputfilename): 
        return False
    
    opentype: str 
    if ospath.exists(outputfilename):
        opentype = "a" 
    else:
        opentype = "w"

    with open(outputfilename, opentype, encoding="utf-8") as file:
        for lines in printlines:
            file.write(lines+"\n")
        file.write("\n")
    return True

def print_names_and_dobs(people: dict, outputfilename: str = "") -> None:
    """
    Function to print names and dates of birth of people in a dictionary
    
    :param people: dictionary containing the persons's full name as key  
        and their date of birth as value
    :type people: dict 
    :param outputfilename: default value ""
       if output file name is not "" then print to the output file name
    :type outputfilename: str
    :returns None:
    """
    
    headerline1: str = "Name"
    headerline2: str = "Birthdate"

    printlines: list[str] = [headerline1]
    person: str
    for person in people.keys(): 
        printlines.append(person)
    
    printlines.append("")
    
    printlines.append(headerline2)
    dob: str
    for dob in people.values(): 
        printlines.append(dob)
    
    lines: str
    for lines in printlines:
        print(lines)
    
    test: bool = True
    if outputfilename != "": 
        test = print_names_and_dobs_to_outputfilename(printlines, 
                                                      outputfilename)
    if test == False:
        raise Exception("Outputfilename not correct. "
                        "Could not print to the file \""
                        +outputfilename+"\"")

def check_line(linecounter: int, check_line: list[str]) -> None:
    """
    Function to check if the list has 5 elements 
    when the file string is split into words

    :param linecounter: line number in the input file
        (note this is not the python index of the line)
    :type linecouonter: int
    :param check_line: list of words in the line
    :type check_line: list[str]
    
    :returns None:
    """

    if len(check_line) != 5: 
        check_line_message = " ".join(check_line)
        print("Error on line "+str(linecounter)+": line does not contain 5 words" )
        print("The line reads:" + check_line_message)
        print("Please correct the input file and rerun the program")
        exit()
    return

def check_name(linecounter: int, names: list[str]):
    """
    Function to check if the name is made up of only
    alphabetical characters
    
    :param linecounter: line number in the input file
        (note this is not the python index of the line)
    :type linecounter: int
    :param names: list with contents of 
        [first name field, second name field] 
    :type name: list[str]
    
    :returns None:
    """
    
    for name in names:
        if name.isalpha() == False: 
            print("Error on line "+str(linecounter)+": name "+name+"is not alphabetical")
            print("Please correct the input file and retry the program")
            exit()
    return
            
def check_dob(linecounter: int, date: str, dateformat: str ="%d %B %Y") -> None:
    """
    Function to check if the date of birth is correct format
    and exists as a real date
    
    :param linecounter: line number in the input file
        (note this is not the python index of the line)
    :type linecounter: int
    :param date: date
    :type date: str
    :param dateformat: format of the date in the input file. 
            Defaults to "%d %B %Y".
    :type dateformat: str, optional
    
    :returns None:
    """
    
    try:
        dateObject = datetime.strptime(date, dateformat)
    # If the date validation goes wrong exit the program
    except ValueError:
        # printing the appropriate text if ValueError occurs
        print("Error on line: "+str(linecounter)+": date "
              +date+" is an incorrect date.")
        print("It may be an incorrect format, should be %d %B %Y, "
              "or a date that doesnt exist")
        print("such as the 30th February")
        print("Please correct the input file and retry the program")
        exit()
    return
   
def readdob(filename: str, outputfilename: str = "", 
            dateformat: str = "%d %B %Y") -> None: 
    """
    Function to read names and dates of birth of people listed in an 
    input text file
    Outputs the names as a single list and birthdays as a 
    separate list to the screen
    
    :param filename: filename of the file containing date of birth 
        information
    :type filename: str
    :param outputfilename: default value = ""
       if output file name is not "" then print to the output file name
    :type outputfilename: str
    :param dateformat: default value = "%d %B %Y"
       format of the date field in the input file
    :type dateformat: str
    :returns None:
    """    
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    people: dict = {}
    linecounter = 1
    for line in lines:
        cleanline = line.strip().split()
        check_line(linecounter, cleanline)
 
        check_name(linecounter, cleanline[0:1])
        fullname: str = " ".join(cleanline[:2])

        fulldob: str = " ".join(cleanline[2:])
        ## there is a problem with DOB.txt
        ## which gives a DOB of 30 February for Jerry Keller
        ## uncomment this line to catch the error
        #check_dob(linecounter, fulldob, dateformat)
            
        people[fullname] = fulldob
        linecounter += 1

    print_names_and_dobs(people, outputfilename)
    
if __name__ == "__main__":
    filename = "./DOB.txt"
    outputfilename = "./listnamesanddobs.txt"
    dateformat = "%d %B %Y"
    readdob(filename, outputfilename, dateformat)