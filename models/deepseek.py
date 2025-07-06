import deepseek
from config import MODEL_CONFIGS

def run_deepseek(prompt: str) -> str:
    api_key = MODEL_CONFIGS["deepseek"]["api_key"]
    if not api_key:
        return "Error: DeepSeek API key not configured. Please set DEEPSEEK_API_KEY in your .env file."
    
    # Configure the API key
    deepseek.api_key = api_key
    
    # Handle different prompt formats
    if isinstance(prompt, dict):
        content = prompt.get("user", prompt.get("prompt", ""))
    else:
        content = prompt
    
    try:
        response = deepseek.chat.completions.create(
            model=MODEL_CONFIGS["deepseek"]["model"],
            messages=[{"role": "user", "content": content}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling DeepSeek API: {str(e)}"