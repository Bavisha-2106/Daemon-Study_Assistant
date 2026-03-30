def rewrite_query(client, user_input, conversation_history):
    history_text = "\n".join([f"{m['role']}: {m['content']}"
                              for m in conversation_history[-4:]])
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages = [{
            "role": "user",
            "content": f"""Given this conversation: {history_text}, and this new message: "{user_input}",
             Rewrite the message as a clear search query for an OS notes database.
              Reply with ONLY the search query and nothing else."""
        }]
    )
    return response.choices[0].message.content