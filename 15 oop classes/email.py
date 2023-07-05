### --- OOP Email Simulator --- ###
import os

class Email:
    '''
    Email class.
    
    :param has_been_read: flag if email has been read. 
    :type has_been_read: boolean class variable.
    '''
    has_been_read: bool = False 
    
    def __init__(self, email_address:str, 
                subject_line: str, 
                email_content:str) -> None:
        '''
        Initialise the instance variables for emails.
        :param email_address: email address of the sender
        :type email_address: str
        
        :param subject_line: subject line of the email
        :type subject_line: str
        
        :param email_content: content of the email
        :type email_content: str
        
        :returns: None
        
        '''
        self.email_address = email_address 
        self.subject_line = subject_line
        self.email_content = email_content

    def toggle_has_been_read(self) -> None:
        '''
        Method to change 'has_been_read' emails from False to True.
        :param self: Email object
        :type self: Email object
        
        :returns: None
        '''
        self.has_been_read = True
        
def email() -> None:
    '''
    Email simulator function with OOP. 
    
    :params: None
    :returns: None
    '''
    inbox: list[Email] = []

    def populate_inbox() -> None:
        '''
        Function to simulate emails in an inbox. 
        
        :params: None
        :returns: None
        '''

        # Create 3 sample emails and add them to the Inbox list. 
        email_address1: str = "xy@xyz.com"
        subject_line1: str = "Welcome to your inbox!"
        email_content1: str = "This is your welcome email. \n Best wishes, Bob."
        email1: Email = Email(email_address1, subject_line1, email_content1)

        email_address2: str = "ab@abc.com"
        subject_line2: str = "Thank you for signing up to our newsletter"
        email_content2: str = "This is today's news: \n The weather is sunny!"
        email2: Email = Email(email_address2, subject_line2, email_content2)

        email_address3: str = "bib@bab.com"
        subject_line3: str = "Your shopping will arrive at 6pm"
        email_content3: str = ("Thank you for shopping with us.\n "
                        "Your shopping will arrive at 6pm\n" 
                        "See you then.")
        email3: Email = Email(email_address3, subject_line3, email_content3)

        inbox.extend([email1, email2, email3])

        # for i in range(200):
        #     j = str(i % 10)
        #     email_address: str = "spam"+j+"@spam.com"
        #     subject_line: str = "This is blatently spam "+j
        #     email_content: str = ("Spam\nSpam\nSpam")
        #     email: Email = Email(email_address, subject_line, email_content)
        #     inbox.extend([email])


    def list_emails() -> None:
        '''
        Function to list emails with subject line. 
        
        :params: None
        :returns: None
        '''
        total_emails: int = len(inbox)
        hline: str = ("|"+"="*73+"|")
        emails_per_page: int = 100
            
        for i, email in enumerate(inbox):
            if ((i > 1) and (i % emails_per_page == 0)):
                continue_keypress = input("Press enter to exit or any other"
                    +" key to print the next 100 emails.")
                if continue_keypress == "":
                    return

            if (i % emails_per_page) == 0:
                maxemails = min([i+emails_per_page, total_emails])
                print(f"{i+1}-{maxemails} of {total_emails}")
            if i == 0:
                print(f"|   #  : Email address   | Subject"+" "*39+" |")
                print(hline)
        
            lenaddress = min([len(email.email_address),15])
            lensubject = min([len(email.subject_line),46])
            
            print(f"|{i+1:4d}  : "
                +f"{email.email_address[:lenaddress].ljust(15) } | "
                +f"{email.subject_line[:lensubject].ljust(46) } | ")
                
        print(hline)
            
    def read_email(index: int) -> bool:
        '''
        Function to read an email. 
        
        :param index: index of email in inbox. 
        :type index: int
        
        '''
        # Create a function which displays a selected email. 
        email: Email = inbox[index]
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        print(email.subject_line)
        print(email.email_address)
        print(email.email_content)
        print(" ")
        email.toggle_has_been_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
        return True

    populate_inbox()
    
    menu: bool = True

    while True:
        try:
            user_choice: int = int(input('''\n
    Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
        except:
            user_choice = -1
        print(user_choice)
        
        if user_choice == 1:
            # Read an email.
            list_emails()
            while True:
                print("Enter email number ")
                choose_email: str = input("or press enter to return to main menu: ")
                if choose_email == "":
                    index: int = -1
                    break
                index = int(choose_email)-1
                try:
                    inbox[index]
                    break
                except:
                    continue
                
            if index != -1:
                print(" ")
                is_read: bool = read_email(index)
            else: 
                print("Returning to main menu.")
                continue
            
        elif user_choice == 2:
            # View unread emails.
            print(" ")
            for i, email in enumerate(inbox): 
                if email.has_been_read == False: #type: ignore
                    print(f"{i+1} : "+email.subject_line) # type:ignore
                
        elif user_choice == 3:
            # Quit application
            print("Goodbye")
            break
        else:
            print("Oops - incorrect input.")
            
if __name__ == "__main__":
    email()