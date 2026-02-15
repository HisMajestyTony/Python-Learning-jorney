#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) # b
print(new_list[-2]) # a
print(new_list[1:3]) # c
new_list[0] = 'z'
print(new_list) # z b c 

my_list = [1,2,3] 
bonus = my_list + [5] #1 2 8 or 1 2 3 5 ??
my_list[0] = 'z'
print(my_list) # z 2 3 
print(bonus) # z 2 3 8 or z 2 3 5 