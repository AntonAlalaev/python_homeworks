from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(
        user_id: Annotated[int, Path(gt=1, le=100,
                                     title="Enter User ID",
                                     description="The ID must be integer greater than 0 and lower than 100")]):
    return f"Вы вошли как пользователь # {user_id}"


@app.get("/user")
async def get_user_info(username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      title="Enter User Name",
                                                      description="The name must be between 5 and 20 characters long",
                                                      pattern="^[a-zA-Z0-9_-]")],
                         age: Annotated[int, Path(gt=18, le=120,
                                              title="Enter Age",
                                              description="The age must be integer greater than 18 and lower than 120")]):
    return f"Информация о пользователе. Имя: {username}, возраст: {age}"
