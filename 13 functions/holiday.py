import datetime

def choice_in_list(choice: int, 
                   options: list[int]) -> bool:
    """
    Function to test if an integer is 
    in a list of options. 

    :param choice: integer 
    :type choice: int
    :param options: list of options
    :type options: list[int]
    
    :return bool: returns True if the integer is in the list
    """
    if (not isinstance(choice, int)  
        or len(options) == 0):
        return False
    
    if (choice in options): 
        return True
    else:
        return False

def make_a_new_choice(options: list[int]) -> int:
    """
    Function to request user to select an option from a list
    
    :param options: list of options to choose from
    :type options: list[int]
    
    :return choice: choice from the options list
    :type choice: int
    """
    optionstr: list[str] = list(map(str, options))
    optionstr_print: str = " ".join(optionstr)
    if len(optionstr) > 10:
        maxval: int = max(options)
        minval: int = min(options)
        if options == list(range(minval, maxval+1)):
            optionstr_print = f"in the range {minval} to {maxval}"
    
    while True:
        print("Choose from the options : "+optionstr_print)
        choicestr: str = input("or press Enter on its own to cancel  : ")
        choicestr.strip()
        if choicestr == "":
            return False
        elif choicestr in optionstr:
            choice: int = int(choicestr)
            break
        else:
            print(choicestr+" is not a valid option. Please try again.")
            
    return choice

def options() -> dict:
    """
    Function to define the flight options, 
        including information on hotel, and car rental
         
    :param None:
    
    :return options: flight_options dictionary, 
    KEY as index 
    VALUES as list of 
        (destination, 
        return flight price in GBP, 
        return flight carbon dioxide emissions per passenger in kg,
        hotel price per room in destination city per night in GBP
        car rental price in destination city per day in GBP)
    :type options: dict
    
    NB. carbon dioxide emissions from http://www.ecopassenger.org/ without climate factor
    """
    flight_options: dict = {
        "headline": ("key: destination : return flight price £ : "
                     "return carbon dioxide emissions kg : "
                     "hotel price per night £ : "
                     "car rental price per day £"),
        1: ("Glasgow", 29, 137, 7, 3), 
        2: ("Amsterdam", 55, 136, 13, 5),
        3: ("Paris", 60, 244, 25, 7),
        4: ("Rome", 75, 275, 19, 8)
    }
    return flight_options

def print_flight_options(flight_options: dict) -> None:
    """
    Function to print flight options to the screen
    
    :param flight_options: dictionary containing 
       information on flight destinations
    :type flight_options: dict
    
    :return None:
    """
    print("Flight options:")
    print("."*len(flight_options["headline"]))
    print(flight_options["headline"])
    for key in flight_options.keys():
        if type(key) == str:
            continue
        destination_properties = flight_options[key]
        print(str(key)+"  : "
                +destination_properties[0].ljust(11)+" : "
                +f"{destination_properties[1]: 21.2f}"+" : "
                +f"{destination_properties[2]: 10d}"+" "*24+" : "
                +f"{destination_properties[3]: 10.2f}"+" "*10+" : "
                +f"{destination_properties[4]: 10.2f}")
    print("."*len(flight_options["headline"]))
    
def input_city_flight(choice: int, 
                      suppress_print_messages: bool = False) -> int:
    
    """
    Function to check and/or input the destination city
        for the flights
    
    :param choice: destination city reference number
        of flight_options dictionary
    :type choice: int
    :param suppress_print_messages: option to suppress printing 
        messages to the screen
    :type suppress_print_messages: bool   
    
    :return num_nights: number of nights in the hotel
    """
    flight_options: dict = options()
    flight_option_keys: list[int] = (list(flight_options.keys()))[1:]
    
    is_choice: bool = choice_in_list(choice, flight_option_keys)
    if not is_choice:
        if not suppress_print_messages:
            print("Enter destination number:")
        city_flight_num: int = make_a_new_choice(flight_option_keys)
        if city_flight_num == False:
            return False
    else:
        city_flight_num = choice
    if not suppress_print_messages:
        print("Your destination: "+flight_options[city_flight_num][0])
        print("")
    return city_flight_num

