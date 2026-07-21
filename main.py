#Deining the menu items and prices
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
#printing menu items and prices
def print_menu():
    print("Penyet + BBQ Set Meal")
    for item_no, item in FOOD_MENU.items():
        print(f"\n[{item_no}]/\t{item['name']:<30} : ${item['price']:.2f} \n\t{item['transl']}")
    print("\nAdd-ons")
    for add_on_no, add_on in ADD_ONS.items():
        print(f"\n{add_on_no}/\t{add_on['name']:<30} : ${add_on['price']:.2f}")
#getting user input for ordering items
def get_order():
    while True:
        input_item = input('\nPlease enter the item number you want to order (e.g., 01, 02, A1, A2):')
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
        if remove_choice.lower() == 'cancel':
            return
        if remove_choice in shopping_cart:
            qty_to_remove = int(input(f"How many to remove? (currently {shopping_cart[remove_choice]['qty']})"))

            if qty_to_remove >= shopping_cart[remove_choice]['qty']:
                del shopping_cart[remove_choice]
                print("Item fully removed from cart.")
            else:
                shopping_cart[remove_choice]['qty'] -= qty_to_remove
                print(f"Removed {qty_to_remove}. {shopping_cart[remove_choice]['qty']} remaining.") 
                break
        else:
            print("That item is not in your cart. Please try again")
            
#the summary and receipt of the order
def order_summary(order):
    print("\nOrder Summary:")
    total_price = 0
    for item in order.values():
        total_total = item['price'] * item['qty']
        if 'transl' in item:
            print(f"\t{item['name']:<30} x{item['qty']} : ${total_total:.2f} \n\t{item['transl']}")
        else:
            print(f"\t{item['name']:<30} x{item['qty']} : ${total_total:.2f}")
        total_price += total_total
    print(f"\nTotal: ${total_price:.2f}")
 
#Shows the items in cart and total after every input   
def items_in_cart(order):
    total_price = 0
    total_qty = 0
    for item in order.values():
        total_price += item['price'] * item['qty']
        total_qty += item['qty']
    print(f"\nNumber of items in cart: {total_qty}")
    print(f"Cart Total: ${total_price:.2f}")

#Applying NYP student/ staff discount
#def discount_nyp():
    #print("\nDiscounts" \
    #"\n[01] NYP student discount (10% \disocunt)" \
   # "\n[02] NYP staff discount (5% \discount)")
    #while True:
       # eligibility = input("Enter [01] or [02] for any eligible discount. Enter 'next' if not eligible:")
       # if eligibility == '01':
            #for item in order.values():
            
    
while True:
    print_menu()
    get_order()
    items_in_cart(order)

    remove_choice = input("\nDo you want to remove an item\nPlease enter 'y; for yes and 'n' for no: ")
    if remove_choice.lower().strip():
        remove_item()
        items_in_cart(order)


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
        continue
    order_summary(order)
    break_programme = False
    while True:
        opinion2 = input("\nDo you want to confirm your order?\nPlease enter 'y' for yes and 'n' for no: ")
        if opinion2.lower() == 'y':
            break_programme = True
            break
        if opinion2.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'no'")
    if break_programme:
        break