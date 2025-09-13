import typer
from noteforces import services

app = typer.Typer()

@app.command()
def add():
    """Add a new Codeforces problem note."""
    tag = typer.prompt("Tag")
    rating = typer.prompt("Rating")
    ideas = typer.prompt("Main ideas")
    time_spent = typer.prompt("Time spent (minutes)")
    editorial = typer.prompt("Editorial needed?")

    services.add_note(tag, rating, ideas, time_spent, editorial)
    typer.echo("Note added Successfully")

@app.command()
def search(by: str = typer.Option("all", help = "Search filter: all, tag, date")):
    """Search for stored notes"""
    results = services.search_notes(by)
    if (results):
        for r in results:
            typer.echo(r)
        else:
            typer.echo("No results found.")

