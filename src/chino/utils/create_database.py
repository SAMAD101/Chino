import os
import shutil

from typing import Any, List

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma


CHROMA_PATH: str = "chroma"
DATA_PATH: str = "data"


def main() -> None:
    generate_data_store()


def generate_data_store() -> None:
    documents: Any = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    loader: DirectoryLoader = DirectoryLoader(DATA_PATH)
    documents: Any = loader.load()
    return documents


def split_text(documents: List[Document]) -> List[Document]:
    text_splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks: List[Document] = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    return chunks


def save_to_chroma(chunks: List[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db: Chroma = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
