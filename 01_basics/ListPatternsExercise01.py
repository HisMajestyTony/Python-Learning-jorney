#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = 'Stanley'
friends.append(new_friend)

print(sorted(friends))



numbers = [1, 2, 3]
extra = [4, 5]

numbers.append(extra)
print(numbers)


names = ['Alice', 'Charlie']
new_names = ['Bob', 'David']

names.extend(new_names)


print(sorted(names))