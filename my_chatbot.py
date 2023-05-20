import os
import openai

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
    return content, tokens_used
