friends = ['Anna', 'Mark', 'John', 'Anna', 'Sophie']

unique_friends = []
for friend in friends:
    if friend not in unique_friends:
        unique_friends.append(friend)

unique_friends.sort()

names_4digits = 0
for friend in unique_friends:
    if len(friend) > 4:
        names_4digits += 1

print(names_4digits)
print(unique_friends)

the_A_list = []
for friend in unique_friends:
    if friend.startswith("A"):
        the_A_list.append(friend)

print(the_A_list)
