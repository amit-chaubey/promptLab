import openai

def run_gpt(prompt_dict):
    messages = [
        {"role": "system", "content": prompt_dict["system"]},
        {"role": "user", "content": prompt_dict["user"]}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]
