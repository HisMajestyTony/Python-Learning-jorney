#THIS CODE SHOULD REMOVE THE DUPLICATES FROM A LIST
numbers = [1,2,3,2,4,1,5]

new_numbers = []

for number in numbers:
    if number in new_numbers :
        continue
    else: 
        new_numbers.append(number)
print(new_numbers)