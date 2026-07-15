import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_issue(user_issue):

    issue = user_issue.lower()

    if "vpn" in issue:
        return "VPN"
    elif "wifi" in issue or "internet" in issue or "network" in issue:
        return "WiFi"
    elif "printer" in issue:
        return "Printer"
    elif "password" in issue or "login" in issue:
        return "Password"
    elif "outlook" in issue or "mail" in issue:
        return "Outlook"
    elif "software" in issue or "install" in issue:
        return "Software Installation"
    elif "blue screen" in issue:
        return "Blue Screen"
    elif "bluetooth" in issue:
        return "Bluetooth"
    elif "camera" in issue or "webcam" in issue:
        return "Camera"
    elif "microphone" in issue or "mic" in issue or "audio" in issue:
        return "Microphone"
    elif ("slow" in issue or "lag" in issue  or "hanging" in issue or "cpu" in issue or "performance" in issue):  
        return "Slow Computer"
    else:
        return "Unknown"

def generate_solution(category, issue_details):

    possible_causes = "\n".join(
        f"- {cause}" for cause in issue_details["possible_causes"]
    )

    solutions = "\n".join(
        f"{i+1}. {solution}"
        for i, solution in enumerate(issue_details["solutions"])
    )

    prompt = f"""
You are an IT Support Assistant.

Prepare a simple troubleshooting response.

Rules:
- No email format.
- No Subject.
- No Dear User.
- No Best Regards.
- No markdown (**).
- Use simple English.
- Maximum 12 lines.

Use exactly this format:

Issue Category: {category}
Priority: {issue_details["priority"]}

Possible Causes:
{possible_causes}

Suggested Solutions:
{solutions}

If the issue continues, contact the IT Support Team.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:

        return f"""
Issue Category: {category}
Priority: {issue_details["priority"]}

Possible Causes:
{possible_causes}

Suggested Solutions:
{solutions}

If the issue continues, contact the IT Support Team.
"""