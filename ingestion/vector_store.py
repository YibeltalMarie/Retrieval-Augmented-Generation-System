import os
import chromadb
from chromadb.config import Settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "data/vector_db")


def store_embeddings(chunks, persist_directory=DOCS_PATH):
    """
    Store chunk embeddings in Chroma vector database.
    """

    print("Connecting to chroma database..... in vector_store.py")

    client = chromadb.Client(
        Settings(
            persist_directory=persist_directory,
            is_persistent=True   # VERY IMPORTANT
        )
    )

    print("Creating 'rag_documents' collection in chroma db.....")
    collection = client.get_or_create_collection(name="rag_documents")

    print("Start adding embedded chunks into collection...")
    for i, doc in enumerate(chunks):
        collection.add(
            ids=[f"chunk_{i}"],
            documents=[doc.page_content],
            embeddings=[doc.metadata["embedding"]],
            metadatas=[doc.metadata]
        )

    print("Finished adding embedded chunks.")
    print("##### Now All embeddings are stored persistently in chroma db ########")

    # return collection