def input_num_nights(num: int = 7, 
                     suppress_print_messages: bool = False) -> int:
    """
    Function to check and/or input the number of hotel 
        nights in the holiday
    
    :param num: number of nights in the hotel
    :type num: int
    :param suppress_print_messages: option to suppress printing 
        messages to the screen
    :type suppress_print_messages: bool    
    
    :return num_nights: number of nights in the hotel
    :type num_nights: int
    """
    maxlen: int = 90 # nights
    
    thislist: list = [*range(maxlen+1)]
    is_choice:bool = choice_in_list(num, thislist)
    if not is_choice: 
        if not suppress_print_messages:
            print("Enter number of nights in hotel:")
        num_nights: int = make_a_new_choice(thislist)
        if num_nights == False:
            return False
    else:
        num_nights = num
    
    if num_nights == 0:
        check: str = input("Press y to confirm no hotel required. ")
        if check == "y":
            return num_nights
        else:
            return False
        
    if num_nights > maxlen:
        print("Extended holidays of more than "
                +str(maxlen)
                +" days not allowed.")
        return False
    
    if not suppress_print_messages:
        print(f"Number of nights in hotel: {num_nights}")
        print("")
    return num_nights
        
def input_rental_days(num_rental_days: int = 4, 
                      num_nights: int = 4, 
                      suppress_print_messages: bool = False) -> int:
    """
    The number of days renting a car. 
    
    :param num_rental_days: number of days renting a car
    :type num_rental_days: int
    :param num_nights: number of nights in the hotel,
        cannot rent a car for more days than the number
        of nights in the hotel
    :type num_nights: int
    :param suppress_print_messages: option to suppress printing 
        messages to the screen
    :type suppress_print_messages: bool    
    
    :return rental_days: number of days renting a car
    """  
    thislist: list = [*range(num_nights+1)]
    is_choice: bool = choice_in_list(num_rental_days, thislist)
    if not is_choice:
        if not suppress_print_messages:
            print("Enter number of car rental days:")
        rental_days: int = make_a_new_choice(thislist)
        if rental_days == False:
            return False
    else:
        rental_days = num_rental_days
    
    if num_rental_days == 0:
        check = input("Press y to confirm you do not want to rent"
                " a car : ")
        if check == "y":
            rental_days = 0
            return rental_days
        else:
            return False

    if rental_days > num_nights:
        print("You cannot rent a car for more days "
                "than the number of nights you will "
                "be at your destination.")
        return False

    if not suppress_print_messages:
        print(f"Car rental days: {rental_days}")
        print("")
    return rental_days

def hotel_cost(hotel_cost_per_night: float, 
               num_nights: int,
               number_of_rooms: int) -> float: 
    """
    Function to calculate the total cost of the hotel
    
    :param hotel_cost_per_night: cost of one hotel room per night in GBP
    :type hotel_cost_per_night: float
    :param num_nights: number of nights
    :type num_nights: int
    :param number_of_rooms: number of rooms
    :type number_of_rooms: int
    
    :return hotel_cost_total: total cost of the hotel in GBP
    
    """
    hotel_cost_total:float = (number_of_rooms 
                              * hotel_cost_per_night
                              * num_nights)
    return hotel_cost_total

def flight_cost(flight_cost: float, 
                number_of_passengers: int) -> float:
    """
    Function to calculate the total cost of the flight. 
    
    :param flight_cost: cost of return flight per person in GBP
    :type flight_cost: float
    :param number_of_passengers: number of passengers 
    :type number_of_passengers: int
    
    :return flight_cost_total: total cost for flights in GBP
    :type flight_cost_total: float
    """
    flight_cost_total: float = flight_cost * number_of_passengers
    return flight_cost_total

def car_rental(car_rental_per_day: float, 
               rental_days: int,
               need_big_car:bool= False) -> float:
    """
    Function to calculate the total cost of car rental. 
    
    :param car_rental_per_day: cost of car rental for one day in GBP
    :type car_rental_per_day: float
    :param rental_days: number of days car rented
    :type rental_days: int
    
    :return car_rental_total: total cost of car rental in GBP
    :type car_rental_total: float
    """
    if need_big_car == True:
        size_car = 2
    else:
        size_car = 1
    car_rental_total: float = (size_car 
                               * car_rental_per_day 
                               * rental_days)
    return car_rental_total

