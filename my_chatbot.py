import os
from openai import OpenAI, APIError

# Instantiate a client and set the API key from the environment variable
client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_content_v1(title, keywords, avoid_keywords, content_type, length, service_areas):
    try:
        prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nService Areas: {service_areas}\n\nContent:"
        
        # Create a completion with the desired model, prompt, and parameters using client.completions.create
        completion = client.completions.create(
            model="gpt-4-0125-preview",
            prompt=prompt,
            max_tokens=length
        )
        content = completion.choices[0].text.strip()  # Access response content
        tokens_used = completion.usage.total_tokens  # Access token usage
        
        if content:
            content_length = len(content.split())
        else:
            content_length = 0
            
        return content, tokens_used, content_length
    except APIError as e:
        print(f"An error occurred: {e}")
        return None, None, None
