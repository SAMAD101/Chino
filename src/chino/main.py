# !/usr/bin/python

import typer
import sys

from openai import OpenAI

client = OpenAI()
messages = [
    {
        "role": "system",
        "content": "You are Chino, a chatbot powered by OpenAI's GPT-3.5. 'Chino' means 'curious' in Japanese."
    },
]


def run_conversation(prompt):
    global client, messages

    while True:
        prompt = input("You: ")
        if prompt == "quit":
            break
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        messages.append({"role": "system", "content": response.choices[0].message.content})
        print(f"Chino: {response.choices[0].message.content}")


def main(
        prompt: str = typer.Option(None, '-p', '--prompt', help="Prompt for ChatGPT"),
        quit: bool = typer.Option(False, '-q', '--quit', help="Quit the running conversation"),
):
    run_conversation(prompt)


if __name__ == "__main__":
    typer.run(main)
