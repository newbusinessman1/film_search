from dotenv import load_dotenv
import os

load_dotenv()

# ---------- MySQL(sakila) ----------
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DB", "sakila"),
}

# ---------- MongoDB ----------
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB  = os.getenv("MONGO_DB", "ich_edit")

# ---------- Для имени коллекции ----------
GROUP     = os.getenv("GROUP")
FULL_NAME = os.getenv("FULL_NAME")

PAGE_SIZE = 10