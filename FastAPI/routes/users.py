from fastapi import APIRouter, HTTPException
from models.user_model import User, MessageResponse, UserUpdate, CountResponse
from services.user_service import (
    get_all_users,
    find_user_by_name,
    search_users,
    create_user,
    delete_user,
    update_age, oldest_user, get_users_count,  get_sort_users, get_age_range, get_users_paginated
)

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[User])
def get_users(skip: int = 0, limit: int = 10):
    return get_users_paginated(skip, limit)


@router.get("/count", response_model=CountResponse)
def users_count():
    total = get_users_count()
    return {"count": total}


@router.get("/search", response_model=list[User])
def search_user(name: str):
    results = search_users(name)

    if not results:
        raise HTTPException(status_code=404, detail="User not found")

    return results

@router.get("/oldest", response_model=User)
def get_oldest_user():
    ancient_user = oldest_user()

    if not ancient_user:
        raise HTTPException(status_code=404, detail="There are no users in the database")

    return ancient_user


@router.get("/filter", response_model=list[User])
def filter_users(min_age: int, max_age: int):
    try:
        return get_age_range(min_age, max_age)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/sort", response_model=list[User])
def sort_users(order: str = "asc"):
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")

    users = get_sort_users(order)

    if not users:
        raise HTTPException(status_code=404, detail="There are no users in the database")

    return users


@router.get("/{name}", response_model=User)
def find_user_by_exact_name(name: str):
    user = find_user_by_name(name)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.delete("/{name}", response_model=MessageResponse)
def remove_user(name: str):
    deleted = delete_user(name)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}





@router.put("/{name}", response_model=User)
def update_user(name: str, data: UserUpdate):

    if data.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be positive")

    updated = update_age(name, data.age)

    if not updated:
        raise HTTPException(status_code=404, detail="User not found")

    return updated



@router.post("/", status_code=201, response_model=MessageResponse)
def add_user(user: User):
    try:
        create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "User added"}




