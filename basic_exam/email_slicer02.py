#THIS PROGRAM NEEDS TO SLICE THE USER INPUT EMAIL INTO USERNAME AND DOMAIN
user_email = input("Please enter your email:")

index = user_email.find("@")
username = user_email[0:index]
domain = user_email[index+1 :]
print(f'Username: {username}')
print(f'Domain: {domain}')