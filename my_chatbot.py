import os
from openai import OpenAI
import traceback

client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_content_v1(title, keywords, avoid_keywords, content_type, length, service_areas):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\nService Areas: {service_areas}\n\nContent:"
    
    try:
        completion = client.completions.create(
            model="text-davinci-003",  # Adjusted to a standard model identifier
            prompt=prompt,
            max_tokens=length
        )
        content = completion.choices[0].text.strip()
        tokens_used = completion.usage.total_tokens
        content_length = len(content.split())
        return content, tokens_used, content_length
    except Exception as e:
        traceback.print_exc()
        print(f"Prompt used: {prompt}")
        print(f"Length: {length}")
        print(f"Service Areas: {service_areas}")
        return None, None, None
