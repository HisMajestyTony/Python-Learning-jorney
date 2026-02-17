some_list = ['a','b','c','b','d','m','n','n']

seen = set()
duplicates = []

for symbol in some_list:
    if symbol in seen:
        duplicates.append(symbol)
    else:
        seen.add(symbol)

print(duplicates)