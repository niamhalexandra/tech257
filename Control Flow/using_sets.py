# Explain 2 main ways that sets are different to lists and tuples
# Sets are:

# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {'apple', 'banana', 'cherry'}
# Print the set 'fruits'
print(fruits)
# Add "orange" to the fruits set using one of the set's methods.
fruits.add('orange')
# Print the set 'fruits' - check it's added
print(fruits)
# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove('banana')
# Print the set 'fruits' - check it's removed
print(fruits)
# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add('apple')
# Print fruits now with the added apple
print(fruits)
#What do you observe? Apple is not printed as an additional because sets are designed for elements to be unique
# Print the 2nd item in the set. If there is any problem doing this, explain.
# print(fruits[1])
fruits_list = list(fruits)
print(fruits_list[1])
# You cannot print an item in a set because they are unordered, items having no index means you can't access items directly
# You could potentially convert them to a list instead to access an item individually