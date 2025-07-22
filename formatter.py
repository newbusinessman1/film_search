from rich.table import Table
from rich.console import Console

console = Console()

def print_movies(rows):
    if not rows:
        console.print("[yellow]Ничего не найдено[/]")
        return
    t = Table(show_header=True, header_style="bold cyan")
    t.add_column("ID", justify="right")
    t.add_column("Название")
    t.add_column("Год", justify="center")
    t.add_column("Жанры")
    for r in rows:
        t.add_row(str(r["film_id"]), r["title"],
                  str(r["release_year"]), r.get("genres", "-"))
    console.print(t)

def print_stats(rows, title):
    t = Table(title=title)
    t.add_column("Запрос")
    t.add_column("Cnt", justify="right")
    for r in rows:
        t.add_row(str(r["_id"]), str(r["cnt"]))
    console.print(t)