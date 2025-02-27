from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
users = []

@app.get("/")
async def wellcom():
    return f'Приветствую тебя, пользователь!'

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def all_users() -> list:
    return users

@app.post("/user/{username}/{age}")
async def reg_new_user(username: Annotated[str, Path(min_length=5, max_length=20, discription="Enter username",
                                                   example="UrbanUser")],
                     age: Annotated[int,Path(ge=18, le=90, discription="Enter age", example="47")]):
    new_id = max((j.id for j in users),default=0) + 1
    new_user = User(id=new_id,username =username, age = age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user_list(user_id: Annotated[int, Path(gt=0)],
                           username: Annotated[str,Path(min_length=5, max_length=20)],
                           age: Annotated[int,Path(ge=18, le=90)]):
    try:
        for user in users:
            if user.id ==user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user_id)
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")