# 🎬 Film Search CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

Search and analyze movies stored in a MySQL database using a clean, interactive command-line interface. Query logs are stored in MongoDB and auto-maintained for performance.

---

## ✨ Features

- 🔍 **Search by keyword** — instantly filter films by title
- 🎞️ **Filter by genre and year range** — with full validation
- 📈 **Top-5 most popular queries** — from Mongo logs
- 🕓 **Last 5 unique queries** — for quick history reference
- 🧼 **Old logs auto-cleaned** (older than 30 days)
- 💡 **Rich CLI interface** with emoji, colors, and clean formatting


---

## 🗂 Project Structure
film_search/

├── main.py               # CLI interface logic

├── formatter.py          # Output formatting and stats display

├── log_writer.py         # MongoDB logger (with error handling)

├── log_stats.py          # Aggregation logic for queries

├── mysql_connector.py    # MySQL search queries

├── config.py             # Load settings from .env

├── requirements.txt      # Dependencies

└── .env.example          # Environment variable sample
## 🖥️ Technologies and stack

| Components    | Version   | Purpose                               |
|---------------|-----------|---------------------------------------|
| Python        | 3.10+     | CLI logic, scripts                    |
| MySQL         | 8.x / 5.7 | Storing the `sakila` database         |
| MongoDB       | 6.x / 5.x | Search logs and aggregation pipelines |
| rich          | 13.x      | Tabular output and color CLI         |
| pymysql       | 1.x       | Connecting to MySQL                  |
| pymongo       | 4.x       | Working with MongoDB                     |
| python‑dotenv | 1.x       | Loading secrets from `.env`           |

---

## ⚙️ Requirements

python >= 3.9

pymysql

pymongo

python-dotenv

rich

> **In total** the application was tested on macOS Sequoia 15.1.1.
---

## 🚀 How to Run

```bash
# 	1.	Clone the repo and go to the folder:
$ git clone https://github.com/newbusinessman1/film_search.git
$ cd film_search

# 2. Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies:
$ pip install -r requirements.txt

# 4. Fill the .env.example file with your data and rename it to .env
$ cp .env.example .env      # or create manually

# 5. Run the program:
$ python3 main.py

```

---

## 🔒 Safety & Error Handling

- try/except added for all external connections (MySQL & Mongo)
- Connection errors are caught and displayed clearly
- User input (like year range) is validated against type errors
- Logging to Mongo is suppressed if connection fails — no crash
- Logs older than 30 days are automatically deleted

---

## 🧪 Example Output

```bash

🎬 Film Search CLI
Search movies in the database

1. 🔍 Search by keyword
2. 🎯 Search by genre and year
3. 📊 Top 5 Popular Queries
4. 🕓 Last 5 unique queries
0. ❌ Exit

Your choice: _

```

---

# 📁 License

MIT (or specify otherwise)


---

# 🙌 Author

Oleksandr Kovalchuk  
[![GitHub](https://img.shields.io/badge/GitHub-121013?logo=github&logoColor=white)](https://github.com/newbusinessman1)  
[![Instagram](https://img.shields.io/badge/Instagram-%239B37A7.svg?logo=instagram&logoColor=white)](https://instagram.com/oldbusinessman)