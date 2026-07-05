import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
from pathlib import Path

OUTPUT_FILE = Path("generated_test_cases.md")

def save_output(response):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(response)

    print(f"Test cases saved to {OUTPUT_FILE}")


api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def build_prompt(requirement):
    prompt = f"""
You are a Senior QA Engineer with expertise in web application testing.

Your task is to generate comprehensive test cases for the given software requirement.

Requirement:
{requirement}

Generate test cases covering:
- Functional
- Smoke
- Regression
- Negative
- Edge Cases
- Security
- Validation

For each test case include:
- Test Case ID
- Title
- Preconditions
- Test Steps
- Expected Result
- Priority

Constraints:
- Generate as many test cases as necessary to thoroughly cover the requirement.
- Avoid duplicate or low-value test cases.
- Generate only the categories relevant to the given requirement.
- Do not assume features that are not mentioned in the requirement.
- If an assumption is required, clearly label it as an assumption.
- Use generic placeholders instead of invented usernames, passwords, or emails.
- Assign priorities based on business impact and risk.
- Keep each test case clear and executable.

Return a Markdown table with exactly these columns:
- Test Case ID
- Category
- Title
- Preconditions
- Test Steps
- Expected Result
- Priority
"""
    return prompt


def main():
    requirement = input("Enter requirement: ").strip()

    if not requirement:
        print("Requirement cannot be empty.")
        return

    prompt = build_prompt(requirement)
    response = ask_ai(prompt)

    print("\n===== Generated Test Cases =====\n")
    print(response)

    save_output(response)

main()