import os
import openai

<<<<<<< HEAD
openai.api_key = os.getenv('API_KEY', 'default_api_key')  # Set the API key globally

def generate_content(title, keywords, avoid_keywords, content_type, length, number_of_contents, service_areas, api_key):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nNumber of Contents: {number_of_contents}\nService Areas: {service_areas}\n\nContent:"
    
    response = openai.Completion.create(
        model="text-davinci-003",  # Ensure you use the correct model identifier
        prompt=prompt,
        max_tokens=length,
        # Removed the api_key parameter since the API key is set globally
    )
    content = response['choices'][0]['text'].strip()  # Access response content
    tokens_used = response['usage']['total_tokens']  # Access token usage
=======
def generate_content(title, keywords, avoid_keywords, content_type, length, number_of_contents, service_areas, api_key):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nNumber of Contents: {number_of_contents}\nService Areas: {service_areas}\n\nContent:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=length,
        api_key=api_key
    )
    content = response.choices[0].text.strip()
    tokens_used = response.usage['total_tokens']
>>>>>>> 73ee3466d0f59f04ccc82fc2a1e7eb290f57178c
    return content, tokens_used
