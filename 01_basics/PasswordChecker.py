username = input("Username:")
password = input("Password:")

passwordLenght = len(password)
pass_security = '*' * passwordLenght


print(f'{username}, your password {pass_security} is {passwordLenght} letters long!')