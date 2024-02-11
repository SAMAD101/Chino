# !/usr/bin/python

import typer

from typing import List, Union

from rich.console import Console

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage, BaseMessage
from langchain_openai import ChatOpenAI

from utils.query_data import query_data

app = typer.Typer()
console = Console()

model: ChatOpenAI = ChatOpenAI()

messages: List[Union[SystemMessage, HumanMessage]] = [
    SystemMessage(
        content="You are Chino, a chatbot based on ChatGPT. 'Chino' means 'intelligence' in Japanese."
    ),
]


def get_response(prompt: str) -> None:
    global model, messages

    with console.status("[i]thinking...[/i]"):
        messages.append(HumanMessage(content=prompt))
        response: BaseMessage = model.invoke(messages)
        messages.append(SystemMessage(content=response.content))
        console.print(f"[b blue]Chino:[/b blue] {response.content}")
        console.rule()


def run_query(prompt: str) -> None:
    global model, messages

    with console.status("[i]thinking...[/i]"):
        query_text, query_sources = query_data(prompt)
        messages.append(HumanMessage(content=query_text))
        response: BaseMessage = model.invoke(messages)
        messages.append(SystemMessage(content=response.content))
        console.print(f"[b blue]Chino:[/b blue] {response.content}\n\n[i violet]Sources:[/i violet]{query_sources}")
        console.rule()


def run_conversation(prompt: str, query: bool) -> None:
    global model, messages

    if prompt:
        if query or prompt.lower().startswith("\\q:"):
            run_query(prompt)
            return
        get_response(prompt)
        return

    while True:
        prompt: str = console.input("[b green]You: [/b green]")
        if prompt == "quit":
            break
        elif query or prompt.lower().startswith("\\query:"):
            run_query(prompt)
            continue
        get_response(prompt)


def main(
        prompt: str = typer.Option(None, '-p', '--prompt', help="Prompt for ChatGPT"),
        query: bool = typer.Option(False, '-q', '--query', help="Query for your data")
) -> None:
    run_conversation(prompt, query)


if __name__ == "__main__":
    typer.run(main)
