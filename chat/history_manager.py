
class HistoryManager:
    def __init__(self, max_history=5):
        """
        Initialize history manager.
        :param max_history: number of recent conversations to keep
        """
        self.history = []
        self.max_history = max_history

    def add_turn(self, user_input, assistant_response):
        """
        Add a new conversation turn.
        """
        self.history.append({
            "user": user_input,
            "assistant": assistant_response
        })

        # Keep only the latest N conversations
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_history(self):
        """
        Return current chat history.
        """
        return self.history

    def clear_history(self):
        """
        Reset conversation history.
        """
        self.history = []