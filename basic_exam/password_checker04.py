password = input("Please enter your new password:")

does_it_have_digit = any(char.isdigit() for char in password)
does_it_have_letter = any(char.isalpha() for char in password)
is_it_long_enough = len(password) >= 8

if does_it_have_digit and does_it_have_letter and is_it_long_enough:
    print("Strong password")
else:
    print("Weak password")