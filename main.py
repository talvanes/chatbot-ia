from dotenv import load_dotenv
import os

import streamlit as st
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

ai_model = OpenAI(api_key=api_key)

st.title("Chatbot com IA")

# TODO initialize with "System Instructions" to make the assistant look like more like a persona

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state["messages"]:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content)

user_text = st.chat_input("Digite sua mensagem aqui...")

if user_text:
    st.chat_message("user").write(user_text)

    user_message = {"role": "user", "content": user_text}
    st.session_state["messages"].append(user_message)

    # AI has answered
    assistant_response = ai_model.chat.completions.create(
        messages=st.session_state["messages"], 
        model="gpt-5-nano"
    )
    assistant_response_text = assistant_response.choices[0].message.content
    
    assistant_message = {"role": "assistant", "content": assistant_response_text}
    st.session_state["messages"].append(assistant_message)

    st.chat_message("assistant").write(assistant_response_text)
