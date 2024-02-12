import os

from typer import Typer

from .query import Query
from .conversation import Conversation
from .migrations import Migration


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
def main():
    """Start the main event loop function. A chat interface will be opened."""

    conversation: Conversation = Conversation()
    try:
        while True:
            prompt = conversation.console.input("[bold green]You: [/bold green]")
            if prompt == "quit":
                conversation.console.print("[bold red]Quiting...[/bold red]")
                break
            elif prompt.lower().startswith("\\q:"):
                conversation.run_query(prompt)
                continue
            conversation.get_response(prompt)
    except KeyboardInterrupt:
        conversation.console.print("\n[bold red]Quiting...[/bold red]")
