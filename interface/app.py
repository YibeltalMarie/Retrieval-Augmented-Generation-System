# interface/app.py
import sys
import os
# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from retrieval.rag_pipeline import RAGPipeline
from chat.history_manager import HistoryManager

# ----------------------------
# Initialize RAG and History
# ----------------------------
if "rag" not in st.session_state:
    st.session_state.rag = RAGPipeline()

if "history_manager" not in st.session_state:
    st.session_state.history_manager = HistoryManager()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Title and Layout
# ----------------------------
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🧠 RAG Chatbot")
st.write("Ask questions about your documents. Responses stream in real-time!")

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.session_state.history_manager.clear_history()
    st.experimental_rerun()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# User Input
# ----------------------------
user_input = st.chat_input("Type your question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get chat history
    chat_history = st.session_state.history_manager.get_history()

    # Run RAG pipeline
    with st.spinner("Thinking..."):
        response = st.session_state.rag.run(user_input, chat_history)
        stream = response["stream"]
        sources = response.get("sources", [])
        rewritten_query = response.get("rewritten_query", None)

    # ----------------------------
    # Stream Assistant Response
    # ----------------------------
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Stream tokens
        for token in stream:
            full_response += token
            message_placeholder.markdown(full_response + "▌")  # typing effect

        message_placeholder.markdown(full_response)  # final clean text

        # Show rewritten query if exists
        if rewritten_query:
            st.markdown(f"🔁 **Rewritten Query:** {rewritten_query}")

        # Show sources
        if sources:
            st.markdown("📚 **Sources:**")
            for src in sources:
                st.markdown(f"- {src['metadata'].get('source', 'Unknown')}")

    # Save assistant response to session and history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.history_manager.add_turn(user_input, full_response)
