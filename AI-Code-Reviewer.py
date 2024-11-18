from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

# config genai api keys
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
# initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# system prompt
sys_prompt = """
You are an expert AI code reviewer integrated into a user-friendly Python application. Your role is to analyze Python code submitted by users and provide the following:
1. ## Bug Report: Identify potential bugs, syntax errors, and logical flaws in the code.
2. ## Fixed Code: Return fixed or optimized code snippets alongside explanations of the changes made.
3. ## User Guidance: Ensure feedback is concise, easy to understand, and helpful for developers of varying experience levels.
Maintain a professional tone while keeping explanations simple and accessible. Focus on accuracy, efficiency, and improving the user's understanding of best coding practices.
"""

# function to get response
def get_response(sys_prompt, code):
    response = model.generate_content([sys_prompt, code])
    return response.text

# Title of the web app with emojis
st.title(":robot_face: AI Code Reviewer ")

# Instruction text
st.markdown(
    """
    Welcome to _**AI Code Reviewer**_! 🚀  
    """
)

# Text box for code input
code = st.text_area(":memo: _Enter your Python code here_...")

# Generate button with emoji
button = st.button(":sparkles: _Generate Review_")

# Add a header for the results
st.header("_Your AI-Powered Code Review_:scroll:")

if button:
    try:
        response = get_response(sys_prompt, code)
        st.write(response)
    except Exception as e:
        print(e)