def holiday_cost(hotel_cost: float, 
                 flight_cost: float, 
                 car_rental: float) -> float:
    """
    Function to calculate the total holiday cost. 
    
    :param hotel_cost: total hotel cost in GBP
    :type hotel_cost: float
    :param flight_cost: total return flight cost in GBP
    :type flight_cost: float
    :param car_rental: total car rental cost in GBP
    :type car_rental: float
    
    :return holiday_cost_total: total cost of holiday in GBP
    :type holiday_cost_total: float
    """
    holiday_cost_total: float = (hotel_cost
                                 + flight_cost
                                 + car_rental)
    return holiday_cost_total

def print_holiday_invoice(input_dictionary: dict,
                          invoice_dictionary: dict) -> bool:
    """
    Function to print an invoice for a holiday.

    :param input_dictionary: dictionary with the fields
    - customer_name (str): identifier string for the invoice
    - number_of_passengers (int): number of passengers 
    - holiday_start_date (str): string format starting date of the holiday
    :type input_dictionary: dict
    
    :param invoice_dictionary: dictionary with the fields
    - invoice_time (str): string format date identifying the invoice
    - num_nights (int): number of nights in the hotel
    - hotel_cost_total (float): total hotel cost in GBP 
    - flight_cost_total (float): total cost of return flights for 
      the number of passengers in GBP
    - rental_days (int): number of days renting the car
    - car_rental_total (float): total cost of car rental in GBP
    - holiday_cost_total (float): total cost of the holiday in GBP
    :type invoice_dictionary: dict
    
    :return bool: returns True
    """
    print("")
    print("")
    print("Invoice Reference : "+input_dictionary["customer_name"]
          +f" holiday for {input_dictionary['number_of_passengers']}"
          " passengers")
    print(f"                  : start date "
          +input_dictionary["holiday_start_date"])
    print("Invoice Date      : "+invoice_dictionary["invoice_time"])
    print("")
    print("Total cost of the hotel for "
          +f"{invoice_dictionary['num_nights']:2d} nights "+" "*3
          +f": £{invoice_dictionary['hotel_cost_total']:7.2f}")
    print("Total cost of the return flight"+" "*9
          +f" : £{invoice_dictionary['flight_cost_total']:7.2f}")
    print("Total cost of the car rental for "
          +f"{invoice_dictionary['rental_days']:2d} days"
          +f" : £{invoice_dictionary['car_rental_total']:7.2f}")
    final_string = ("The total cost of your holiday is "+" "*7
        +f": £{invoice_dictionary['holiday_cost_total']:7.2f}")
    print("="*len(final_string))
    print(final_string)
    print("="*len(final_string))
    print("")
    print("")
    return True

