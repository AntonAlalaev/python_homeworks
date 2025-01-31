from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users() -> list:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(ge=5, le=20,
                                      description='Enter username',
                                      examples='Urban_user')],
        age: int = Path(ge=18, le=100, discription='Enter age', examples='51')) -> dict:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return (f"User {current_index} is registered")


@app.put('/user/{username}/{user_id}/{age}')
async def update_user(
        user_id: str = Path(ge=5, le=20,
                            description='Enter username',
                            examples='Urban_user'),
        username: str = Path(ge=18, le=100,
                             discription='Enter age',
                             examples='51'),
        age: int = 30) -> dict:
    users[user_id] = user_id, username, age
    return (f"User {user_id} has been updated")


@app.delete('/user/{user_id}')
async def delite_user(user_id: str) -> str:
    users.pop(user_id)
    return (f"User {user_id} has been deleted")