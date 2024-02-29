import datetime

date_now = datetime.datetime.now()
current_year = date_now.year

name_str = input("What is your name? ")
age_int = int(input("How old are you? "))
year_born = date_now.year - age_int


print(f"OMG, you are {age_int} years old so you were born in {year_born}")

# Third part - calculate total number of hours this person has lived

hours_lived = age_int * 8760
print(f"You have lived {hours_lived} hours")


