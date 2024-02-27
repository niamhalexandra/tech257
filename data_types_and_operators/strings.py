
double_quotes_str = "Look! Double Quotes!"
single_quotes_str = 'Look! Single Quotes!'
print(double_quotes_str)
print(single_quotes_str)

# bad_str = 'I said 'Wow!' '

escape_str = 'I said \'Wow!\''
print(escape_str)
double_quotes_in_single_quotes_str = 'I said "Wow!" '
print(double_quotes_in_single_quotes_str)
single_quotes_in_double_quotes_str = "I said 'Wow!'"
print(single_quotes_in_double_quotes_str)

extra_spaces_str = "   Bob        "
print(len(extra_spaces_str))
print(len(extra_spaces_str.strip()))

example_str = "Here's some text with lot's of text"
print(example_str)
print(example_str.count("Fred"))

# all lowercase
print(example_str.lower())

# all uppercase
print(example_str.upper())

# capitalise first letter
print(example_str.capitalize())

# Replace something in string
print(example_str.replace(" with", ","))