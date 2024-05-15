import os
import typer

from typer import Typer, Context, Option

from .conversation import Conversation
from .migrations import Migration

from .utils import fancy_print

from chino import __version__


app: Typer = Typer(
    help="Chino is a chatbot based on OpenAI. It can also provide responses about queries on user-provided data.",
)


@app.command()
def migrate(
    chroma_path: str = os.path.expanduser("~/.local/share/chino/chroma/"),
    data_path: str = os.path.expanduser("~/.local/share/chino/data/"),
) -> None:
    """Migrate the data to the chroma using vector embeddings."""

    migration = Migration(chroma_path, data_path)
    migration.generate_data_store()


@app.command()
def start() -> None:
    """Start the main event loop function. A chat interface will be opened."""
    conv: Conversation = Conversation()
    try:
        while True:
            prompt = conv.console.input("[bold green]You: [/bold green]")
            if prompt == "quit":
                conv.console.print("[bold red]Quiting...[/bold red]")
                break
            elif prompt.lower().startswith("\\q:"):
                quried_res = conv.run_query(prompt)
                fancy_print(conv.console, quried_res[0], isQuery=True)
                conv.console.print(f"[bold blue]Sources:[/bold blue] {quried_res[1]}")
                conv.console.rule()
                continue
            fancy_print(conv.console, conv.get_response(prompt).content)
    except KeyboardInterrupt:
        conv.console.print("\n[bold red]Quiting...[/bold red]")


@app.command()
def version() -> None:
    """Print the version of the chino package."""
    typer.echo(f"Chino {__version__}")
