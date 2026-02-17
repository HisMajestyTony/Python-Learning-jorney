numbers = [4, 7, 2, 9, 4, 2, 10, 15, 3]

end_result = {}
only_evens = []

for number in numbers:
    if number % 2 == 0:
        only_evens.append(number)
        end_result[number] = "Even"
    else:
        end_result[number] = "Odd"

evens_as_set = set(only_evens)

print(evens_as_set)
print(end_result)