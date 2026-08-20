import streamlit as st
from workflow import workflow
from datetime import datetime
import random
from utils import get_issue_details
# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Powered IT Support",
    page_icon="💻",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* Background */

.stApp{
    background:#F5F8FC;
}

/* Hide Streamlit Menu */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Main */

.block-container{
    max-width:1450px;
    padding-top:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#0F172A;
    border-right:1px solid #1E293B;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Hero */

.hero{

background:linear-gradient(135deg,#2563EB,#60A5FA);

padding:35px;

border-radius:25px;

color:white;

box-shadow:0px 15px 35px rgba(37,99,235,.25);

margin-bottom:25px;

}

.hero h1{

font-size:34px;

margin-bottom:10px;

}

.hero p{

font-size:16px;

line-height:1.8;

}

/* Dashboard Card */

.card{

background:white;

padding:20px;

border-radius:20px;

border:1px solid #E2E8F0;

box-shadow:0px 8px 20px rgba(0,0,0,.05);

transition:.25s;

height:100%;

}

.card:hover{

transform:translateY(-4px);

box-shadow:0px 15px 30px rgba(37,99,235,.12);

}

/* Card Title */

.card-title{

font-size:18px;

font-weight:700;

color:#0F172A;

margin-top:10px;

margin-bottom:8px;

}

.card-text{

font-size:14px;

color:#64748B;

line-height:1.7;

}

/* Badge */

.badge{

display:inline-block;

background:#DBEAFE;

padding:6px 14px;

border-radius:30px;

font-size:13px;

font-weight:600;

color:#2563EB;

margin-bottom:12px;

}

/* Chat Input */

.stChatInput input{

border-radius:15px !important;

padding:15px !important;

font-size:15px !important;

border:1px solid #CBD5E1 !important;

}

/* Upload */

[data-testid="stFileUploader"]{

background:white;

padding:15px;

border-radius:15px;

border:2px dashed #60A5FA;

}

/* Scroll */

::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-thumb{
background:#CBD5E1;
border-radius:20px;
}

</style>
""",unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image("https://img.icons8.com/fluency/96/chatbot.png", width=70)
    st.title("IT Support")

    st.caption("AI Powered Help Desk")

    st.divider()

    st.markdown("### Navigation")

    st.write("🏠 Dashboard")

    st.write("🎫 New Ticket")

    st.write("📜 Chat History")

    st.write("📚 Knowledge Base")

    st.write("⚙ Settings")

    st.divider()

    st.success("🟢 AI Assistant Online")

    
# HERO SECTION

left, right = st.columns([2.2, 1])

with left:
    st.title("💻 AI IT Helpdesk Assistant")

    st.write("""
Smart Multi-Agent IT Support System that instantly resolves
WiFi, VPN, Printer, Outlook, Password, Camera, Microphone,
and Software issues with AI-powered troubleshooting.
""")

    st.success("🤖 AI Assistant is Ready to Help")

with right:
    st.image("images/robot.png", width=290)


    #Dashboard Cards==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("⚡ **Fast Response**\n\nAI agents instantly analyze your issue.")

with col2:
    st.info("🤖 **Multi-Agent AI**\n\nSpecialized AI agents solve different IT problems.")

with col3:
    st.info("🎫 **Smart Ticket**\n\nAutomatically generates professional support tickets.")

with col4:
    st.info("🟢 **24×7 Available**\n\nReceive instant IT support anytime.")

st.write("")



# ==========================================================
# MAIN DASHBOARD
# ==========================================================

left, right = st.columns([1, 2])

# ---------------- LEFT PANEL ---------------- #

with left:

    with st.container(border=True):

        st.subheader("🤖 Smart Features")

        st.write("✅ Automatic Issue Classification")
        st.write("✅ Priority Detection")
        st.write("✅ AI Multi-Agent Workflow")
        st.write("✅ Intelligent Troubleshooting")
        st.write("✅ Automatic Ticket Generation")
        st.write("✅ Secure & Reliable Processing")

    st.write("")

    
# ---------------- RIGHT PANEL ---------------- #

with right:

    with st.container(border=True):

        st.subheader("💬 AI Support Chat")

        st.write("""
Describe your IT issue below.

The AI Multi-Agent System will analyze your problem,
identify the category, assign priority, troubleshoot it,
and automatically generate a professional support ticket.
""")

        # Chat History
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

                # Chat Input
        user_issue = st.chat_input("💬 Describe your IT issue...")

        if user_issue:

            # Show user message immediately
            with st.chat_message("user"):
                st.markdown(user_issue)

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": user_issue
                }
            )

            # Assistant response
            with st.chat_message("assistant"):

                placeholder = st.empty()
                placeholder.markdown("🤖 *Analyzing your issue...*")

                try:
                    result = workflow.invoke(
                        {
                            "user_issue": user_issue,
                            "uploaded_image": None,
                            "category": "",
                            "issue_details": {},
                            "final_response": ""
                        }
                    )

                    category = result["category"]
                    details = get_issue_details(category)
                    priority = details["priority"]

                    ticket_id = f"IT-{random.randint(1000,9999)}"
                    current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")

                    ai_response = f"""
🎫 **Ticket Successfully Created**

🆔 **Ticket ID:** {ticket_id}

📅 **Created:** {current_time}

🟢 **Status:** Open

🚨 **Priority:** {priority}

---

{result["final_response"]}
"""

                    placeholder.markdown(ai_response)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": ai_response
                        }
                    )
                    st.rerun()

                except Exception as e:
                    placeholder.error(f"❌ {e}")


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;
color:#64748B;
font-size:13px;">

© 2026 AI IT Helpdesk Assistant

<br>

Built with ❤️ using Python • Streamlit • LangGraph • Google Gemini

</div>
""",
unsafe_allow_html=True
)

