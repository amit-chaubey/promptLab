import anthropic
from config import MODEL_CONFIGS

def run_claude(prompt: str) -> str:
    api_key = MODEL_CONFIGS["claude"]["api_key"]
    if not api_key:
        return "Error: Anthropic API key not configured. Please set ANTHROPIC_API_KEY in your .env file."
    
    # Create client with API key
    client = anthropic.Anthropic(api_key=api_key)
    
    # Handle different prompt formats
    if isinstance(prompt, dict):
        content = prompt.get("user", prompt.get("prompt", ""))
    else:
        content = prompt
    
    try:
        response = client.messages.create(
            model=MODEL_CONFIGS["claude"]["model"],
            messages=[{"role": "user", "content": content}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Anthropic API: {str(e)}"