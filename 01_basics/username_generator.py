first_name = input("Enter first name:")
last_name = input("Enter last name:")
birth_year = input("Year of birth:")

username = first_name.lower() + "." + last_name.lower() + birth_year[2:4]
print(username)