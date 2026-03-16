import hashlib

password = "mydog123"

hashed = hashlib.sha256(password.encode())

print(hashed.hexdigest())


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



print(hash_password("hello123"))

