#print time in receipt like actual receipts
from datetime import datetime
def get_timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

#want an order system like mcdonalds.
import random
def order_number():
    return random.randint(100, 999)

#Defining the menu items and prices
FOOD_MENU = {
    "01":{"name":"Ayam Bakar Set", "transl": "Grilled Chicken Set", "price": 5.80},
    "02":{"name":"Dori Bakar Set", "transl": "Grilled Dori Set", "price": 5.90},
    "03":{"name":"Ayam Bakar Set", "transl": "Grilled Boneless Chicken Set", "price": 6.30},
    "04":{"name":"Gulai Ayam Set", "transl": "Curry Chicken Whole Leg Set", "price": 6.20},
    "05":{"name":"Ayam Penyet Set", "transl": "Fried Chicken Set", "price": 5.80},
    "06":{"name":"Dori Penyet Set", "transl": "Fried Dori Set", "price": 5.90},
    "07":{"name":"Ayam Penyet Set", "transl":"Fried Boneless Chicken Set", "price": 6.30},
    "08":{"name":"Ayam Penyet Set", "transl":"Fried Chicken Wing Set", "price":5.60}
}
ADD_ONS = {
    "A1":{"name":"Rice", "price": 0.50,},
    "A2":{"name":"Egg", "price": 0.80,},
    "A3":{"name":"Chili", "price": 0.50,},
    "A4":{"name":"Fried/Grilled Dori Fish (per piece)", "price": 3.50,},
    "A5":{"name":"Fried/Grilled Chicken Leg Quarter (per piece)", "price": 3.50,},
    "A6":{"name":"Fried Chicken Wing (1pc)", "price": 1.50,},
}
shopping_cart = {} #storing the items user wants to order
order = shopping_cart

#choose to dine-in or take-away
def get_order_type():
    while True:
        order_type = input("Welcome, Is this for Dine-in or Takeaway? (d/t): ")
        if order_type.lower() == 'd':
            return "Dine-in"
        elif order_type.lower() == 't':
            return "Takeaway"
        else:
            print("Invalid input. please enter 'd' or 't'.")

#printing menu items and prices
def print_menu():
    print("\nPenyet + BBQ Set Meal".center(91))
    print("=" * 91)

    food_list = list(FOOD_MENU.items())
    for i in range(0, len(food_list), 2):
        row = food_list[i:i+2]

        name_line = ""
        transl_line = ""
        for no, item in row:
            name_line += f"[{no}] {item['name']:<30} ${item['price']:.2f}".ljust(50)
            transl_line += f"    {item['transl']}".ljust(50)

        print(name_line)
        print(transl_line)
        print()   # blank line between rows for spacing

    print("\nAdd-ons")
    print("-" * 91)
    for add_on_no, add_on in ADD_ONS.items():
        print(f"\n{add_on_no}/\t{add_on['name']:<30} : ${add_on['price']:.2f}")
#I converted the dictionary into a list to make it so that I can index and splice the dictionary to make the above code possible
#Instead of len(food_list) I could literally just put 8, but I just put it and it looks better
# [i:i+2] just give every two menu items.
#I had a difficult time with the tranlation for the menu items as \n 'transl' absolutely messes up my code and the 'transl'
# - for [06] in particular keep extending to the price so I had to add more padding.

