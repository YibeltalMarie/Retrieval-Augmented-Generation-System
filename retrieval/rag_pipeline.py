
# from retrieval.retriever import Retriever
# from retrieval.prompt_builder import build_prompt
# from llm.ollama_client import generate_response


# class RAGPipeline:
#     def __init__(self):
#         self.retriever = Retriever()

#     def run(self, query, chat_history=None):
#         """
#         Full RAG pipeline:
#         1. Retrieve relevant chunks
#         2. Build prompt
#         3. Generate response from LLM
#         """

#         # Step 1: Retrieve relevant chunks
#         retrieved_chunks = self.retriever.retrieve(query)

#         # Step 2: Build prompt
#         prompt = build_prompt(query, retrieved_chunks, chat_history)

#         # Step 3: Generate response using LLM
#         answer = generate_response(prompt)

#         return {
#             "answer": answer,
#             "sources": retrieved_chunks
#         }


from retrieval.query_rewriter import rewrite_query
from llm.ollama_client import generate_response

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def run(self, query, chat_history=None):

        # Step 0: Reformulate query
        rewritten_query = rewrite_query(query, chat_history, generate_response)

        # Step 1: Retrieve using rewritten query
        retrieved_chunks = self.retriever.retrieve(rewritten_query)

        # Step 2: Build prompt (use original query!)
        prompt = build_prompt(query, retrieved_chunks, chat_history)

        # Step 3: Generate answer
        answer = generate_response(prompt)

        return {
            "answer": answer,
            "sources": retrieved_chunks,
            "rewritten_query": rewritten_query
        }