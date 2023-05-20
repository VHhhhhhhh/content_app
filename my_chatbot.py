import os
import openai
import streamlit as st
from my_chatbot import generate_content

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
    total_cost = 0
    total_tokens = 0
    for _ in range(number_of_contents):
        try:
            content = generate_content(title, keywords, avoid_keywords, content_type, length)
            st.write(content)
            total_length += len(content.split())
            total_tokens += len(content)
            total_cost += total_tokens / 10**6 * openai.Pricing.unit_cost  # assuming $0.06 per token
        except Exception as e:
            st.error(f"An error occurred: {e}")
            break

    st.write(f"Total words generated: {total_length}")
    st.write(f"Total tokens used: {total_tokens}")
    st.write(f"Total cost: ${total_cost:.2f}")

# Import the necessary modules
import config

# Access the API key from the config.py file
api_key = config.api_key

# Use the API key in your code
# ...

requirements.txt:
streamlit
openai
