
from langchain_community.embeddings import HuggingFaceEmbeddings

def embed_documents(chunks):
    """
    Generate embeddings for each chunk using HuggingFace Sentence Transformers.
    """

    # Initialize embedding model
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create embeddings for each chunk
    for doc in chunks:
        doc.metadata["embedding"] = embedder.embed_query(doc.page_content)

    return chunks
