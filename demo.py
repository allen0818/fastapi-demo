from fastapi import FastAPI

app = FastAPI()

@app.get('/book/{book_id}')
def get_book_by_id(book_id: int):
    return { "book_id": book_id }

@app.get("/users/me")
async def read_user_me():
    return { "user_id": "the current user" }

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return { "user_id": user_id }