import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys - Load from .env file first, then fall back to environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")

# Validate that required API keys are present
def validate_api_keys():
    """Validate that API keys are configured"""
    missing_keys = []
    
    if not GEMINI_API_KEY:
        missing_keys.append("GEMINI_API_KEY")
    if not OPENAI_API_KEY:
        missing_keys.append("OPENAI_API_KEY") 
    if not ANTHROPIC_API_KEY:
        missing_keys.append("ANTHROPIC_API_KEY")
    if not DEEPSEEK_API_KEY:
        missing_keys.append("DEEPSEEK_API_KEY")
    
    if missing_keys:
        print(f"⚠️  Warning: Missing API keys: {', '.join(missing_keys)}")
        print("   These models will not work without valid API keys.")
        print("   Update your .env file or set environment variables.")
    
    return len(missing_keys) == 0

# Model provider mappings
MODEL_PROVIDERS = {
    "gemini": "models.gemini",
    "gpt": "models.gpt", 
    "claude": "models.claude",
    "deepseek": "models.deepseek"
}

# Model configurations
MODEL_CONFIGS = {
    "gemini": {
        "model": "gemini-1.5-flash",
        "api_key": GEMINI_API_KEY
    },
    "gpt": {
        "model": "gpt-4",
        "api_key": OPENAI_API_KEY
    },
    "claude": {
        "model": "claude-3-5-sonnet-20240620",
        "api_key": ANTHROPIC_API_KEY
    },
    "deepseek": {
        "model": "deepseek-chat",
        "api_key": DEEPSEEK_API_KEY
    }
} 