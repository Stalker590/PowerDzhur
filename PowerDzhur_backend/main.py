from fastapi import FastAPI, Request
from pydantic import BaseModel
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname("/PowerDzhur_backend\Databases")))
from Databases import database_users
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
    client_host = request.client.host  # IP користувача
    ip_info = get_ip_info(client_host)  # Має повертати dict з country, region, timezone

    db1 = database_users.DataBaseUsers()
    db1.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            surname TEXT,
            email TEXT,
            phone TEXT,
            country TEXT,
            region TEXT,
            timezone TEXT
        );
    """)

    # Записуємо дані в БД
    insert_query = """
        INSERT INTO users (name, surname, email, phone, country, region, timezone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    db1.execute_query(insert_query, (
        user.name,
        user.surname,
        user.email,
        user.phone,
        ip_info.get("country", "Unknown"),
        ip_info.get("region", "Unknown"),
        ip_info.get("timezone", "Unknown")
    ))

    print(f"📩 Новий користувач: {user}")
    print(f"🌍 IP користувача: {client_host}")
    print(f"🗺️ Інформація про IP: {ip_info}")

    return {
        "status": "success",
        "message": "Користувача зареєстровано!",
        "ip": client_host,
        "ip_info": ip_info
    }


#uvicorn main:app --reload