def check_input_dictionary(input_dictionary: dict) -> bool:
    """
    Function to check the input dictionary
    and add any keys and values that are not included

    :param input_dictionary: dictionary with keys for
    - customer name (str)
    - number of passengers (int)
    - holiday start date (str)
    - destination city number (int)
    - number of nights in hotel (int)
    - number of car rental days (int)
    - whether a big car is required (bool)
    :type input_dictionary: dict
    
    :returns bool: True if input dictionary has been updated
    """
    input_dictionary_keys: list[str] = \
        ["customer_name", 
        "number_of_passengers", 
        "holiday_start_date",
        "city_flight_option", 
        "num_nights_option", 
        "number_of_rooms", 
        "rental_days_option",
        "need_big_car"]
    input_dictionary_descriptions: list[str] = \
        ["customer name",
        "number of passengers (between 1-10)",
        "holiday start date",
        "destination city",
        "number of nights in a hotel",
        "number of rooms in a hotel \n(between 1-10 and not more than the number of passengers)", 
        "number of days renting a car",
        "if you need a car that seats more than 5 people"]
    input_dictionary_value_types: list[str] = \
        ["str", "int", "str", "int", "int", "int", "int", "bool"]
    input_dictionary_limits: list[tuple[int,int]] = \
        [(0,25), (1,10), (0,35), (0,90), (1, 10), (0,90), (False, True)]
        
    for i in range(len(input_dictionary_keys)):
        k: str = input_dictionary_keys[i]
        try:
            input_dictionary[k]
        except:
            if k not in ["city_flight_option", 
                         "num_nights_option", 
                         "rental_days_option"]:
                while True:
                    user_value: str = input(\
                        "Enter "
                        +input_dictionary_descriptions[i]+" ("
                        +str(input_dictionary_value_types[i])+") : ")
                    match input_dictionary_value_types[i]:
                        case "str":
                            if len(user_value) > input_dictionary_limits[i][1]:
                                print("String too long.")
                                continue
                            input_dictionary[k]  = user_value
                        case "int":
                            is_choice = choice_in_list(int(user_value), 
                                        [*range(input_dictionary_limits[i][0],
                                        input_dictionary_limits[i][1]+1)])
                            if (k == "number_of_rooms" 
                                and int(user_value) > input_dictionary["number_of_passengers"]):
                                continue
                            if is_choice == False: 
                                continue
                            input_dictionary[k]  = int(user_value)
                        case "bool":
                            if bool(user_value) not in [True, False]:
                                continue
                            input_dictionary[k]  = bool(user_value)
                    break
            else:
                input_dictionary[k]  = -1
    return True
    
def holiday(input_dictionary: dict, 
        suppress_print_option: bool = False, 
        suppress_print_messages: bool = False) -> bool:
    """
    Program to generate reports to 
    calculate a user's holiday cost 
    including the plane cost, hotel cost, and
    car rental cost.
    
    :param input_dictionary: holiday information with 
        optional input keys:
    - customer name (str)
    - number of passengers (int)
    - holiday start date (str)
    - destination city reference number (int)
    - number of nights in a hotel (int)
    - number of rooms in a hotel (int)
    - number of days renting a car (int)
    - if you need a car that seats 
        more than 5 people (bool)
    adds any keys not in the dictionary.
    :type input_dictionary: dict
    
    :param suppress_print_option: if true, don't 
        print the options to the screen
    :type suppress_print_option: boolean
    :param suppress_print_messages: if true, don't 
        print the acknowledgement messages
    :type suppress_print_messages: boolean
    
    :return bool: returns True
    """
    
    # Welcome splash screen
    if not suppress_print_messages:
        print("="*38)
        print("Welcome to the holiday booking system.")
        print("="*38)
    flight_options: dict = options()
    
    # Check input dictionary
    chk: bool = check_input_dictionary(input_dictionary)
    if input_dictionary["number_of_passengers"] > 10: 
        if not suppress_print_messages: 
            print("Sorry we do not do group booking")
            return False
    
    # Choose destination city, determines costs of hotel and car rental. 
    if not suppress_print_option:
        print_flight_options(flight_options)
    city_flight_num: int = input_city_flight(
        input_dictionary["city_flight_option"],
        suppress_print_messages=suppress_print_messages)
    if isinstance(city_flight_num, bool):
        if not suppress_print_option:
            print("No destination chosen. "
                  "Cancelling this holiday booking!")
        return False
    
    # Choose number of nights in hotel.
    num_nights: int = input_num_nights(
        input_dictionary["num_nights_option"],
        suppress_print_messages=suppress_print_messages)
    if isinstance(num_nights, bool) or num_nights == 0:
        if not suppress_print_option:
            print("You chose to stay 0 nights. "
                  "Cancelling this holiday booking!")
        return False
    
    # Choose number of days car rental.
    rental_days: int = input_rental_days(
        input_dictionary["rental_days_option"],
        num_nights=num_nights,
        suppress_print_messages=suppress_print_messages)
    if isinstance(rental_days, bool):
        if not suppress_print_option:
            print("You chose not to rent a car. "
                  "That's fine")
        rental_days = 0
                
    # Calculate invoice costs.
    hotel_cost_per_night: float = (flight_options[city_flight_num])[3]
    car_rental_per_day: float = (flight_options[city_flight_num])[4]
    flight_cost_return: float = (flight_options[city_flight_num])[1]
    
    hotel_cost_total: float = hotel_cost(
        hotel_cost_per_night, num_nights,
        input_dictionary["number_of_rooms"])
    flight_cost_total: float = flight_cost(flight_cost_return,
        input_dictionary["number_of_passengers"])
    
    if input_dictionary["number_of_passengers"] > 5:
        need_big_car: bool = True
    else:
        need_big_car = False
        
    car_rental_total: float = car_rental(car_rental_per_day, 
                                  rental_days,
                                  need_big_car=need_big_car)
    
    holiday_cost_total: float = holiday_cost(
        hotel_cost(hotel_cost_per_night, num_nights,
                   input_dictionary["number_of_rooms"]),
        flight_cost(flight_cost_return, 
                    input_dictionary["number_of_passengers"]),
        car_rental(car_rental_per_day, rental_days,
                   need_big_car=input_dictionary["need_big_car"]))
    
    # Print invoice.
    if not suppress_print_messages:
        print("Generating your invoice:")
    now: datetime.datetime = datetime.datetime.now()
    
    invoice_time: str = now.strftime("%d/%m/%Y %H:%M")
    
    invoice_dictionary: dict = dict(\
        invoice_time=invoice_time, 
        num_nights=num_nights, 
        hotel_cost_total=hotel_cost_total,
        flight_cost_total=flight_cost_total, 
        rental_days=rental_days, 
        car_rental_total=car_rental_total,
        holiday_cost_total=holiday_cost_total)
    
    print_holiday_invoice(input_dictionary,  
                          invoice_dictionary)
    
    return True
      
