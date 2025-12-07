import ollama

def summarize_text(text):
    response = ollama.chat(
        model="llama3.1",
        messages=[
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
    )
    return response['message']['content']

if __name__ == "__main__":
    notes = input("Paste your notes:\n")
    summary = summarize_text(notes)
    print("\n--- Summary ---\n")
    print(summary)