#getting user input for ordering items
def get_order():
    while True:
        input_item = input('\nPlease enter the item number you want to order (e.g., 01, 02, A1, A2): ')
        if input_item in FOOD_MENU or input_item in ADD_ONS:
            while True:
                try:
                    qty = int(input("Enter quantity: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")

            if input_item in shopping_cart:
                shopping_cart [input_item]['qty'] += qty
            else:
                if input_item in FOOD_MENU:
                    shopping_cart[input_item] = FOOD_MENU[input_item].copy()
                else:
                    shopping_cart[input_item] = ADD_ONS[input_item].copy()
                shopping_cart[input_item]['qty'] = qty
            break
        else:
            print("Invalid item number. Please try again.")
#what this code does is get what the user wants to order and store it into shopping_cart. However, if the user chooses the same item twice,
# -there will not be an additional copy so I had figure out a solution which was .copy() which just copied the equation instead of equating keys
#if it is the first time that the user orders that item, then it routes him to add ['qty'] in his nested dict keys

#Remove items from cart
def remove_item():
    if not shopping_cart:
        print("\nYour cart is empty. Nothing to remove")
        return
    print("\nItems in your cart:")
    for item_no, item in shopping_cart.items():
        if 'transl' in item:
            print(f"[{item_no}]\t{item['name']:<30} x{item['qty']} : ${item['price']:.2f} \n\t{item['transl']}")
        else:
            print(f"[{item_no}]\t{item['name']:<30} x{item['qty']} : ${item['price']:.2f}")
    while True:
        remove_choice = input("\nEnter the item number to remove the item / Enter 'cancel' to go back: ")
        if remove_choice.lower().strip() == 'cancel':
            return
        if remove_choice in shopping_cart:
            qty_to_remove = int(input(f"How many to remove? (currently {shopping_cart[remove_choice]['qty']})"))
            if qty_to_remove >= shopping_cart[remove_choice]['qty']:
                del shopping_cart[remove_choice]
                print("Item fully removed from cart.")
                break
            else:
                shopping_cart[remove_choice]['qty'] -= qty_to_remove
                print(f"Removed {qty_to_remove}. {shopping_cart[remove_choice]['qty']} remaining.") 
                break
        else:
            print("That item is not in your cart. Please try again")
#'transl' only exists in food menu and not addons, so had to differentiate them with an if statement
            
#the summary and view cart
def order_summary(discount_rate):
    print("\nOrder Summary:")
    total_price = 0
    for item in order.values():
        each_total = item['price'] * item['qty']
        if 'transl' in item:
            print(f"\t{item['name']:<30} x{item['qty']} : ${each_total:.2f} \n\t{item['transl']}")
        else:
            print(f"\t{item['name']:<30} x{item['qty']} : ${each_total:.2f}")
        total_price += each_total

    discount_amount = total_price * discount_rate
    final_total = total_price - discount_amount

    print(f"\nSubtotal :${total_price:.2f}")
    if discount_rate > 0:
        print(f"Discount ({discount_rate*100:.0f}%): -${discount_amount:.2f}")
    print(f"\nTotal: ${final_total:.2f}")

    return final_total, total_price, discount_rate, discount_amount

 #print receipt
def print_receipt(order, order_no, order_type, timestamp, total, subtotal, discount_rate, discount_amount):
    print("=" * 40)
    print("      PENYET + BBQ SET MEAL".center(40))
    print("=" * 40)
    print(f"ORDER NO:".center(40))
    print(f"{order_no}".center(40))
    print("=" * 40)
    print(f"{order_type}".ljust(20) + f"{timestamp}".rjust(20))
    print("-" * 40)

    for item in order.values():
        each_total = item['price'] * item['qty']
        print(f"{item['name']:<24}{f'x{item['qty']}':<6}${each_total:>6.2f}")

    print("-" * 40)
    print(f"{'Subtotal':<30}${subtotal:>8.2f}")
    if discount_rate > 0:
        print(f"{'Discount (' + str(int(discount_rate*100)) + '%)':<30}$ -{discount_amount:>7.2f}")
    print(f"{'TOTAL':<30}${total:>8.2f}")
    print("=" * 40)
    print("Thank you! Please collect".center(40))
    print(f"your order at counter #{order_no}".center(40))
    print("=" * 40)
#Really did not want to copy the whole formulas from summary to receipt so I just returned the summary values.

#Shows the items in cart and total after every input   
def items_in_cart():
    total_price = 0
    total_qty = 0
    for item in order.values():
        total_price += item['price'] * item['qty']
        total_qty += item['qty']
    print(f"\nNumber of items in cart: {total_qty}")
    print(f"Cart Total: ${total_price:.2f}")

#Applying NYP student/ staff discount
def discount_nyp():
    print("\nDiscounts"
    "\n[01] NYP student discount (10% discount)"
    "\n[02] NYP staff discount (5% discount)")
    while True:
        eligibility = input("Enter [01] or [02] for any eligible discount. Enter 'next' if not eligible: ")
        if eligibility == '01':
            print("10% student discount applied")
            return 0.10
        elif eligibility == '02':
            print("5% staff discount applied")
            return 0.05
        elif eligibility == 'next':
            return 0.0
        else:
            print("Invalid input. Please try again.")

#Payment methods. Mostly mock since this is just for the immersion.
def process_payment(total):
    while True:
        method = input("\nSelect payment method:\n[1] Cash\n[2] Card\nEnter choice: ")
        if method == '1':
            while True:
                amount_paid = float(input(f"Total is ${total:.2f}. Enter cash amount: "))
                #Need to enter the right amount of money or will show error sign or give change
                if amount_paid >= total:
                    change = amount_paid - total
                    print(f"Payment successful. Change: ${change:.2f}")
                    return
                else:
                    print("Insufficient amount. Please try again.")
        elif method == '2':
            print("Processing card payment...")
            print("Payment successful.")
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

#main spine
#you start with a clean cart every loop which explain shopping_cart.clear()
while True:
    shopping_cart.clear()
    order_type = get_order_type()

    while True:
        print_menu()
        get_order()
        items_in_cart()

        while True:
            remove_choice = input("\nDo you want to remove an item\nPlease enter 'y' for yes and 'n' for no: ")
            if remove_choice.lower().strip() == 'y':
                remove_item()
                items_in_cart()
                break
            elif remove_choice.lower().strip() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        continue_programme = False
        while True:
            opinion = input("\nDo you want to add more items?\nPlease enter 'y' for yes and 'n' for no: ")
            if opinion.lower().strip() == 'y':
                continue_programme = True
                break
            elif opinion.lower().strip() == 'n':
                break
            else:
                print("invalid input. Please enter 'y' or 'no'")

        if continue_programme:
            continue  # they want more items then it loop back

        # customer is done adding items and proceeds to check out
        order_no = order_number()
        time = get_timestamp()
        discount_rate = discount_nyp()
        total, total_price, discount_rate, discount_amount = order_summary(discount_rate)

        while True:
            opinion2 = input("\nDo you want to confirm your order?\nPlease enter 'y' for yes and 'n' for no: ")
            if opinion2.lower() == 'y':
                process_payment(total)
                print(" ")
                print_receipt(order, order_no, order_type, time, total, total_price, discount_rate, discount_amount)
                break
            elif opinion2.lower() == 'n':
                print("\nOrder cancelled")
                break
            else:
                print("Invalid input. Please enter 'y' or 'no'")

        break #either confirm or not, pushes you back to outer loop for customer

    print("\n\n" + "=" * 40)
    print("Resetting Ordering System...".center(40))
    print("=" * 40 + "\n")
