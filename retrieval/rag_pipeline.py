
from retrieval.retriever import Retriever
from retrieval.prompt_builder import build_prompt
from llm.ollama_client import generate_response


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def run(self, query, chat_history=None):
        """
        Full RAG pipeline:
        1. Retrieve relevant chunks
        2. Build prompt
        3. Generate response from LLM
        """

        # Step 1: Retrieve relevant chunks
        retrieved_chunks = self.retriever.retrieve(query)

        # Step 2: Build prompt
        prompt = build_prompt(query, retrieved_chunks, chat_history)

        # Step 3: Generate response using LLM
        answer = generate_response(prompt)

        return {
            "answer": answer,
            "sources": retrieved_chunks
        }