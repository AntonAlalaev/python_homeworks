from fastapi import FastAPI, Path, HTTPException
from typing import List, Annotated
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request


# Создаем модель User, представляющую собой пользователя с полями id, username и age:
class User(BaseModel):
    id: int
    username: str
    age: int


# Создаем FastAPI приложение и настраиваем Jinja2 для загрузки шаблонов из папки templates
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")


# Загружаем исходные данные пользователей:
users: List[User] = [
    User(id=1, username="David Copperfield", age=54),
    User(id=2, username="John Smith", age=30)
]

# Напишите новый запрос по маршруту '/':
@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request":request, "users": users})


# Измените get запрос по маршруту '/user' на '/user/{user_id}':
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user_by_id(request: Request, user_id: Annotated[int, Path(ge=1)]) -> templates.TemplateResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")



# Добавьте новый POST запрос по маршруту '/user/{username}/{age}':
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      title="Enter username",
                                      description="The name must be between 5 and 20 characters long",
                                      example="Urban_user")],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='46')]) -> str:
    current_index = len(users) + 1
    users.append(User(id=current_index, username=username, age=age))
    return f"User {current_index} is registered"


# Добавьте новый PUT запрос по маршруту '/user/{user_id}/{username}/{age}':
@app.put("/user/{user_id}/{username}/{age}")
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


# Добавьте новый DELETE запрос по маршруту '/user/{user_id}':
@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail="User was not found")
