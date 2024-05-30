# 설치 필요
# pip install streamlit langchain

import streamlit as st
from langchain_community.llms import OpenAI

# 다크 모드 CSS
dark_mode_css = """
<style>
    body, .css-1d391kg, .css-1wvyk6x, .css-1v3fvcr, .css-k1vhr4 {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput, .stTextArea, .stSelectbox, .stCheckbox, .stNumberInput, .stDateInput {
        background-color: #333333;
        color: white;
        border: 1px solid #ffffff;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox select, .stNumberInput input, .stDateInput input {
        color: white;
    }
    .stAlert, .stForm, .stSidebar, .stSidebarContent {
        background-color: #444444;
        border: 1px solid #555555;
    }
    .css-1v3fvcr, .css-k1vhr4 {
        border-color: #555555;
    }
</style>
"""

# 다크 모드 설정 함수
def set_dark_mode():
    st.markdown(dark_mode_css, unsafe_allow_html=True)

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, max_tokens=1000)
    response = llm(input_text)
    st.info(response)

# 초기 다크 모드 상태
is_dark_mode = False

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    
    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
    
    if submitted:
        if text.strip().lower() == "/다크모드":
            is_dark_mode = True
            st.success("다크 모드가 활성화되었습니다.")
        elif openai_api_key.startswith('sk-'):
            generate_response(text)

# 다크 모드가 활성화된 경우 CSS 적용
if is_dark_mode:
    set_dark_mode()
