import sys

from typing import List, Tuple

from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Details

{context}

---

Answer this question based on the above details and previous messages: {question}
"""


def prepare_db() -> Chroma:
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())


def query_data(query_text: str) -> Tuple[str, List[str]]:
    # query text will be the prompt - provided by the user - to be processed using the embeddings and the model

    db: Chroma = prepare_db()

    # Search the DB.
    results: List = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        sys.exit()

    context_text: str = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    query_prompt = "QUERY:"+prompt_template.format(context=context_text, question=query_text)
    # This prompt will serve as a context for the model to generate a response.

    query_sources = [doc.metadata.get("source", None) for doc, _score in results]
    return query_prompt, query_sources
