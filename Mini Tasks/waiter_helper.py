# Rationale: To practice lists

# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hi there, welcome to waiter helper!")

# Print a list of starters
print("Please see below a list of starters:")
starters = "Garlic Bread OR Salad OR Soup"
print(starters)

# Take an input for the user for their starter
starter_choice = input("please enter the starter you would like to order: ")

# Print a list of mains
print("Please see below a list of Main Courses:")
print("Steak & Chips OR Burger & Fries OR Pizza")

# Take an input for the user for their main course
main_choice = input("please enter the main course you would like to order: ")

# Print a list of desserts
print("Please see below a list of Desserts:")
print("Cheesecake OR Chocolate Brownie OR Ice Cream")

# Take an input for the user for their dessert
dessert_choice = input("please enter the dessert you would like to order: ")

# Add each item ordered to a list called 'customer_order_list'
print("Please check your order is correct below: ")
customer_order_list = starter_choice , main_choice , dessert_choice
for element in customer_order_list:
    print(element)

# Use at least one f-string
# Print all of the user's choices
print(f"Just to confirm, you have ordered: {starter_choice}, {main_choice} & {dessert_choice}")




# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.