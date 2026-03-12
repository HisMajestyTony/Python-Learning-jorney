def fib(number):

    a = 0
    b = 1

    for i in range(number):
        yield a
        temp_a = a
        a = b
        b = temp_a + b

for x in fib(20):
    print(x)