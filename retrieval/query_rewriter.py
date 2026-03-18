
def rewrite_query(query, chat_history, llm_generate):
    """
    Reformulate the query into a standalone question using chat history.
    """

    if not chat_history:
        return query  # no need to rewrite

    history_text = ""
    for turn in chat_history:
        history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

    prompt = f"""
You are an AI assistant that reformulates user questions.

Given the conversation history and the latest user query,
rewrite the query into a clear, standalone question.

Conversation History:
{history_text}

User Query:
{query}

Rewritten Query:
"""

    rewritten_query = llm_generate(prompt)

    return rewritten_query.strip()
