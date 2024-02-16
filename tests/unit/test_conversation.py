import pytest
from chino.conversation import Conversation


def test_get_response():
    conversation = Conversation()
    conversation.get_response("Hello")
    assert conversation.messages[-1].content == "Hello"
