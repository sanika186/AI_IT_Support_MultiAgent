import os
from dotenv import load_dotenv
from google import genai
from PIL import Image


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
    elif ("battery" in issue or  "charging" in issue or "charge" in issue or "battery drain" in issue   or "draining" in issue   or "low battery" in issue):
        return "Battery"
    elif ("slow" in issue or "lag" in issue  or "hanging" in issue or "cpu" in issue or "performance" in issue):  
        return "Slow Computer"
    else:
        return "Unknown"

def generate_solution(category, issue_details):

    possible_causes = ""
    for cause in issue_details["possible_causes"]:
        possible_causes += f"- {cause}\n"
    

    solutions = ""
    for i, solution in enumerate(issue_details["solutions"], 1):
        solutions += f"{i}. {solution}\n"

    prompt = f"""
You are an IT Support Assistant.

The user has reported a {category} issue.

Write ONLY a short troubleshooting summary in 2-3 lines.

Do not include:
- Issue Category
- Priority
- Possible Causes
- Suggested Solutions
- Greetings
- Markdown
"""

    try:

        response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)


        summary = response.text.strip()

    except Exception:

        summary = "Please follow the troubleshooting steps."

    final_response = f"""
**📌 Issue Category**

{category}

**🔍 Possible Causes**

{possible_causes}

**🛠 Suggested Solutions**

{solutions}

**🤖 AI Recommendation**

{summary}

If the issue continues, contact the IT Support Team.
"""


    return final_response

def analyze_screenshot(uploaded_file):
    return ""

    try:
        image = Image.open(uploaded_file)

        prompt = """
You are an IT Support Assistant.

Analyze this screenshot.

Return your answer in EXACTLY this format:

Category: <One of these only>
VPN
WiFi
Printer
Password
Outlook
Software Installation
Blue Screen
Bluetooth
Camera
Microphone
Battery
Slow Computer
Unknown

Issue: <Short description of the problem>

Error: <Exact error message if visible, otherwise None>

Do not return anything else.
"""

        response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image]
)
        print("Gemini Vision Response:")
        print(response.text)

        return response.text.strip()

    except Exception as e:
        print("Gemini Vision Error:", e)
        return f"ERROR: {str(e)}"