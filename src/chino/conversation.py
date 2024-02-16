import os

from typing import List, Union

from rich.console import Console

from langchain.schema import HumanMessage, SystemMessage, BaseMessage
from langchain_openai import ChatOpenAI

from .query import Query


class Conversation:
    def __init__(self) -> None:
        self.model = ChatOpenAI()
        self.messages: List[Union[SystemMessage, HumanMessage]] = [
            SystemMessage(
                content="You are Chino, a chatbot based on ChatGPT. 'Chino' means 'intelligence' in Japanese."
            ),
        ]
        self.console = Console()

    def get_response(self, prompt: str) -> BaseMessage:
        with self.console.status("[i]thinking...[/i]"):
            self.messages.append(HumanMessage(content=prompt))
            response: BaseMessage = self.model.invoke(self.messages)
            return response

    def run_query(self, prompt: str) -> BaseMessage:
        with self.console.status("[i]thinking...[/i]"):
            query_text, query_sources = Query(
                prompt, os.path.expanduser("~/.local/share/chino/chroma/")
            ).query_data()
            self.messages.append(HumanMessage(content=query_text))
            response: BaseMessage = self.model.invoke(self.messages)
            return response
