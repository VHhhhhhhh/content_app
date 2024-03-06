import os
import openai

openai.api_key = os.getenv('API_KEY', 'default_api_key')  # Set the API key globally

def generate_content(title, keywords, avoid_keywords, content_type, length, number_of_contents, service_areas, api_key):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nNumber of Contents: {number_of_contents}\nService Areas: {service_areas}\n\nContent:"
    
    response = openai.Completion.create(
        model="gpt-4-turbo-0125",  # Specify the GPT-4 Turbo model
        prompt=prompt,
        max_tokens=length,
        api_key=api_key
    )
    content = response['choices'][0]['text'].strip()  # Access response content
    tokens_used = response['usage']['total_tokens']  # Access token usage
    return content, tokens_used
