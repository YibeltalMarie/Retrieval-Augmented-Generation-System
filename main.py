from ingestion.loader import load_documents
from ingestion.chunking import chunk_documents
from ingestion.embedding import embed_documents
from ingestion.vector_store import store_embeddings


documents = load_documents()
chunks = chunk_documents(documents)
embeddings = embed_documents(chunks)
stored_embeddings = store_embeddings(embeddings)



