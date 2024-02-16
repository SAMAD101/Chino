import os

from typer import Typer

from .conversation import Conversation
from .migrations import Migration

from .utils import fancy_print

app: Typer = Typer(
    help="Chino is a chatbot based on OpenAI. It can also provide responses about queries on user-provided data."
)


@app.command()
def migrate(
    chroma_path: str = os.path.expanduser("~/.local/share/chino/chroma/"),
    data_path: str = os.path.expanduser("~/.local/share/chino/data/"),
) -> None:
    """Migrate the data to the chroma using vector embeddings."""

    migration = Migration(chroma_path, data_path)
    migration.generate_data_store()


@app.command("start")
def main() -> None:
    """Start the main event loop function. A chat interface will be opened."""

    conv: Conversation = Conversation()
    try:
        while True:
            prompt = conv.console.input("[bold green]You: [/bold green]")
            if prompt == "quit":
                conv.console.print("[bold red]Quiting...[/bold red]")
                break
            elif prompt.lower().startswith("\\q:"):
                fancy_print(conv.console, conv.run_query(prompt).content, isQuery=True)
                continue
            fancy_print(conv.console, conv.get_response(prompt).content)
    except KeyboardInterrupt:
        conv.console.print("\n[bold red]Quiting...[/bold red]")
