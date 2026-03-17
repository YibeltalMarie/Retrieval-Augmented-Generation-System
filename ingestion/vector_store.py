from chromadb import Client
from chromadb.config import Settings


def store_embeddings(chunks, persist_directory="vector_store"):
    """
    Store chunk embeddings in Chroma vector database.
    """

    client = Client(Settings(persist_directory=persist_directory))

    collection = client.get_or_create_collection(name="rag_documents")

    for i, doc in enumerate(chunks):

        collection.add(
            ids=[f"chunk_{i}"],
            documents=[doc.page_content],
            embeddings=[doc.metadata["embedding"]],
            metadatas=[doc.metadata]
        )

    client.persist()

    return collection
