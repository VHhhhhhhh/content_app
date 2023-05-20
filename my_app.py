import streamlit as st
from my_chatbot import generate_content
from config import api_key 

st.title('Content Generator')

title = st.text_input("Title:")
keywords = st.text_input("Keywords:")
avoid_keywords = st.text_input("Avoid Keywords:")
content_type = st.text_input("Content Type:")
length = st.number_input("Length:", min_value=100, max_value=10000, step=100)
number_of_contents = st.number_input("How Many:", min_value=1, max_value=100, step=1)
service_areas = st.text_input("Service Areas:")

if st.button('Generate'):
    total_length = 0
    total_tokens = 0
    for i in range(number_of_contents):
        content, tokens_used = generate_content(title, keywords, avoid_keywords, content_type, length, number_of_contents, service_areas, api_key)
        content_length = len(content.split())
        st.markdown(f"**{i+1}. ({content_length} words)**\n{content}\n")
        total_length += content_length
        total_tokens += tokens_used

    st.write(f"Total words generated: {total_length}")
    st.write(f"Total tokens used: {total_tokens}")
