
# from retrieval.query_rewriter import rewrite_query
import time
from retrieval.retriever import Retriever
from retrieval.prompt_builder import build_prompt
# from llm.ollama_client import generate_response
from llm.ollama_client import stream_response
class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()

    # def run(self, query, chat_history=None):

        # # Step 0: Reformulate query
        # # rewritten_query = rewrite_query(query, chat_history, generate_response)
        # rewritten_query = query
        # # Step 1: Retrieve using rewritten query
        # start = time.time()
        # retrieved_chunks = self.retriever.retrieve(rewritten_query)
        # print("Retrieval time: ", time.time() - start)

        # # Step 2: Build prompt (use original query!)
        # start = time.time()
        # prompt = build_prompt(query, retrieved_chunks, chat_history)
        # print("Prompt Build time: ", time.time() - start)

        # # Step 3: Generate answer
        # print("\nAssistant: ", end="")
        # start = time.time()
        # answer = generate_response(prompt)
        # print("Generate text time: ", time.time() - start)

        # return {
        #     "answer": answer,
        #     "sources": retrieved_chunks,
        #     "rewritten_query": rewritten_query
        # }
    def run(self, query, chat_history=None):

        retrieved_chunks = self.retriever.retrieve(query)

        prompt = build_prompt(query, retrieved_chunks, chat_history)

        # 🔥 return generator instead of final text
        stream = stream_response(prompt)

        return {
            "stream": stream,
            "sources": retrieved_chunks
        }


# For Streamlit UI
# from llm.ollama_client import stream_response
# class RAGPipeline:
#     def run(self, query, chat_history=None):

#         retrieved_chunks = self.retriever.retrieve(query)

#         prompt = build_prompt(query, retrieved_chunks, chat_history)

#         # 🔥 return generator instead of final text
#         stream = stream_response(prompt)

#         return {
#             "stream": stream,
#             "sources": retrieved_chunks
        # }