#Initialise x with the value of 0
x = 0

#Create a while statement so that it loops while x'' is less than 10 everytime it loops it should: Print the value of 'x' to the screen in an f-string
while x < 10:
    print(f"print x -> {x}")

# Increment (add 1 to x)
# without doing this increment 0 would loop and output over and over again
    x += 1

# when code is run with first line commented out, we get the name error: name 'x' is not defined

# copy while loop, modifying it o that it breaks when x = 4
x = 0
while x < 10:
    print(f"print x -> {x}")

    x += 1

    if x == 5:
        break