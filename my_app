import streamlit as st
from my_chatbot import generate_content

st.title('Content Generator')

title = st.text_input("Title:")
keywords = st.text_input("Keywords:")
avoid_keywords = st.text_input("Avoid Keywords:")
content_type = st.text_input("Content Type:")
length = st.number_input("Length:", min_value=100, max_value=10000, step=100)

if st.button('Generate'):
    content = generate_content(title, keywords, avoid_keywords, content_type, length)
    st.write(content)
