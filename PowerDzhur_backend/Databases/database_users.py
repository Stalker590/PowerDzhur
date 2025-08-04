import psycopg2
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "..", ".."))
from config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT

class DataBaseUsers:
    def __init__(self):
        self.conn = None  # ← Обов'язково

    def connect(self):
        if self.conn:  # вже є з'єднання
            return
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
            self.conn = None

        self.execute_query("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    email TEXT,
                    phone TEXT,
                    country TEXT,
                    region TEXT,
                    timezone TEXT,
                    admin BOOLEAN DEFAULT FALSE NOT NULL
                    time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

    def execute_query(self, query: str, params=None, fetch: bool = False):
        self.connect()
        if not self.conn:
            print("⚠️ Немає з'єднання з БД.")
            return None
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = cursor.fetchall() if fetch else None
            self.conn.commit()
            cursor.close()
            return result
        except Exception as e:
            print(f"❌ Помилка запиту: {e}")
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None  # ← щоб уникнути повторного закриття
            print("🔌 З'єднання з БД закрито.")

    def __del__(self):
        self.close()
