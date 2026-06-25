import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found.")
else:
    client = genai.Client(api_key=api_key)

    prompt = input("Ask AI something: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
    else:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\n===== AI Response =====")
        print(response.text)