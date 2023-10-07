#!/usr/bin/python
import typer

def get_gpt_response(prompt):
    pass
def main(prompt: str = typer.Option(None, '-p', '--prompt', help="Prompt for ChatGPT"),
         ):
    if prompt is not None:
        response = get_gpt_response(prompt)
        typer.echo(prompt)
        typer.echo(response)
    else:
        typer.echo("Chino is Happy!")

if __name__ == "__main__":
    typer.run(main)
