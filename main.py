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
            "[bold cyan]🎬 Film Search CLI[/bold cyan]\n[green]Search movies in the database[/green]",
            border_style="blue",
            padding=(1, 2)
        ))

        console.print("""[bold magenta]
[cyan]1.[/cyan] 🔍 Search by keyword
[cyan]2.[/cyan] 🎭 Search by genre and year
[cyan]3.[/cyan] 📊 Top 5 Popular Queries
[cyan]4.[/cyan] 🕒 Last 5 unique queries
[cyan]0.[/cyan] ❌ Exit
[/bold magenta]""")

        choice = input("Your choice: ").strip()

        if choice == "1":
            kw = input("Keyword: ").strip()
            offset = 0
            while True:
                rows = search_by_keyword(kw, PAGE_SIZE, offset)
                print_movies(rows)
                log_query("keyword", {"kw": kw})
                if len(rows) < PAGE_SIZE or input("More 10? (Enter/y): ").lower() not in ("", "y"):
                    break
                offset += PAGE_SIZE

        elif choice == "2":
            genres = list_genres()
            console.print("[bold green]Genre:[/bold green] " + ", ".join(genres))
            genre = input("Genre: ").strip()
            y = year_bounds()
            print(f"Years in DataBase: {y['min_y']}–{y['max_y']}")
            y1 = int(input("Year from: "))
            y2 = int(input("Year to: "))
            offset = 0
            while True:
                rows = search_by_genre_year(genre, y1, y2, PAGE_SIZE, offset)
                print_movies(rows)
                log_query("genre_year", {"genre": genre, "y1": y1, "y2": y2})
                if len(rows) < PAGE_SIZE or input("More 10? (Enter/y): ").lower() not in ("", "y"):
                    break
                offset += PAGE_SIZE

        elif choice == "3":
            print_stats(top_queries(), "📊 Top 5 Popular Queries")

        elif choice == "4":
            print_stats(recent_unique(), "🕒 Last 5 unique queries")

        elif choice == "0":
            print("👋🏻 Goodbye :)")
            break

if __name__ == "__main__":
    main()