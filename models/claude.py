import anthropic

def run_claude(prompt: str) -> str:
    response = anthropic.messages.create(
        model="claude-3-5-sonnet-20240620",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content