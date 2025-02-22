import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

system_prompt='''you are built just to solve the error in python code.if you were asked something other
than codes tell that you are there to solve only code related issues.think of user as a beginner who
is learning python.provide them only the bug report of all the errors and the corrected code.'''

model=genai.GenerativeModel(model_name='models/gemini-2.0-flash-exp',system_instruction=system_prompt)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #006400, #32CD32, #FFD700, #FF8C00, #FF4500);
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('AI CodeMaster 🏆📝')

code = st.text_area("Code Input : ", placeholder="Paste your code here...")

button=st.button("🔮 See the Magic!")

if button:
    st.write("🎩✨ Ta-da! Magic happens.")

    response=model.generate_content(code)
    st.write(response.text)
    