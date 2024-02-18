import pytest

from typing import Generator, Tuple, List

from chino.conversation import Conversation
from chino.migrations import Migration
from chino.query import Query


@pytest.fixture
def mock_conv() -> Conversation:
    class MockConversation(Conversation):
        def __init__(self) -> None:
            super().__init__()
            self.model = None
            self.messages = []

    return MockConversation()


@pytest.fixture(scope="session")
def mock_migration(tmpdir_factory) -> Generator[Migration, None, None]:
    CHROMA_PATH = tmpdir_factory.mktemp("chroma")
    DATA_PATH = tmpdir_factory.mktemp("data")

    class MockMigration(Migration):
        def __init__(self) -> None:
            super().__init__(str(CHROMA_PATH), str(DATA_PATH))

    yield MockMigration()


@pytest.fixture
def mock_query(mock_migration) -> Query:
    class MockQuery(Query):
        def __init__(self) -> None:
            super().__init__(chroma_path=mock_migration.CHROMA_PATH)

        def query_data(self) -> Tuple[str, List[str]]:
            return "query_text", ["sources"]

    return MockQuery()
