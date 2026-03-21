
# import ollama

# def generate_response(prompt, model="phi"):
#     """
#     Send prompt to Ollama and get response.
#     """

#     response = ollama.chat(
#         model=model,
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         options={
#         "num_predict": 100,   # LIMIT output
#         "temperature": 0.2
#     }
#     )

#     return response['message']['content']



# For interactive Terminal Chat

# import ollama

# def generate_response(prompt, model="phi"):
#     """
#     Generate response from Ollama with streaming.
#     Prints tokens as they are generated (real-time).
#     """

#     stream = ollama.chat(
#         model=model,
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         stream=True,
#         options={
#             "num_predict": 150,   # limit output length (important for speed)
#             "temperature": 0.3
#         }
#     )

#     full_response = ""

#     for chunk in stream:
#         token = chunk['message']['content']
#         print(token, end="", flush=True)   # 🔥 real-time output
#         full_response += token

#     print()  # newline after completion

#     return full_response



# For Streamlit UI
import ollama

def stream_response(prompt, model="phi"):
    """
    Stream response token-by-token (generator)
    """

    stream = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=True,
        options={
            "num_predict": 150,
            "temperature": 0.3
        }
    )

    for chunk in stream:
        yield chunk['message']['content']