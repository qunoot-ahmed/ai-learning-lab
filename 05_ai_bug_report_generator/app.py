from pathlib import Path
from common.gemini_client import ask_ai

OUTPUT_FILE = Path(__file__).parent / "generated_bug_report.md"

def save_output(response):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(response)

    print(f"\nBug report saved to {OUTPUT_FILE}")

def build_prompt(bug_description):
    prompt = f"""
You are a Senior QA Engineer responsible for writing high-quality Jira bug reports.

## Task

Transform the following rough bug description into a professional bug report.

## Bug Description

{bug_description}

## Constraints

- Do not invent browser, operating system, environment, application version, user account, or any information not explicitly provided.
- If information is missing, write "Not Provided".
- Keep the report concise, professional, and Jira-ready.
- Use clear QA terminology.
- Infer severity and priority only when sufficient information is available.
- If severity or priority cannot be determined confidently, state that additional information is required.
- Do not include unnecessary explanations outside the bug report.

## Output Format

Return the bug report using exactly these sections:

# Title

# Summary

# Environment

# Preconditions

# Steps to Reproduce

# Actual Result

# Expected Result

# Severity

# Priority

# Possible Root Cause

# Business Impact
"""
    return prompt

def main():
    bug_description = input("Enter bug description: ").strip()

    if not bug_description:
        print("Bug description cannot be empty.")

    prompt = build_prompt(bug_description)
    response = ask_ai(prompt)

    print("\n===== Generated Bug Report =====\n")
    print(response)

    save_output(response)


if __name__ == "__main__":
    main()