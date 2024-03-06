import streamlit as st
from my_chatbot import generate_content
# Removed the import of api_key since it's not used directly

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
        # Removed api_key from the arguments
        content, tokens_used = generate_content(title, keywords, avoid_keywords, content_type, length, 1, service_areas)  # Note: Passing 1 instead of number_of_contents
        content_length = len(content.split())
        content = content.replace('\n', '<br/>')
        st.markdown(f"**{i+1}. ({content_length} words)**<br/>{content}", unsafe_allow_html=True)
        total_length += content_length
        total_tokens += tokens_used

    st.write(f"Total words generated: {total_length}")
    st.write(f"Total tokens used: {total_tokens}")
