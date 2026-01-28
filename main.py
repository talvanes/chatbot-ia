"""
AI Chatbot Application using Streamlit and OpenAI.

This module provides a conversational interface powered by OpenAI's GPT models.
"""

# Standard library imports
import os
from typing import Dict, List, Optional

# Third-party imports
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Constants
DEFAULT_MODEL = "gpt-4o-mini"  # More reliable model than gpt-5-nano
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful and friendly AI assistant. Provide clear, concise, and accurate responses."
}


def initialize_environment() -> Optional[str]:
    """
    Load environment variables and retrieve the OpenAI API key.
    
    Returns:
        Optional[str]: The API key if found, None otherwise.
    """
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")


def initialize_openai_client(api_key: str) -> OpenAI:
    """
    Initialize and return an OpenAI client instance.
    
    Args:
        api_key: The OpenAI API key for authentication.
        
    Returns:
        OpenAI: Configured OpenAI client instance.
    """
    return OpenAI(api_key=api_key)


def initialize_session_state() -> None:
    """Initialize Streamlit session state with default values."""
    if "messages" not in st.session_state:
        st.session_state.messages = [SYSTEM_PROMPT]


def display_chat_history() -> None:
    """Display all messages from the chat history, excluding system messages."""
    for message in st.session_state.messages:
        if message["role"] != "system":  # Don't display system prompts
            st.chat_message(message["role"]).write(message["content"])


def get_ai_response(client: OpenAI, messages: List[Dict[str, str]], model: str) -> Optional[str]:
    """
    Get a response from the OpenAI API.
    
    Args:
        client: The OpenAI client instance.
        messages: List of conversation messages.
        model: The model identifier to use.
        
    Returns:
        Optional[str]: The assistant's response text, or None if an error occurred.
    """
    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=0.7,  # Balanced creativity
            max_tokens=1000,  # Reasonable response length
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        st.error(f"OpenAI API Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None


def main() -> None:
    """Main application entry point."""
    # Page configuration
    st.set_page_config(
        page_title="AI Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    
    st.title("🤖 Chatbot com IA")
    
    # Initialize environment and check API key
    api_key = initialize_environment()
    if not api_key:
        st.error("⚠️ API key not found. Please set the OPENAI_API_KEY environment variable.")
        st.info("Create a `.env` file with: `OPENAI_API_KEY=your_key_here`")
        st.stop()
    
    # Initialize OpenAI client
    try:
        ai_client = initialize_openai_client(api_key)
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {str(e)}")
        st.stop()
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat history
    display_chat_history()
    
    # User input
    user_text = st.chat_input("Digite sua mensagem aqui...")
    
    if user_text:
        # Display user message
        st.chat_message("user").write(user_text)
        
        # Add user message to history
        user_message = {"role": "user", "content": user_text}
        st.session_state.messages.append(user_message)
        
        # Get AI response
        with st.spinner("Pensando..."):
            assistant_response_text = get_ai_response(
                ai_client,
                st.session_state.messages,
                DEFAULT_MODEL
            )
        
        if assistant_response_text:
            # Add assistant message to history
            assistant_message = {"role": "assistant", "content": assistant_response_text}
            st.session_state.messages.append(assistant_message)
            
            # Display assistant response
            st.chat_message("assistant").write(assistant_response_text)


if __name__ == "__main__":
    main()
