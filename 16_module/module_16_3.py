from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def reg_new_user(username: Annotated[str, Path(min_length=5, max_length=20, discription="Enter username",
                                                   example="UrbanUser")],
                     age: Annotated[int,Path(ge=18, le=90, discription="Enter age", example="47")]) -> str:
    new_user = str(int(max(users, key=int))+1)
    users[new_user] = f'Имя: {username}, возраст: {age}'
    return f'User {new_user} is registered'

@app.put("/user/{user_id}/{username}/{age}")
async def update_user_list(user_id: Annotated[int, Path(gt=0)],
                           username: Annotated[str,Path(min_length=5, max_length=20)],
                           age: Annotated[int,Path(ge=18, le=90)]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
