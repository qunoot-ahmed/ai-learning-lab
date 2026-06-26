import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def ask_ai(prompt):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if not api_key:
    print("Gemini API key not found.")
else:
    prompt = input("Ask AI something: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
    else:
        answer = ask_ai(prompt)

        print("\n===== AI Response =====")
        print(answer)