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


def ask_ai(prompt):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def start_chatbot():
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

        answer = ask_ai(prompt)

        print("\nAI:")
        print(answer)


start_chatbot()