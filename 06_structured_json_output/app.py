import json

from common.gemini_client import ask_ai


def build_prompt(bug_desc):
    prompt = f"""
You are a Senior QA Engineer.

Transform the following bug description into structured JSON.

Bug Description:
{bug_desc}

Constraints:
- Return only valid JSON.
- Do not return Markdown.
- Do not wrap the JSON in code fences.
- Do not include explanations or additional text.
- Do not invent missing information.
- If information is unavailable, use "Not Provided".
- The response must begin with {{ and end with }}.

Return exactly this JSON schema:

{{
    "title": "",
    "summary": "",
    "environment": "",
    "preconditions": "",
    "steps_to_reproduce": [],
    "actual_result": "",
    "expected_result": "",
    "severity": "",
    "priority": "",
    "possible_root_cause": "",
    "business_impact": ""
}}
"""
    return prompt


def main():
    bug_desc = input("Enter bug description: ").strip()

    if not bug_desc:
        print("Bug description cannot be empty.")
        return

    prompt = build_prompt(bug_desc)
    response = ask_ai(prompt)

    try:
        bug_report = json.loads(response)
        print(type(bug_report))
        print(bug_report)
    except json.JSONDecodeError:
        print("Gemini did not return valid JSON.")
        print("\nRaw response:")
        print(response)
        return

    print("\n===== Structured Bug Report =====")
    print(f"Title: {bug_report['title']}")
    print(f"Severity: {bug_report['severity']}")
    print(f"Priority: {bug_report['priority']}")
    print(f"Actual Result: {bug_report['actual_result']}")
    print(f"Expected Result: {bug_report['expected_result']}")


if __name__ == "__main__":
    main()