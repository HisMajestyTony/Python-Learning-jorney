#THIS GAME KEEPS THE USER GESSING UNTIL HE GETS THE CORRECT NUMBER AND COUNTS THE ATTEMPTS
n = input()

current = 0
counter = 0
while current != n:
    current = input()
    counter+=1
print(f'Secret number{n}')
print(f'Attempts: {counter}')