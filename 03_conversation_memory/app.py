import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

commands = {
    "help": """
Available commands:
- help : Show this menu
- exit : Close the chatbot
"""
}

client = genai.Client(api_key=api_key)

def ask_ai(history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    return response.text


def start_chatbot():
    history = []
    if not api_key:
        print("Gemini API key not found.")
        return

    print("===== Gemini Chatbot =====")
    print("Type 'help' for commands.")

    while True:
        prompt = input("\nChat: ").strip()

        if not prompt:
            print("Prompt cannot be empty.")
            continue

        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        if prompt.lower() == "help":
            print(commands["help"])
            continue

        history.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })
        answer = ask_ai(history)
        history.append({
            "role": "model",
            "parts": [{"text": answer}]
        })

        print("\nAI:")
        print(answer)


start_chatbot()