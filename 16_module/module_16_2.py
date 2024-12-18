from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI
@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{username}/{age}")
async def users_info(username: Annotated[str, Path(min_length=5, max_length=20, discription="Enter username",
                                                   example="UrbanUser")],
                     age: Annotated[int,Path(ge=18, le=120, discription="Enter age", example="47")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/{user_id}")
async def users_id(user_id: Annotated[int, Path(ge=1, le=100, discription="Enter User ID", example="55")]):
    return f"Вы вошли как пользователь № {user_id}"