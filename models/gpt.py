import openai
from config import MODEL_CONFIGS

def run_gpt(prompt):
    api_key = MODEL_CONFIGS["gpt"]["api_key"]
    if not api_key:
        return "Error: OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file."
    
    # Configure the API key
    openai.api_key = api_key
    
    # Handle different prompt formats
    if isinstance(prompt, dict):
        messages = [
            {"role": "system", "content": prompt.get("system", "")},
            {"role": "user", "content": prompt.get("user", prompt.get("prompt", ""))}
        ]
    else:
        messages = [{"role": "user", "content": prompt}]
    
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_CONFIGS["gpt"]["model"],
            messages=messages
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error calling OpenAI API: {str(e)}"
