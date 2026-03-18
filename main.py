# from ingestion.loader import load_documents
# from ingestion.chunking import chunk_documents
# from ingestion.embedding import embed_documents
# from ingestion.vector_store import store_embeddings


# documents = load_documents()
# chunks = chunk_documents(documents)
# embeddings = embed_documents(chunks)
# stored_embeddings = store_embeddings(embeddings)

# from retrieval.retriever import Retriever

# query = "What are the two main components of the Transformer architecture?"
# retriever = Retriever()
# retrieved_chunks = retriever.retrieve(query)

# print(retrieved_chunks)

# from retrieval.rag_pipeline import RAGPipeline

# rag = RAGPipeline()

# response = rag.run("What is attention in transformers?")

# print(response["answer"])

# for src in response["sources"]:
#     print(src["metadata"]["source"])


from chat.chat_loop import start_chat

if __name__ == "__main__":
    start_chat()