from fastapi import FastAPI, HTTPException

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def func_get() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def func_post(username: str, age: int) -> str:
    user_id = str(int(max(users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User  {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def func_put(user_id: str, username: str, age: int) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User  not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def func_delete(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User  not found")
    users.pop(user_id)
    return f"User  {user_id} has been deleted"
