from fastapi import FastAPI


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def func_get() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def func_post(user = str, username = str, age = str) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def func_put(user = str, user_id = str, username = str, age = str) -> dict:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return "The user <user_id> is updated"

app.delete("/user/{user_id}")
async def func_delete(user_id = str) -> str:
    users.pop(user_id)
    pass
