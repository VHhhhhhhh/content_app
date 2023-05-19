import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

def generate_content(title, keywords, avoid_keywords, content_type, length):
    prompt = f"Title: {title}\nKeywords: {keywords}\nAvoid: {avoid_keywords}\nType: {content_type}\nLength: {length}\n\nContent:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=length,
        api_key=api_key
    )
    return response.choices[0].text.strip()
