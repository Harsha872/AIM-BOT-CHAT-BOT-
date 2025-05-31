import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure API key
gen_ai.configure(api_key=GOOGLE_API_KEY)

# List available models (optional - shows in Streamlit app)
models = gen_ai.list_models()
st.write("Available models:", models)

# Initialize the generative model (make sure the model name is correct and accessible)
model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session in Streamlit session state if not already
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Set Streamlit page title
st.title("🧠 AimBot Pro - ChatBot")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input area for user prompt
user_prompt = st.chat_input("Ask AimBot-Pro...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    # Send user prompt to the model and get response
    aimbot_response = st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(aimbot_response.text)
