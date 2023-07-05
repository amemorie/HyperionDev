import re
import os
import time
import sys

def check_studentid_format(studentid: str, 
                    studentidformat: str) ->bool:
    studentid.strip()
    
    # match student id input to studentidformat string
    # mypy difficult to type this one! leaving it as any
    is_studentid = re.search(studentidformat, studentid)
    
    if is_studentid == None:
        print("You have entered an id that is not the correct "
                "format. Please try again")
        return False
    return True

def print_student_register(venue: str, examdatetime: str, 
                           studentids: list[str]) -> None:
    """
    prints a student register to a file

    :param venue: Exam venue name
    :type venue: str
    :param examdatetime: Exam date and time
    :type examdatetime: str
    :param studentids: List of student ids to print
    :type studentids: list[str]
    
    prints to output filename reg_form.txt 
    """
    filename:str = "reg_form.txt"
    
    print("Printing to filename: "+filename)
    number_of_students: int = len(studentids)
    headerline1: str = ("Registration form for venue: "+venue
                       +" on "+examdatetime)
    headerline2: str = ("Total number of students registered = "
                       +f"{number_of_students: 5d}")
    
    headerlinelen: int = len(headerline1)
    printlines: list[str] = [headerline1,
                             headerline2, 
                             "="*headerlinelen]
    dotted_line: str = "\n signature: "+("." * (headerlinelen-10)) + "\n"
    studentidsstrings: list[str] = [studentid+dotted_line for studentid in studentids]
    printlines.extend(studentidsstrings)
    
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(len(printlines)):
            file.write(printlines[i]+"\n")
    
def student_register(studentidformat: str ="([a-zA-Z]{3})([0-9]{3})", 
                     examvenuename: str = "Exam Venue 1", 
                     examdatetime: str = "13 June 2008 14:00-17:15", 
                     examvenuemaxstudents: int = 55) -> bool:
    """
    A program to allow students to register for an exam venue
    
    :param studentidformat: default value "([a-zA-Z]{3})([0-9]{3})"
    :type studentidformat: str
    :param examvenuename: default value "Exam Venue 1"
    :type examvenuename: str
    :param examdatetime: default value "13 June 2008"
    :type examdatetime: str
    :param examvenuemaxstudents: default value 55
        maximum number of students that can fit in the given venue
    :type examvenuemaxstudents: int
    
    :returns: boolean
    """  
    ##==============================
    ## Part 1: Administrator screen
    ##==============================    
    os.system('cls')
    print("Welcome Administrator!")
    while True:
        try:
            request: str = input("How many students are registering? ")
            if request.isnumeric() == True:
                number_of_students: int = int(request)
                if number_of_students > examvenuemaxstudents:
                    print("The maximum number of students for this venue is "
                          +str(examvenuemaxstudents))
                    print("Please enter a number between 1 and "+
                          str(examvenuemaxstudents))
                    continue
                else:
                    break
            if len(request) == 0:
                sys.exit()            
            print("Please enter a number")
        except (KeyboardInterrupt, SystemExit):
            sys.exit()
 
    print("Thank you Administrator. You wish to register "+str(number_of_students))
    ready_to_begin = input("Please press y to begin registering students, press any other key to exit: ")
    ready_to_begin.strip()
    
    if ready_to_begin != "y":
        sys.exit()
        
    ##==============================
    ## Part 2: Student screen
    ##==============================        
    studentids: list[str] = []
    for student in range(number_of_students):
        os.system('cls')
        print("Registering student "+str(student+1)+" of "+str(number_of_students))
        print("")
        if student == 0:
            newstr = "Welcome! "
        else:
            newstr = ("\n\nNext student please!\n\n Welcome! ")
        newstr += ("Register for "
                    +examvenuename+" at "+examdatetime+". \n")

        while True:
            studentid: str = \
                input(newstr+" Enter your student id number (format ABC123): ")
            is_correct_format: bool = \
                check_studentid_format(studentid, studentidformat)
            if is_correct_format == False:
                newstr = ""
                continue
            print("Please check carefully and confirm "
                  "that your student id number is :\n\n"
                  +studentid+"\n")
            student_id_checked: str = \
                input("Enter y if correct, "
                      "enter n to re-enter your student id: ")
            if student_id_checked == "y":
                studentids.append(studentid)
                break
            else:
                newstr = ""
                continue
        
        print("Student id \""+studentid+"\" is now registered for this exam venue.")
        time.sleep(3)

    ##==============================
    ## Part 3: Print to file
    ##==============================           
    os.system('cls')
    print(str(number_of_students)+" student(s) are now registered. Printing register to file.")
    print_student_register(examvenuename,examdatetime, studentids)
    return True

if __name__ == "__main__":
    studentidformat = ""
    student_register()
    