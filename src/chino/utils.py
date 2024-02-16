from rich.console import Console


def fancy_print(console: Console, text: str, isQuery: bool = False) -> None:
    if isQuery:
        console.print(f"[b blue]Chino:[/b blue] {text}")
        console.rule()
    else:
        console.print(f"[b blue]Chino:[/b blue] {text}")
        console.rule()
