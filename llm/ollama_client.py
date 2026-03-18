
import ollama

def generate_response(prompt, model="phi"):
    """
    Send prompt to Ollama and get response.
    """

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']