
from langchain_community.embeddings import HuggingFaceEmbeddings

def embed_documents(chunks):
    """
    Generate embeddings for each chunk using HuggingFace Sentence Transformers.
    """

    print("Loadding Embedding model.... in embedding.py")
    # Initialize embedding model
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Finished loading Embedding model..... in embedding.py")

    print("Start Embedding for each chunk.... in embedding.py")
    # Create embeddings for each chunk
    for doc in chunks:
        doc.metadata["embedding"] = embedder.embed_query(doc.page_content)

    print("Finished embedding and return embeddings..... in embedding.py")
    return chunks
