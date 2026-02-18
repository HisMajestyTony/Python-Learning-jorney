#1 - EVEN CHECKER
def is_even(number):
    return number % 2 == 0

#2 - FULL NAME FORMATTER
def format_name(first , last):
    connected_names = str(first).capitalize() + " " + str(last).capitalize()
    return connected_names

#3 - CALCULATOR FUNCTION
def calculator(a, b, operation):
    total = 0
    if operation == "add":
        total = a + b
    elif operation == "sub":
        total = a - b
    elif operation == "mul":
        total = a * b
    elif operation == "div":
        if  b == 0:
            return "Cannot divide by zero"
        else :
            total = a / b
    else :
        return "Wrong operation requested"
    return total

#4 - LARGEST OF THREE
def largest(a, b, c,):
    larg = a
    nums = [a, b , c]
    for n in nums:
        if larg < n:
            larg = n
    return larg




#5 - COUNT VOWELS
def count_vowels(text):
    counter = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            counter+=1
    return counter

#6 - LIST CLEANER
def remove_duplicates(lst):
    new_list = []
    for char in lst:
        if char in new_list:
            pass
        else:
            new_list.append(char)
    return new_list


#7 - POWER FUNCTION - #HAD TO USE HELP ON THIS ONE
def power(base , exponent=2):
    return base ** exponent



#8 - FLEXIBLE ADDER
def add_all(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

#9 - USER PROFILE BUILDER - #USED HELP FROM GOOGLE ON THIS ONE TOO BECAUSE I WASNT FAMILIAR WITH KWARGS
def create_profile(**kwargs):
         return kwargs

#10 - COUNTER WITH CLOSURE
def counter():
    number = 0
    def de():
        nonlocal number
        number+=1
        return number
    return de
    

