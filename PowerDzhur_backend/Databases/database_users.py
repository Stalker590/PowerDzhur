import psycopg2
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Поточний файл
sys.path.append(os.path.join(BASE_DIR, "..", ".."))  # Додаємо шлях до config
from config import DB_PASSWORD,DB_NAME,DB_USER,DB_HOST,DB_PORT

class DataBaseUsers:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME
            )
            print("✅ Успішне підключення до PostgreSQL!")
        except Exception as e:
            print("❌ Помилка підключення:", e)


    def execute_query(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            print("🔌 З'єднання з БД закрито.")

    def __del__(self):
        self.close()
