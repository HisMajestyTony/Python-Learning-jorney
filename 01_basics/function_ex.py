def highest_even (lis) :
    highest = 0
    for number in lis:
        if number %2 == 0:
            if highest < number:
                highest = number
    return highest

print(highest_even([10,2,3,4,8,11]))