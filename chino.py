# !/usr/bin/python

import typer

from openai import OpenAI


client = OpenAI()


def run_conversation(prompt) -> str:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are Chino. Chino means 'wisdom' in Japanese."},
        {"role": "user", "content": prompt}
      ]
    )
    return response.choices[0].message.content


def main(prompt: str = typer.Option(None, '-p', '--prompt', help="Prompt for ChatGPT")):
    if prompt is not None:
        response = run_conversation(prompt)
        typer.echo(response)
    else:
        typer.echo("Chino is Happy!")


if __name__ == "__main__":
    typer.run(main)
