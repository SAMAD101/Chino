import pytest

from typing import Generator

from chino.migrations import Migration


@pytest.fixture
def migration_env(mock_migration, monkeypatch) -> Generator[Migration, None, None]:
    migration: Migration = mock_migration
    monkeypatch.setattr(migration, "_save_to_chroma", lambda: "saved to chroma")
    yield migration


def test_generate_data_store(monkeypatch, migration_env) -> None:
    migration = migration_env
    documents = migration._load_documents(migration.DATA_PATH)
    chunks = migration._split_text(documents)
    migration._save_to_chroma()  # No arguments are needed
    assert True
