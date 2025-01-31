from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                       title="Enter username",
                                       description="The name must be between 5 and 20 characters long",
                                       example="Urban_user")],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='46')]):
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return (f"User {current_index} is registered")


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
         age: Annotated[int, Path(ge=18, le=100,
                              title='Enter age',
                              description = "Age must be between 18 and 120",
                              example='46')]):
     users[user_id] = f"Имя: {username} возраст {age}"
     return (f"User {user_id} has been updated")


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
     users.pop(user_id)
     return (f"User {user_id} has been deleted")
