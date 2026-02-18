#FINDS THE LARGEST NUMBER MANUALLY
nums = [14, 3, 77, 2, 99, 5]

largest = 0
for num in nums:
    if largest < num:
        largest = num
print(f'Largest: {largest}')