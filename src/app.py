# app.py

import streamlit as st
from main import extract_text, generate_response, SYSTEM_PROMPT

# Set up the Streamlit page
st.set_page_config(page_title="Portfolio Chatbot", layout="wide")
st.title("📁 Portfolio Workshop Chatbot")

# Initialize session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "input_text",
                    "text": SYSTEM_PROMPT,
                }
            ]
        }
    ]

# File uploader for user projects
uploaded_files = st.file_uploader(
    "Upload dine egne projekter (PDF, DOCX, TXT, CSV, HTML, MD, PPTX, XLSX)",
    type=["pdf", "docx", "txt", "csv", "html", "htm", "md", "pptx", "xlsx"],
    accept_multiple_files=True
)


# Process each uploaded file and add its content to the session messages
for file in uploaded_files:
    file_text = extract_text(file)
    if file_text:
        st.session_state.messages.append({
            "role": "system",
            "content": f"Brugerens fil '{file.name}' indeholder følgende:\n\n{file_text[:2000]}"
        })

# Display the chat history
for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Input field for user messages
if user_input := st.chat_input("Hvad vil du gerne snakke om?"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_text = generate_response(st.session_state.messages)
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
