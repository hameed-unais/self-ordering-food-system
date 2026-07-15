food_menu = {
    "Ayam Bakar Set (Grilled Chicken Set)" : 5.80,
    "Dori Bakar set (Grilled Dori Set)" : 5.90,
    "Ayam Bakar Set (Grilled Boneless Chicken Set)" : 6.30,
    "Gulai Ayam Set (Curry Chicken Whole Leg Set)" : 6.20,
    "Ayam Penyet Set (Fried Chicken Set)" : 5.80,
    "Dori Penyet Set (Fried Dori Set)" : 5.90,
    "Ayam Penyet Set (Fried Boneless Chicken Set)" : 6.30,
    "Ayam Penyet Set (Fried Chicken Wing Set)" : 5.60
}
add_ons = {
    "Rice" : 0.50,
    "Egg" : 0.80,
    "Chili" : 0.50,
    "Fried/Grilled Dori Fish (per piece)" : 3.50,
    "Fried/Grilled Chicken Leg Quarter (per piece)" : 3.50,
    "Fried Chicken Wing (1pc)" : 1.50,
}

print("Welcome to our restaurant! Here is our menu:")
for items, prices in food_menu.items():
    print(f"{items}\t: \t${prices:.2f}")