# PromptLab

A comprehensive prompt engineering and evaluation framework for testing different LLM providers and prompting strategies.

## Features

- **Multiple LLM Providers**: Support for Gemini, OpenAI GPT, Anthropic Claude, and DeepSeek
- **Prompting Strategies**: Zero-shot, few-shot, and chain-of-thought prompting
- **Evaluation Framework**: Automated response evaluation and scoring
- **Logging**: Comprehensive logging of prompts, responses, and evaluations
- **Modular Design**: Clean separation of concerns with configurable components

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

You have several options to set up your API keys:

#### Option A: Interactive Setup (Recommended)
```bash
python setup_api_keys.py
```

#### Option B: Manual Setup
1. Copy the content from `env_example.txt`
2. Create a `.env` file in the project root
3. Replace the placeholder values with your actual API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

#### Option C: Environment Variables
Set the API keys as environment variables:
```bash
export GEMINI_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"
export ANTHROPIC_API_KEY="your_key_here"
export DEEPSEEK_API_KEY="your_key_here"
```

### 3. Get API Keys

- **Gemini**: [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenAI**: [OpenAI Platform](https://platform.openai.com/api-keys)
- **Anthropic**: [Anthropic Console](https://console.anthropic.com/)
- **DeepSeek**: [DeepSeek Platform](https://platform.deepseek.com/)

## Usage

### Basic Usage

```python
from main import run_prompt

# Test a single model
result = run_prompt("gemini", "What is the capital of France?", "Paris")
print(result)
```

### Run All Models

```bash
python main.py
```

This will test all configured models with different prompting strategies on the sample question.
       

## Security

- API keys are stored in `.env` files (not committed to git)
- The `.env` file is automatically ignored by version control
- Use the interactive setup script for secure key entry

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License
