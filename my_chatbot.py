import os
from openai import OpenAI

# Instantiate a client and set the API key from the environment variable
client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_content_v1(title, keywords, avoid_keywords, content_type, length, service_areas):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nService Areas: {service_areas}\n\nContent:"
    
    try:
        # Create a completion with the desired model, prompt, and parameters using client.completions.create
        completion = client.completions.create(
            model="gpt-4-0125-preview",
            prompt=prompt,
            max_tokens=length,
            endpoint="v1/completions"
        )
        content = completion.choices[0].text.strip()  # Access response content
        tokens_used = completion.usage.total_tokens  # Access token usage
        content_length = len(content.split())  # Calculate content length
        return content, tokens_used, content_length
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
