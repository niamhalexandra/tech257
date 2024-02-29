# Make a dictionary "student_1"
student_1 = {
    'name': 'Susan',
    'stream': 'tech',
    'completed_lessons': 4,
'completed_lessons_names': ["variables", "data types", "set up"]
}
# Dictionaries save/structure data by storing pairs of keys and values (as opposed to a regular dictionary that stores words and definitions
# keys are like words & values are like their meanings
# Print the dictionary to the screen
print(student_1)
# Print it's data type to check it's a dictionary
print(type(student_1))
# Print the value for the key-value pair having the key "stream"
print(student_1['stream'])
# Print the value for 'completed_lesson_names' check for list of 3 items
print(student_1['completed_lessons_names'])
# Print the data type for the value for 'completed_lessons_name', check it's a list
print(type(student_1['completed_lessons_names']))
# Print the first element (should be "variables")
print(student_1['completed_lessons_names'][0])
# Change the value of "completed_lessons" to 3 (an integer not string) and print
student_1['completed_lessons']= 3
print(student_1)
# Delete "data_types" from the list of 'completed_lesson_names'
student_1['completed_lessons_names'].remove("data types")
# Use keys() method on dictionary to list all keys
print(student_1.keys())