if __name__ == "__main__":  
    # Invoice 1
    booking1: dict = dict(customer_name = "Family 1", 
                    number_of_passengers = 3, 
                    holiday_start_date = "23rd July 2024",
                    city_flight_option = 1, 
                    num_nights_option = 7, 
                    number_of_rooms = 2, 
                    rental_days_option = 4,
                    need_big_car = False)
    hasbooked_1_7_4: bool = holiday(booking1,
                           suppress_print_option=True, 
                           suppress_print_messages=True)
    # Invoice 2
    booking2: dict = dict(customer_name = "Family 2", 
                    number_of_passengers = 2, 
                    holiday_start_date = "23rd July 2024",
                    city_flight_option = 1, 
                    num_nights_option = 21, 
                    number_of_rooms = 1,
                    rental_days_option = 6,
                    need_big_car = False)
    hasbooked_1_21_6: bool = holiday(booking2, 
                            suppress_print_option=True, 
                            suppress_print_messages=True)
    # Invoice 3
    booking3: dict = dict(customer_name = "Family 3", 
                    number_of_passengers = 5, 
                    holiday_start_date = "23rd July 2024",
                    city_flight_option = 3, 
                    num_nights_option = 7,
                    number_of_rooms = 2,
                    rental_days_option = 4,
                    need_big_car = False)
    hasbooked_2_7_4: bool = holiday(booking3,  
                           suppress_print_option=True, 
                           suppress_print_messages=True)
    # Invoice 4
    booking4: dict = dict(customer_name = "Family 4", 
                    number_of_passengers = 4, 
                    holiday_start_date = "23rd July 2024",
                    city_flight_option = 3, 
                    num_nights_option = 7,
                    number_of_rooms = 2,
                    rental_days_option = 4,
                    need_big_car = False)
    hasbooked_3_7_4: bool = holiday(booking4,  
                           suppress_print_option=True, 
                           suppress_print_messages=True)
    # Invoice 5
    booking5: dict = dict(customer_name = "Family 5", 
                    number_of_passengers = 2, 
                    holiday_start_date = "23rd July 2024",
                    city_flight_option = 4, 
                    num_nights_option = 7,
                    number_of_rooms = 1,
                    rental_days_option = 4,
                    need_big_car = False)
    hasbooked_4_7_4: bool = holiday(booking5, 
                           suppress_print_option=False, 
                           suppress_print_messages=False)
    
    # User input information
    booking6: dict = {}
    user_input_booking: bool = holiday(booking6)
  