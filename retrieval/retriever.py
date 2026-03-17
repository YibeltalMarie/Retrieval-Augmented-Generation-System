from chromadb import Client
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceEmbeddings


class Retriever:
    def __init__(self, persist_directory="vector_store", collection_name="rag_documents", top_k=3):
        """
        Initialize retriever.
        :param persist_directory: Path to Chroma DB
        :param collection_name: Name of the collection
        :param top_k: Number of top chunks to return
        """
        self.client = Client(Settings(persist_directory=persist_directory))
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
