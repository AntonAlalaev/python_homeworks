from fastapi import FastAPI, Path, HTTPException
from typing import List, Annotated
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()

users: List[User] = [
    User(id=1, username="David Copperfield", age=54),
    User(id=2, username="John Smith", age=30)
]


@app.get("/users")
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      title="Enter username",
                                      description="The name must be between 5 and 20 characters long",
                                      example="Urban_user")],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='46')]) -> str:
    current_index = len(users) + 1
    users.append(User(id=current_index, username=username, age=age))
    return f"User {current_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100,
                                     title="Enter user ID",
                                     description="User ID must be digit from 1 to 100",
                                     example="2")],
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      title="Enter username",
                                      description="The name must be between 5 and 20 characters long",
                                      example='Urban_user')],
        age: Annotated[int, Path(ge=18, le=120,
                                 title='Enter age',
                                 description="Age must be between 18 and 120",
                                 example='46')]) -> str:
    for item in users:
        if item.id == user_id:
            item.username = username
            item.age = age
        return f"User {user_id} has been updated"
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail="User was not found")
