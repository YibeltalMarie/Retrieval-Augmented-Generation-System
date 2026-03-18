
from chat.history_manager import HistoryManager
from retrieval.rag_pipeline import RAGPipeline


def start_chat():
    print("🔹 RAG Chatbot Started (type 'exit' to quit, 'clear' to reset history)\n")

    history_manager = HistoryManager()
    rag = RAGPipeline()

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Clear history
        if user_input.lower() == "clear":
            history_manager.clear_history()
            print("🧹 Chat history cleared.\n")
            continue

        # Get history
        chat_history = history_manager.get_history()

        # Run RAG pipeline
        response = rag.run(user_input, chat_history)

        answer = response["answer"]
        sources = response.get("sources", [])
        rewritten_query = response.get("rewritten_query", None)

        # Show reformulated query (for debugging / learning)
        if rewritten_query:
            print(f"🔁 Rewritten Query: {rewritten_query}\n")

        # Print answer[main ca203d0] build history manager to track chat history
 1 file changed, 33 insertions(+)

RAG-System main ❯ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 697 bytes | 348.00 KiB/s, done.
        print(f"\nAssistant: {answer}\n")


        # Show sources
        if sources:
            print("📚 Sources:")
            for src in sources:
                print(f"- {src['metadata'].get('source', 'Unknown')}")
            print()

        # Update history
        history_manager.add_turn(user_input, answer)