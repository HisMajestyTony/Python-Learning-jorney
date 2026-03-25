from database import load_users, save_users

def get_all_users():
    return load_users()

def find_user_by_name(name: str):
    users = load_users()

    for user in users:
        if user["name"].lower() == name.lower():
            return user

    return None

def search_users(name: str):
    users = load_users()

    return [
        user for user in users
        if name.lower() in user["name"].lower()
    ]

def create_user(user):
    users = load_users()

    for u in users:
        if u["name"].lower() == user.name.lower():
            raise ValueError("User already exists")

    users.append(user.dict())
    save_users(users)

    return user

def delete_user(name: str):
    users = load_users()

    for i, user in enumerate(users):
        if user["name"].lower() == name.lower():
            users.pop(i)
            save_users(users)
            return True

    return False

def update_age(name: str, new_age: int):
    users = load_users()

    for user in users:
        if user["name"].lower() == name.lower():
            user["age"] = new_age
            save_users(users)
            return user

    return None

def oldest_user():
    users = load_users()

    old_user = max(users, key=lambda u: u["age"])

    if not old_user:
        return None

    return old_user

def get_users_count():
    users = load_users()
    return len(users)


def get_sort_users(order: str):
    users = load_users()

    if order == "asc":
        return sorted(users, key=lambda user: user["age"])
    elif order =="desc":
        return sorted(users, key=lambda user: user["age"], reverse=True)

    else:
        raise ValueError("Order must be 'asc' or 'desc'")



def get_age_range(min_age: int, max_age: int):
    if min_age > max_age:
        raise ValueError("min_age cannot be greater than max_age")

    users = load_users()

    return list(filter(lambda u: min_age <= u["age"] <= max_age, users))


def get_users_paginated(skip: int, limit: int):
    users = load_users()
    return users[skip: skip + limit]