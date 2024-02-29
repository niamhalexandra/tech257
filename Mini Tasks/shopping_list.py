# Create a list called 'shopping_list' with the following items:
# eggs
# bread
# bananas
# biscuits
# milk
from typing import List

shopping_list: list[str] = ["eggs", "bread", "bananas", "biscuits", "milk"]
# Print the list to the screen
print(shopping_list)
# Print the data type of 'shopping_list'
print(type(shopping_list))
# Print the first item in the list
print(shopping_list[0])
# Print the last item in the list
print(shopping_list[4])
# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
shopping_list[1] = "Rice"
print(shopping_list[1])
# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '=')
shopping_list.append("carrot")
print(shopping_list)
# check the length of the list (which should now have 6)
print(len(shopping_list))
# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
shopping_list.extend(["toffee", "coffee"])
# Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
print(shopping_list)
# Remove "bananas" from 'shopping_list'
shopping_list.remove("bananas")
# Print 'shopping_list' to check it's been removed.
print(shopping_list)
# Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
coffee_removed = shopping_list.pop()
print(shopping_list)

