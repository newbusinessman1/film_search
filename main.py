from mysql_connector import (
    list_genres, year_bounds,
    search_by_keyword, search_by_genre_year
)
from log_writer import log_query
from log_stats import top_queries, recent_unique
from formatter import print_movies, print_stats
from config import PAGE_SIZE

MENU = """
=========== Film Search ==========
1. Поиск по ключевому слову
2. Поиск по жанру и диапазону годов
3. Топ-5 популярных запросов
4. Последние 5 уникальных запросов
0. Выход
==================================
"""

def run_keyword():
    kw = input("\nКлючевое слово: ").strip()
    off = 0
    while True:
        rows = search_by_keyword(kw, PAGE_SIZE, off)
        print_movies(rows)
        log_query("keyword", {"kw": kw})
        if len(rows) < PAGE_SIZE or input("Ещё 10? (Enter/y): ").lower() not in ("", "y"):
            break
        off += PAGE_SIZE

def run_genre_year():
    genres = list_genres()
    print("\nЖанры:", ", ".join(genres))
    genre = input("Жанр: ").strip()
    yb = year_bounds()
    print(f"Годы в базе: {yb['min_y']}–{yb['max_y']}")
    y1 = int(input("Год от: "))
    y2 = int(input("Год до: "))
    off = 0
    while True:
        rows = search_by_genre_year(genre, y1, y2, PAGE_SIZE, off)
        print_movies(rows)
        log_query("genre_year", {"genre": genre, "y1": y1, "y2": y2})
        if len(rows) < PAGE_SIZE or input("Ещё 10? (Enter/y): ").lower() not in ("", "y"):
            break
        off += PAGE_SIZE

def main():
    while True:
        print(MENU)
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            run_keyword()
        elif choice == "2":
            run_genre_year()
        elif choice == "3":
            print_stats(top_queries(), "Топ-5 запросов")
        elif choice == "4":
            print_stats(recent_unique(), "Последние 5 уникальных")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()