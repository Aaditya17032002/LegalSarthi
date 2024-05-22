import time
import openai,os
from openai.error import RateLimitError

openai.api_key = os.getenv('OPENAI_API_KEY')  # Securely load your API key

def generate_document_content(context, placeholder):
    """
    Generates document content using the OpenAI API.
    This function is called by simulate_trained_model_generation in app.py
    """
    prompt = f"Generate a comprehensive paragraph for the {placeholder} based on: {context}"
    for _ in range(5):  # Retry up to 5 times
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the appropriate model ID
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content'].strip()
        except RateLimitError:
            time.sleep(1)  # Wait 1 second before retrying
    raise RateLimitError("Exceeded rate limit and retries")

