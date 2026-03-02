from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args , **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5

user1 = {
    'name': 'Sorna',
    'valid': True}


def authenticated(fn):

    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)