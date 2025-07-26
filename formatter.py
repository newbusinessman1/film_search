from rich.table import Table
from rich.console import Console

console = Console()

def print_movies(rows):
    if not rows:
        console.print("[yellow]Nothing was found[/]")
        return
    t = Table(show_header=True, header_style="bold cyan")
    t.add_column("ID", justify="right")
    t.add_column("Name")
    t.add_column("Year", justify="center")
    t.add_column("Genre")
    for r in rows:
        t.add_row(
            str(r["film_id"]),
            r["title"],
            str(r["release_year"]),
            r.get("genres", "-")
        )
    console.print(t)

def print_stats(rows, title):
    t = Table(title=title)
    t.add_column("Request")
    t.add_column("Cnt/Time", justify="right")
    for r in rows:
        query = r["_id"]
        if isinstance(query, dict):
            # если это keyword-запрос → покажем только значение
            query = query.get("kw") or json.dumps(query, ensure_ascii=False)
        value = r.get("cnt") or r.get("ts") or "-"
        t.add_row(str(query), str(value))
    console.print(t)