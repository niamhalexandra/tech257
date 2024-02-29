import datetime

current_date = datetime.datetime.now()
current_year = current_date.year
current_month = current_date.month

age_int = int(input("How old are you? "))
month_str = input("What month were you born in? ")

birth_year = current_year - age_int
birth_month = monthsToIndexes[month_str]

if birth_month > current_month:
    birth_year = birth_year - 1

print(f"OMG, you are {age_int} years old and you were born in {birth_year}")

past_date = datetime(birth_year, birth_month, day=1, hour=0, minute=0, second=0)

difference = current_date - past_date

total_hours = difference.total_seconds() / 3600


# final part
birth_date = input("What is your date of birth? ")
current_date = datetime.now()
