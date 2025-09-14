import typer
from rich.console import Console
from rich.table import Table
from noteforces.services.notes_service import add_note, search_note

app = typer.Typer()
console = Console()

@app.command()
def add(
    tag: str = typer.Option(..., help="Problem tag"),
    rating: int = typer.Option(..., help="Problem rating"),
    ideas: str = typer.Option(..., help="Your ideas or notes"),
    time_spent: int = typer.Option(..., help="Time spent on problem (minutes)"),
    # editorial: bool = typer.Option(False, help="Whether editorial was needed")
):
    """Add a new note"""
    add_note(tag, rating, ideas, time_spent)
    console.print(f"[green]✅ Note added with tag:[/green] {tag}")


@app.command()
def search(by_tag: str = typer.Option(None), by_rating: int = typer.Option(None)):
    """Search notes by tag or minimum rating."""
    results = search_note(by_tag, by_rating)
    if not results:
        typer.echo("No notes found.")
        return

    table = Table(title="Codeforces Notes")
    table.add_column("ID", style="cyan")
    table.add_column("Tags", style="magenta")
    table.add_column("Rating", style="green")
    table.add_column("Ideas", style="yellow")
    table.add_column("Time Spent", style="blue")
    # table.add_column("Editorial", style="red")
    table.add_column("Created At", style="white")

    for r in results:
        table.add_row(
            str(r["id"]),
            r["tags"],
            str(r["rating"]),
            r["ideas"],
            str(r["time_spent"]),
            r["created_at"]
        )

    console.print(table)
