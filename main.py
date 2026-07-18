#Deining the menu items and prices
food_menu = {
    "01":{"name":"Ayam Bakar Set", "transl": "Grilled Chicken Set", "price": 5.80},
    "02":{"name":"Dori Bakar Set", "transl": "Grilled Dori Set", "price": 5.90},
    "03":{"name":"Ayam Bakar Set", "transl": "Grilled Boneless Chicken Set", "price": 6.30},
    "04":{"name":"Gulai Ayam Set", "transl": "Curry Chicken Whole Leg Set", "price": 6.20},
    "05":{"name":"Ayam Penyet Set", "transl": "Fried Chicken Set", "price": 5.80},
    "06":{"name":"Dori Penyet Set", "transl": "Fried Dori Set", "price": 5.90},
    "07":{"name":"Ayam Penyet Set", "transl":"Fried Boneless Chicken Set", "price": 6.30},
    "08":{"name":"Ayam Penyet Set", "transl":"Fried Chicken Wing Set", "price":5.60}
}
add_ons = {
    "A1":{"name":"Rice", "price": 0.50,},
    "A2":{"name":"Egg", "price": 0.80,},
    "A3":{"name":"Chili", "price": 0.50,},
    "A4":{"name":"Fried/Grilled Dori Fish (per piece)", "price": 3.50,},
    "A5":{"name":"Fried/Grilled Chicken Leg Quarter (per piece)", "price": 3.50,},
    "A6":{"name":"Fried Chicken Wing (1pc)", "price": 1.50,},
}
shopping_cart = {} #storing the items user wants to order

#testing out functions before aking them into definitions
print("Penyet + BBQ Set Meal")
for item_no, item in food_menu.items():
    print(f"\n[{item_no}]/\t{item['name']:<30} : ${item['price']:.2f} \n\t{item['transl']}")
print("\nAdd-ons")
for add_on_no, add_on in add_ons.items():
    print(f"\n{add_on_no}/\t{add_on['name']:<30} : ${add_on['price']:.2f}")

input_item = input('\nPlease enter the item number you want to order (e.g., 01, 02, A1, A2):')
if input_item in food_menu:
    shopping_cart[input_item] = food_menu[input_item]
else:
    print("Invalid item number. Please try again.")
print(shopping_cart)
cart_total = sum(item['price'] for item in shopping_cart.values())
print(f"Total: ${cart_total:.2f}")