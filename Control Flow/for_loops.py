# starting code
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3], [4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}
# part 1 - loop through the list to print double of each number in 'list data'
for num in list_data:
    print(num * 2)

# part 2 - loop through 'embedded_lists', write loop to print the items, each item called data
for data in embedded_lists:
    print(data)

# part 3 - create another loop inside 'embedded_lists' for loop to list the individual items in the list
for new_list in embedded_lists:
    print(new_list)
    for data in new_list:
        print(data)
# part 4 write a for loop to loop through the dictionary so that it prints the keys
for key in dict_data:
    print(key)

# part 5 loop through dictionary and print values using value()
for value in dict_data.values():
    print(value)

# part 6 print the values of dictionary items inside dictionary, generate an embedded for loop (loop within loop)
for value in dict_data.values():
    for money_value in value.values():
        print(money_value)

# part 7 print specific values of the dictionary, write another loop through 'dict_data' but only print out money values
for value in dict_data.values():
    print(value["money"])

# part 8 use a nested if statement, write another loop to loop through items in 'list_data' and include a nested (indented) if statement inside the loop to check number/item in list
# A) if the number is less than 3 print 'less than 3'
# B) if number equals 3 then print 'I found three'
# C) if number greater than 3 then print 'greater than 3'
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
            print("I found 3")
    else:
        print("greater than 3")
