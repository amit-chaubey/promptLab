import google.generativeai as genai
from config import MODEL_CONFIGS

def run_gemini(prompt: str) -> str:
    api_key = MODEL_CONFIGS["gemini"]["api_key"]
    if not api_key:
        return "Error: Gemini API key not configured. Please set GEMINI_API_KEY in your .env file."
    
    # Configure the API key
    genai.configure(api_key=api_key)
    
    # Create model instance
    model = genai.GenerativeModel(MODEL_CONFIGS["gemini"]["model"])
    
    # Generate response
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"