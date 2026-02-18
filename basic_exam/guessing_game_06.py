n = input()

current = 0
counter = 0
while current != n:
    current = input()
    counter+=1
print(f'Secret number{n}')
print(f'Attempts: {counter}')