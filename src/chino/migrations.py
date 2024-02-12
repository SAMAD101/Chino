import os
import shutil

from typing import Any, List

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma


class Migration:
    def __init__(self, chroma_path: str = None, data_path: str = None) -> None:
        self.CHROMA_PATH: str = chroma_path
        self.DATA_PATH: str = data_path

    def generate_data_store(self) -> None:
        documents: Any = Migration._load_documents(self.DATA_PATH)
        chunks: List[Document] = Migration._split_text(documents)
        Migration._save_to_chroma(chunks, self.CHROMA_PATH)

    @classmethod
    def _load_documents(cls, data_path):
        loader: DirectoryLoader = DirectoryLoader(data_path)
        documents: Any = loader.load()
        return documents

    @classmethod
    def _split_text(cls, documents: List[Document]) -> List[Document]:
        text_splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
        chunks: List[Document] = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        return chunks

    @classmethod
    def _save_to_chroma(cls, chunks: List[Document], chroma_path: str):
        # Clear out the database first.
        if os.path.exists(chroma_path):
            shutil.rmtree(chroma_path)

        # Create a new DB from the documents.
        db: Chroma = Chroma.from_documents(
            chunks, OpenAIEmbeddings(), persist_directory=chroma_path
        )
        db.persist()
        print(f"Saved {len(chunks)} chunks to {chroma_path}.")
