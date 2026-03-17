import os
from chromadb import Client
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "data/vector_db")

class Retriever:
    def __init__(self, persist_directory=DOCS_PATH, collection_name="rag_documents", top_k=3):
        """
        Initialize retriever.
        :param persist_directory: Path to Chroma DB
        :param collection_name: Name of the collection
        :param top_k: Number of top chunks to return
        """
        self.client = Client(Settings(
            persist_directory=persist_directory,
            is_persistent=True
            ))
        self.collection = self.client.get_collection(collection_name)
        self.top_k = top_k

        # Use the same embedding model as during ingestion
        self.embedder = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def retrieve(self, query):
        """
        Retrieve top-k relevant chunks for a given query.
        :param query: User query string
        :return: List of dicts with 'document' and 'metadata'
        """
        query_embedding = self.embedder.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=self.top_k
        )

        # Extract relevant info
        retrieved_chunks = []
        for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
            retrieved_chunks.append({
                "document": doc,
                "metadata": metadata
            })

        return retrieved_chunks
