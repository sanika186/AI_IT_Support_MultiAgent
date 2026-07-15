# AI IT Support Multi-Agent System

## Project Overview

This project is a simple AI-based IT Support System developed using Python, LangGraph, LangChain and Google Gemini API.

The main purpose of this project is to help users solve common IT issues like VPN problems, WiFi issues, printer errors, Outlook issues, password problems and other basic technical issues.

The system first identifies the issue category and then provides suitable troubleshooting steps.

---

## Features

- Detects different IT support issues
- Uses a Multi-Agent workflow
- Uses Google Gemini API
- Reads issue details from a JSON knowledge base
- Generates troubleshooting steps
- Generates a Ticket ID for every request
- Displays current date and time
- Simple console-based interface

---

## Technologies Used

- Python
- LangGraph
- LangChain
- Google Gemini API
- JSON
- Python Dotenv

---

## Project Structure

```
AI_IT_Support_MultiAgent/

│── app.py
│── agents.py
│── workflow.py
│── utils.py
│── prompts.py
│── knowledge_base.json
│── sample_tickets.txt
│── requirements.txt
│── README.md
│── .env
│── .gitignore
```

---

## Supported Issues

The system can identify the following issues:

- VPN
- WiFi
- Printer
- Outlook
- Password
- Software Installation
- Blue Screen
- Bluetooth
- Camera
- Microphone
- Slow Computer

---

## How it Works

1. User enters an IT issue.
2. The Classifier Agent identifies the issue category.
3. The system loads the related information from the Knowledge Base.
4. The Solution Agent generates troubleshooting steps.
5. The final response is displayed with Ticket ID and Date & Time.

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-link>
```

### 2. Open the project folder

```bash
cd AI_IT_Support_MultiAgent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

### 6. Add your Gemini API Key

Create a `.env` file and add:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 7. Run the project

```bash
python app.py
```

---

## Sample Input

```
camera not working
```

## Sample Output

```
Issue Category: Camera

Priority: Medium

Possible Causes:
- Camera permission disabled
- Driver issue

Suggested Solutions:
1. Enable camera permission
2. Restart the application

Status: Open
```

---

## Future Improvements

- Add a graphical user interface
- Store support tickets in a database
- Add voice support
- Support more IT issues
- Add user login system

---

## Conclusion

This project is a simple AI-based IT Support Multi-Agent System that can identify common IT issues and provide troubleshooting steps. It is built using LangGraph, Google Gemini API and a JSON knowledge base. The project is easy to understand and can be improved further by adding more features in the future.