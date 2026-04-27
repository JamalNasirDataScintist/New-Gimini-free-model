import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini AI Chatbot")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Get response
        response = st.session_state.chat.send_message(user_input)
        bot_reply = response.text

        # Show bot message
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

    except Exception as e:
        st.error(f"Error: {e}")