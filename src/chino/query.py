import sys

from typing import Optional, Tuple, List

from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate


class Query:
    def __init__(
        self, prompt: Optional[str] = None, chroma_path: Optional[str] = None
    ) -> None:
        self.query_text = prompt
        self.CHROMA_PATH = chroma_path

    def _prepare_db(self) -> Chroma:
        return Chroma(
            persist_directory=self.CHROMA_PATH, embedding_function=OpenAIEmbeddings()
        )

    def query_data(self) -> Tuple[str, List[str]]:
        # query text will be the prompt - provided by the user - to be processed using the embeddings and the model
        PROMPT_TEMPLATE: str = """
        Details
        {context}
        ---
        Answer this question based on the above details and previous messages: {question}
        """
        db: Chroma = self._prepare_db()

        # Search the DB.
        results: List = db.similarity_search_with_relevance_scores(self.query_text, k=3)
        if len(results) == 0 or results[0][1] < 0.7:
            print(f"Unable to find matching results.")
            sys.exit()

        context_text: str = "\n\n---\n\n".join(
            [doc.page_content for doc, _score in results]
        )
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        query_prompt = "QUERY:" + prompt_template.format(
            context=context_text, question=self.query_text
        )
        # This prompt will serve as a context for the model to generate a response.

        query_sources = [doc.metadata.get("source", None) for doc, _score in results]
        return query_prompt, query_sources
