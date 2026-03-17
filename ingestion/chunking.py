
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings


def chunk_documents(documents):
    """
    Perform semantic chunking on documents.
    Splits text based on semantic similarity instead of characters.
    """

    print("Starting Loading Embedding model.... in chunking.py")
    # Embedding model used for detecting semantic boundaries
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Finished Loading Embedding model.... in chunking.py")
    # This loads the MiniLM embedding model.

    # Characteristics:

    #     Feature  Value
    #     Dimension  384
    #     Speed  Fast
    #     Size  Small
    #     Use  Sentence similarity

    # Create semantic chunker
    chunker = SemanticChunker(embeddings)
    # This chunker now has the embedding model inside it.
    # It will use it to determine:
    # Are two sentences related?

    print("Start splitting text into sentences.... in chunking.py")
    # Split documents
    chunks = chunker.split_documents(documents)

    print("Finish chunking.............")
    # Step 1 — Extract Text
    # The chunker extracts text from each document.

    # Step 2 — Split Into Sentences
    # The text is split into sentences.

    # Step 3 — Create Embeddings for Each Sentence
    # Each sentence is passed to the embedding model.

    # Step 4 — Compare Sentence Similarity
    # The algorithm compares adjacent sentences.

    # Step 5 — Detect Chunk Boundaries
    # When similarity drops below a threshold: New chunk
        # 1️⃣ How SemanticChunker Detects Chunk Boundaries

        # Internally, the chunker does this:
        # Converts each sentence to an embedding vector.
        # Computes similarity between consecutive sentences (usually cosine similarity).
        # Compares the similarity to a threshold:
        #     Above threshold → sentences stay in the same chunk.
        #     Below threshold → sentence starts a new chunk.

        # 2️⃣ Default Threshold

        # LangChain’s SemanticChunker uses a default similarity threshold internally.
        # Default behavior:
        #     It usually sets a threshold around 0.7 cosine similarity, meaning sentences with similarity ≥ 0.7 are grouped together.
        #     The exact number may vary depending on the implementation and version.
        #     It also has a percentile-based option, where it chooses boundaries dynamically based on the distribution of similarities in the document.
        # Parameter Explanation
        #     Parameter  Purpose
        #     breakpoint_threshold :  Value between 0 and 1. Cosine similarity below this triggers a new chunk.
        #     breakpoint_threshold_type:   "absolute" → use exact number (e.g., 0.75), "percentile" → choose threshold from data distribution.
        #     chunk_size (optional):   Maximum number of sentences per chunk (used to avoid huge chunks)
        #     chunk_overlap (optional):   Number of sentences that overlap between consecutive chunks
    # Step 6 — Create New Document Objects
    # Each chunk becomes a new Document.

    # Step 7 — Return Chunk List
    # Finally the function returns:

    # for i, chunk in enumerate(chunks[:2]):
    #     print(f"\nChunk {i+1}: ")
    #     print(f"Source: {chunk.metadata['source']}")
    #     print(f"Content Length: {len(chunk.page_content)} characters")
    #     print(f"Content Preview: {chunk.page_content}")
    #     print(f"Metadata: {chunk.metadata}")

    return chunks

# documents = load_documents()
# chunk_documents(documents)
