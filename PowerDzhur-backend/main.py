from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Створюємо модель для очікуваних даних
class UserData(BaseModel):
    name: str
    surname: str
    email: str
    phone: str

@app.post("/register")
async def register_user(user: UserData):
    print(f"Новий користувач: {user}")
    return {"status": "success", "message": "Користувача зареєстровано!"}