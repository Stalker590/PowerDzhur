from fastapi import FastAPI, Request
from pydantic import BaseModel
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "Databases"))
sys.path.append(os.path.join(BASE_DIR, ".."))
from PowerDzhur_backend.Databases import database_users
from IP_ID import get_ip_info  # Припускаю, що ця функція приймає IP і повертає dict з country, region, timezone

app = FastAPI()

class UserData(BaseModel):
    name: str
    surname: str
    email: str
    phone: str
    # прибираємо country, region, timezone звідси — їх отримуємо на сервері автоматично

@app.post("/register")
async def register_user(user: UserData, request: Request):
    print("Received registration request")
    client_host = request.client.host  # IP користувача
    ip_info = get_ip_info(client_host)  # Має повертати dict з country, region, timezone

    db1 = database_users.DataBaseUsers()

    # Записуємо дані в БД
    print("Всьо заєбон,табличка пішла")
    insert_query = """
        INSERT INTO users (name, surname, email, phone, country, region, timezone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    print("Табличка э")

    print("Всьо,запис є")
    print(f"📩 Новий користувач: {user}")
    print(f"🌍 IP користувача: {client_host}")
    print(f"🗺️ Інформація про IP: {ip_info}")

    return {
        "status": "success",
        "message": "Користувача зареєстровано!",
        "ip": client_host,
        "ip_info": ip_info
    }

@app.get("/")
async def root():
    print("🔥 Вхідний POST /register")
    return {"message": "Привіт, все працює"}


#uvicorn main:app --reload
