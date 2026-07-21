# 💻 AI Powered IT Support Multi-Agent System

An intelligent AI-powered IT Helpdesk Assistant built using **Python, Streamlit, LangGraph, and Google Gemini**. The system automatically classifies IT issues, provides troubleshooting steps, prioritizes tickets, and generates professional IT support responses using a multi-agent workflow.

---

## 🚀 Features

- 🤖 AI-powered Multi-Agent Workflow
- 🧠 Automatic IT Issue Classification
- 📋 Intelligent Troubleshooting
- 🎫 Automatic Ticket Generation
- 🚨 Priority Detection
- ⚡ Fast AI Responses
- 💬 Interactive Chat Interface
- 📚 Knowledge Base Integration
- 🔒 Secure and Lightweight Architecture

---

## 🏗️ System Architecture

```
            User Query
                 │
                 ▼
      Issue Classification Agent
                 │
                 ▼
      Knowledge Base Retrieval
                 │
                 ▼
      Solution Generation Agent
                 │
                 ▼
      Professional IT Ticket
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| LangGraph | Multi-Agent Workflow |
| Google Gemini | AI Response Generation |
| JSON | Knowledge Base |
| CSS | UI Styling |

---

## 📂 Project Structure

```
AI_IT_Support_MultiAgent/
│
├── streamlit_app.py          # Streamlit Frontend
├── workflow.py               # LangGraph Workflow
├── agents.py                 # AI Agents
├── utils.py                  # Knowledge Base Functions
├── knowledge_base.json       # IT Knowledge Base
├── requirements.txt
├── images/
│   └── robot.png
└── README.md
```

---

## ⚙️ Multi-Agent Workflow

### 🧠 Agent 1 – Issue Classification

- Detects the user's IT issue
- Identifies the issue category
- Routes the request for troubleshooting

Supported categories include:

- WiFi
- VPN
- Outlook
- Printer
- Password
- Camera
- Microphone
- Software
- Hardware
- General IT Support

---

### 🤖 Agent 2 – Solution Generator

Uses:

- Knowledge Base
- Google Gemini AI

Generates:

- Step-by-step troubleshooting
- Professional recommendations
- User-friendly explanations

---

## 🎫 Ticket Generation

For every user request, the system automatically generates:

- Ticket ID
- Creation Time
- Issue Category
- Priority Level
- Troubleshooting Steps
- AI Generated Resolution

---

## 💬 Sample Query

```
My laptop is unable to connect to WiFi.
```

### Output

```
Ticket ID : IT-4821

Priority : High

Category : WiFi

Troubleshooting

• Restart the router
• Forget and reconnect to WiFi
• Update network drivers
• Run Windows Network Troubleshooter
• Restart your computer
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI_IT_Support_MultiAgent.git
```

Move into the project

```bash
cd AI_IT_Support_MultiAgent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

## 📸 Application Preview

> Add screenshots of the application here.

Example:

```
Home Page

Chat Interface

Generated Ticket
```

---

## 🔮 Future Enhancements

- Screenshot/Image Issue Analysis
- Voice-Based IT Support
- Database Integration
- User Authentication
- Email Ticket Notifications
- Admin Dashboard
- Ticket History
- Cloud Deployment

---

## 🎯 Learning Outcomes

This project demonstrates:

- Multi-Agent AI Systems
- LangGraph Workflows
- Prompt Engineering
- AI-powered Helpdesk Automation
- Streamlit Application Development
- Knowledge Base Integration
- Google Gemini API Integration

---

## 👩‍💻 Author

**Sanika Kulkarni**

AI/ML Enthusiast | Python Developer | Generative AI | Computer Vision | LangGraph


---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.