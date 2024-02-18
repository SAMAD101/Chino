import pytest

from chino.query import Query


@pytest.fixture
def mock_query(mock_query, monkeypatch) -> Query:
    query = mock_query
    monkeypatch.setattr(query, "_prepare_db", lambda: "db")
    return query


def test_query_data(mock_query) -> None:
    query_text, query_sources = mock_query.query_data()
    assert query_text == "query_text"
    assert query_sources == ["sources"]
