import gemini_api

def run_gemini(prompt: str) -> str:
    response = gemini_api.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )
    return response.text
