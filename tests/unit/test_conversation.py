import pytest

from typing import Generator

from chino.conversation import Conversation


@pytest.fixture
def conv_env(mock_conv, monkeypatch) -> Generator[Conversation, None, None]:
    """
    Handles common setup and teardown for unit tests involving the conversation.
    """
    conv: Conversation = mock_conv
    monkeypatch.setattr(conv, "get_response", lambda: "response")
    monkeypatch.setattr(conv, "run_query", lambda: "query response")
    yield conv


def test_get_response(monkeypatch, conv_env) -> None:
    response = conv_env.get_response()  # No prompt is needed
    assert response == "response"


def test_run_query(monkeypatch, conv_env) -> None:
    response = conv_env.run_query()  # No prompt is needed
    assert response == "query response"
