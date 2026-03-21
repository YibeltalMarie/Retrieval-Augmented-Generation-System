
# def build_prompt(query, retrieved_chunks, chat_history=None):
#     """
#     Build a structured prompt for the LLM using:
#     - user query
#     - retrieved context
#     - optional chat history
#     """

#     # 1. Format retrieved context
#     context_text = ""
#     for i, chunk in enumerate(retrieved_chunks):
#         context_text += f"[{i+1}] {chunk['document']}\n"

#     # 2. Format chat history (if exists)
#     history_text = ""
#     if chat_history:
#         for turn in chat_history:
#             history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

#     # 3. Build final prompt
#     prompt = f"""Answer the question using ONLY the context.
# If not found, say: "I don't know."

# Context:
# {context_text}
# """

#     # Add history if available
#     if history_text:
#         prompt += f"""
# Conversation History:
# {history_text}
# """

#     prompt += f"""
# Question:
# {query}

# Answer:
# """

#     return prompt


def build_prompt(query, retrieved_chunks, chat_history=None):
    MAX_CHARS = 300
    MAX_TURNS = 2

    # Context
    context_text = ""
    for i, chunk in enumerate(retrieved_chunks):
        text = chunk['document'][:MAX_CHARS]
        context_text += f"[{i+1}] {text}\n"

    # History (limited)
    history_text = ""
    if chat_history:
        for turn in chat_history[-MAX_TURNS:]:
            history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

    # Prompt
    prompt = f"""Answer using ONLY based on the provided documents and  the context below.
If not found, say "I don't know. Don't add anything yours if you don't know.

Context:
{context_text}
"""

    if history_text:
        prompt += f"\nHistory:\n{history_text}"

    prompt += f"\nQuestion: {query}\nAnswer:"

    return prompt