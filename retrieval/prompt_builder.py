
def build_prompt(query, retrieved_chunks, chat_history=None):
    """
    Build a structured prompt for the LLM using:
    - user query
    - retrieved context
    - optional chat history
    """

    # 1. Format retrieved context
    context_text = ""
    for i, chunk in enumerate(retrieved_chunks):
        context_text += f"[{i+1}] {chunk['document']}\n"

    # 2. Format chat history (if exists)
    history_text = ""
    if chat_history:
        for turn in chat_history:
            history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

    # 3. Build final prompt
    prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer the question.
If the answer is not in the context, say: "I don't know based on the provided information."

---------------------
Context:
{context_text}
---------------------

"""

    # Add history if available
    if history_text:
        prompt += f"""
Conversation History:
{history_text}
---------------------
"""

    prompt += f"""
Question:
{query}

Answer:
"""

    return prompt