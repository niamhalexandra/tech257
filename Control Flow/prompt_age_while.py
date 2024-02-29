# Let's standardise the input to get the age as digits...
age = input("What is your age? ")

user_prompt = True
while user_prompt:
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else: print("Please re-enter your age as a digit and ensure it doesn't exceed 117 years old!")

print(f"Your age is {age}")
