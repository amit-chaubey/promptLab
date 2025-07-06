import google.generativeai as genai
import re
from config import MODEL_CONFIGS

def run_gemini(prompt: str) -> str:
    api_key = MODEL_CONFIGS["gemini"]["api_key"]
    if not api_key:
        return "Error: Gemini API key not configured. Please set GEMINI_API_KEY in your .env file."
    
    # Configure the API key
    genai.configure(api_key=api_key)
    
    # Handle different prompt formats
    if isinstance(prompt, dict):
        content = prompt.get("user", prompt.get("prompt", ""))
    else:
        content = prompt
    
    try:
        # Create model instance
        model = genai.GenerativeModel(MODEL_CONFIGS["gemini"]["model"])
        response = model.generate_content(content)
        result = response.text
        
        # Clean up response formatting for better evaluation
        # Remove common prefixes like "A: " or "Answer: "
        result = re.sub(r'^(A:|Answer:)\s*', '', result.strip())
        
        return result
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"