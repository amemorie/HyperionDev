from datetime import datetime

def print_stock_report_to_file(printlines: list, today: datetime) -> None:
    """
    Function to print the stock report to a file.
    
    :param printlines: list of string containing the stock report, 
        one line per string
    :type printlines: list
    """
     
    while True:
        isprint: str = input("Would you like to print this stock report to a file? y/n : ")
        if isprint.lower() in ["y","n"]: 
            break
        else:
            print("Your input: "+isprint+" is not valid, please enter y or n")

    if isprint.lower() == "y":
        with open(today.strftime('%Y-%m-%d-%H-%M-%S-')+"stock-value-report.txt", "w", encoding="utf-8") as file:
            for lines in printlines:
                file.write(lines+"\n")

def print_stock_report(stock: dict, price: dict, 
                       total_stock_per_menu_item: dict, total_stock: float, 
                       today: datetime) -> None:
    """
    Function to print the stock report to the screen or to a file.
    
    :param stock: dictionary containing the menu item as key and 
        the number of each menu item that can be made from the 
        current stock as value
    :type stock: dict 
    :param price: dictionary containing the menu item as key 
        and the price of each menu item in GBP as value
    :type price: dict
    :param total_stock_value: dictionary containing the menu item as key 
        and total value of each menu item in the 
        current stock as value
    :type total_stock_value: dict
    :param total_stock: total value in GBP of all of the menu items in 
        the current stock
    :type total_stock: float
    :param today: the date and time when stock amounts were calculated
    :type today: datetime object
    """
    
    headerline: str = ("Menu item              : stock value : "
                       "price £  : total stock value £")
    footerline: str = "Total value of stock: £"

    # variables to help with table alignment
    headerlinelen: int = len(headerline)
    footerlinelen: int = len(footerline)
    diff_len: int = headerlinelen - footerlinelen - 8
    
    # list of output strings, one string per line
    printlines: list = ["Stock value report as of: "
                        + today.strftime('%d-%m-%Y %H:%M'),
                        "="*headerlinelen,
                        headerline,
                        "="*headerlinelen]
    
    for item in stock.keys(): 
        printlines.append(f"{item:23}: {stock[item]:11.0f} : "
                          f"{price[item]:7.2f} : "
                          f"{total_stock_per_menu_item[item]:19.2f}")
    
    printlines.extend(["="*headerlinelen, 
                       " "*diff_len+footerline+f"{total_stock: 4.2f}",
                       "="*headerlinelen])
    
    for lines in printlines:
        print(lines)
        
    print()
    print_stock_report_to_file(printlines, today)
    
def add_menu_items() -> list[str]:
    """
    Function to add menu items.
    Currently adds a fixed list of menu items.
    Update later to allow user to input new items.

    :param menu: menu item names as strings in a list
    :type menu: list 
    """
    menu: list[str] = ["Burger",
            "Battered cod",
            "Chicken Tikka Massala",
            "Pork chow mein"]
    return menu

def update_stock_value(menu) -> list[int]:
    """
    Function to update the stock value list.
    Currently adds a fixed stock value list.
    Update later to allow users to update the stock value of menu items.

    :param menu: list of menu item names as strings
    :type menu: list[str]
    :returns stock_value: list of stock value of menu items as integer types
    :type stock_value: list[int]
    """
    stock_value: list[int] = [10,15,25,55] # items
    if len(stock_value) != len(menu):
        raise ValueError("stock_value and menu are not the same length")
    return stock_value

def update_price_value(menu) -> list[float]:
    """
    Function to update the price of menu items.
    Currently adds a fixed price for each menu item.
    Update later to allow user to update the price of the menu items.

    :param menu: list of menu item names as strings
    :type menu: list[str]
    :returns price_value: list of price of each menu item as float 
        types in GBP
    :type price_value: list[int]
    """
    price_value: list[float] = [8.5, 9.5, 7.5, 10.0] # GBP
    if len(price_value) != len(menu):
        raise ValueError("price_value and menu are not the same length")
    return price_value

def calculate_stock_value(stock: dict, price: dict) -> tuple[float, dict]:
    """
    Function to calculate the stock value,
    for each menu item and a total for all items.
    :param stock: dictionary with 
        menu item names as strings in a list as the keys 
        and stock value for each menu item as the values
    :type menu: dict 
    :param price: dictionary with 
        menu item names as strings in a list as the keys 
        and price for each menu item as the values
    :type menu: dict 
    """
    total_stock: float = 0
    total_stock_per_menu_item: dict = {}
    for item in stock.keys(): 
        item_value: float = stock[item]*price[item]
        total_stock += item_value
        total_stock_per_menu_item[item] = item_value
    return total_stock, total_stock_per_menu_item

def cafe() -> None:
    """
    Cafe stock management programme.

    Prints stock management report to screen or an output file.
    The output file name is given as 
    "yyyy-mm-dd-hh-mm-ss-stock-value-report.txt"

    :param: None 
    :returns: None
    """
    menu: list[str] = add_menu_items()

    stock_value: list[int] = update_stock_value(menu)
    stock: dict = {}
    for item, stockitem in zip(menu, stock_value):
        stock[item] = stockitem

    price_value: list[float] = update_price_value(menu)
    price: dict = {}    
    for item, priceitem in zip(menu, price_value):    
        price[item] = priceitem

    total_stock: float
    total_stock_per_menu_item: dict
    
    total_stock, total_stock_per_menu_item \
        = calculate_stock_value(stock, price)
        
    today: datetime = datetime.now()

    print_stock_report(stock, price, 
                       total_stock_per_menu_item, total_stock, 
                       today)

if __name__ == "__main__":
    cafe()