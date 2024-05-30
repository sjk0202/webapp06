# 설치 필요
# pip install streamlit langchain

import streamlit as st
from langchain_community.llms import OpenAI

# 다크 모드 CSS
dark_mode_css = """
<style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput, .stTextArea {
        background-color: #333333;
        color: white;
        border: 1px solid #ffffff;
    }
    .stTextInput input, .stTextArea textarea {
        color: white;
    }
    .stAlert {
        background-color: #444444;
        border: 1px solid #555555;
    }
</style>
"""

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, max_tokens=1000)
    response = llm(input_text)
    st.info(response)

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    
    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
    
    if submitted:
        if text.strip().lower() == "/다크모드":
            st.markdown(dark_mode_css, unsafe_allow_html=True)
            st.success("다크 모드가 활성화되었습니다.")
        elif openai_api_key.startswith('sk-'):
            generate_response(text)
