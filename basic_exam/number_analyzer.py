#THIS PROGRAM CAN DETERMINE IF THE NUMBER IS POSITIVE / NEGATIVE / ZERO / EVEN / ODD
number = int(input())

if number == 0:
    print("ZERO")
elif number > 0:
    if number %2 == 0:
        print(f'{number} -> Positive Even')
    else:
        print(f'{number} -> Positive Odd')
else :
    if number %2 == 0:
        print(f'{number} -> Negative Even')
    else:
        print(f'{number} -> Negative Odd')