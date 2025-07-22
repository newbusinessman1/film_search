from mysql_connector import (
    list_genres, year_bounds,
    search_by_keyword, search_by_genre_year
)
from log_writer import log_query
from log_stats import top_queries, recent_unique
from formatter import print_movies, print_stats
from config import PAGE_SIZE

from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    while True:
        console.print(Panel.fit(
            "[bold cyan]🎬 Film Search CLI[/bold cyan]\n[green]Поиск фильмов по базе данных[/green]",
            border_style="blue",
            padding=(1, 2)
        ))

        console.print("""[bold magenta]
[cyan]1.[/cyan] 🔍 Поиск по ключевому слову
[cyan]2.[/cyan] 🎭 Поиск по жанру и годам
[cyan]3.[/cyan] 📊 Топ-5 популярных запросов
[cyan]4.[/cyan] 🕒 Последние 5 уникальных запросов
[cyan]0.[/cyan] ❌ Выход
[/bold magenta]""")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            kw = input("Ключевое слово: ").strip()
            offset = 0
            while True:
                rows = search_by_keyword(kw, PAGE_SIZE, offset)
                print_movies(rows)
                log_query("keyword", {"kw": kw})
                if len(rows) < PAGE_SIZE or input("Ещё 10? (Enter/y): ").lower() not in ("", "y"):
                    break
                offset += PAGE_SIZE

        elif choice == "2":
            genres = list_genres()
            console.print("[bold green]Жанры:[/bold green] " + ", ".join(genres))
            genre = input("Жанр: ").strip()
            y = year_bounds()
            print(f"Годы в базе: {y['min_y']}–{y['max_y']}")
            y1 = int(input("Год от: "))
            y2 = int(input("Год до: "))
            offset = 0
            while True:
                rows = search_by_genre_year(genre, y1, y2, PAGE_SIZE, offset)
                print_movies(rows)
                log_query("genre_year", {"genre": genre, "y1": y1, "y2": y2})
                if len(rows) < PAGE_SIZE or input("Ещё 10? (Enter/y): ").lower() not in ("", "y"):
                    break
                offset += PAGE_SIZE

        elif choice == "3":
            print_stats(top_queries(), "📊 Топ-5 популярных запросов")

        elif choice == "4":
            print_stats(recent_unique(), "🕒 Последние 5 уникальных запросов")

        elif choice == "0":
            print("👋🏻 Goodbye :)")
            break

if __name__ == "__main__":
    main()