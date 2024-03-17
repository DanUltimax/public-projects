import os, colorama
from colorama import Fore, Back, Style

# Create global variables
global items
global cart
global menu

cart = []
menu = 0

""" HELPER FUNCTIONS """

# Clears the console
def clear_console():
    command = "clear" if os.name == "posix" else "cls"  
    os.system(command)
    
# Loads item information from the store database
def load_store(filename):
    items = []
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            item = {
                "Name": parts[0],
                "Category": parts[1],
                "Price": float(parts[2]),
                "Emoji": parts[3]
            }

            items.append(item)
    return items

# Function for storing the quantities of items
def quantity_handler(max):
    while True:
        quantity = int(input(Fore.BLUE + "Quantity: " + Fore.RESET))

        if quantity <= max and quantity > 0: #checks if quantity is in a valid range and puts the user in a loop
            break
        else:
            print(Fore.RED + "Invalid quantity." + Fore.RESET)
    return quantity

# Function for returning the user to the main menu
def return_to_menu():
    input(Fore.BLACK + "Press ENTER to continue..." + Fore.RESET)
    clear_console()
    display_menu()

# Displaying title headers for different parts of the program
def header(string):
    print(Fore.GREEN + "===================")
    print(Fore.WHITE + f"{string:^19}")
    print(Fore.GREEN + "===================")


""" STUDENT FUNCTIONS - complete below"""

# Displays the main menu
def display_menu():
    global menu
    header("MAIN MENU")
    if menu % 2 == 0:
        print(Fore.WHITE + """\n(b) Buy Item
(v) View Cart
(r) Remove Item
(c) Clear Cart
(help) Show/Hide help commands
(x) Quit
===========================================""")
    if menu % 2 == 1:
        print(Fore.WHITE + """\nType 'help' to toggle the menu commands
          
===========================================""")
    handle_commands()

# Handles main menu input
def handle_commands():
    choice = input(Fore.BLUE + "Enter Command... " + Fore.RESET)
    if choice == "b":
        buy_item()
    elif choice == "v":
        view_cart()
    elif choice == "r":
        remove_item()
    elif choice == "c":
        clear_cart()
    elif choice == "help":
        input(Fore.BLACK + "Press ENTER to continue..." + Fore.RESET)
        show_help()
    elif choice == "x":
        input(Fore.BLACK + "Press ENTER to continue..." + Fore.RESET)
        quit()
    else:
        print(Fore.RED + "Invalid command choice.")
        return_to_menu() #serves as a loop
    return choice

# Displays buy menu  
items = load_store('store.txt') #makes declaring the items list easier

def buy_menu():
    clear_console()
    header("BUY MENU")
    #column indicators
    print(Fore.YELLOW + f"{'#':<2} {'NAME':^9} {'CATEGORY':>17} {'PRICE':>9}       {'#':<2} {'NAME':^9} {'CATEGORY':>17} {'PRICE':>9}" + Fore.RESET)
    #     column 1                                                                  column 2

    for i in range(0, len(items), 2):
        item1 = items[i]
        print(Fore.WHITE + f"{i + 1:<2}: {item1['Emoji']:<3}{item1['Name']:<13} {item1['Category']:<12} {item1['Price']:<7}", end="     ")
        if i + 1 < len(items): #so that the items are displayed two in a row
             item2 = items[i + 1]
             print(Fore.WHITE + f"{i + 2:<2}: {item2['Emoji']:<3}{item2['Name']:<13} {item2['Category']:<12} {item2['Price']:<7}", end="     ")
        print()

# Buys an item and adds it to the shopping cart
def buy_item():
    global cart
    buy_menu()
    item_select = int(input(Fore.BLUE + "Choice: " + Fore.RESET))
    if item_select not in range(1, (len(items) + 1)): #if item_select is above or below 1-11, in this case.
        print(Fore.RED + "Invalid input." + Fore.RESET)
        input(Fore.BLACK + "Press ENTER to continue..." + Fore.RESET)
        clear_console()
        buy_item() #resets back to the beginning of the function


    if item_select in range(1, (len(items) + 1)):
        quantity = quantity_handler(99)

        item = items[item_select - 1]
        cart.append(item)

        print(f"{quantity} {item['Name']} purchased for ${(item['Price'] * quantity):.2f} (before tax)")
        item["Amount"] = quantity
        return_to_menu()
        return item["Amount"]

# Displays the contents of the shopping cart
def view_cart():
    clear_console()
    header("SHOPPING CART")
    global cart
    if cart == []: #checks if cart is empty
        print(Fore.RED + "No items in cart")
        return_to_menu()

    print(Fore.YELLOW + f"{'#':<3} {'NAME':>8} {'CATEGORY':>17} {'AMT':>7} {'PRICE':>9} {'TOTAL COST':>12}" + Fore.RESET)
    #column indicators. similar to buy menu, but fundamentally different.
    for i in range(0, len(cart)):
        item1 = cart[i]
        print(f"{i + 1:<2}: {item1['Emoji']:<3}{item1['Name']:<13} {item1['Category']:<12} {item1['Amount']:<7} ${item1['Price']:<6} ${(item1['Price'] * item1['Amount']):.2f}")

    subtotal = sum([item['Price'] * item['Amount'] for item in cart]) #stores all total prices in a list and adds them

    print(f"Subtotal     ${subtotal:.2f}")
    print(f"Tax (HST)    ${subtotal * 0.13:.2f}")
    print(f"TOTAL        ${subtotal + (subtotal * 0.13):.2f}")

# Removes an item from the shopping cart
def remove_item():
    clear_console()
    view_cart()
    while True:
        choice = int(input(Fore.BLUE + "Choice: " + Fore.RESET))
        if choice > len(cart) or choice <= 0:
            print(Fore.RED + "Invalid choice.")
        else:
            break

    item = cart[choice - 1]

    quantity = quantity_handler(item["Amount"])
    item["Amount"] -= quantity
    if item["Amount"] <= 0:
        cart.pop(choice - 1)
    print(f"{quantity} {item['Name']} removed from cart.")

# Clears the shopping cart
def clear_cart():
    clear_console()
    global cart
    view_cart()
    if input(Fore.BLUE + "\nAre you sure you want to clear the cart? (Y/N) " + Fore.RESET).strip().lower() == "y":
        cart = []
        print(Fore.GREEN + "Cart cleared!" + Fore.RESET)
    else:
        return_to_menu()

# Toggles the help menu (main menu)
def show_help():
    global menu
    clear_console()
    menu += 1
    display_menu()

# Calling Functions
display_menu() #only for initial startup

def main():
    global items

    colorama.init(autoreset=True)
    items = load_store("store.txt")

    # Main app loop
    while True:
        return_to_menu()


if __name__ == "__main__":
    main()