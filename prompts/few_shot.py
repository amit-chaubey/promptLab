EXAMPLES = [
    {
        "question": "What is the capital of France?",
        "ground_truth": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "ground_truth": "4"
    },
    {
        "question": "What is the capital of Germany?",
        "ground_truth": "Berlin"
    },
    {
        "question": "What is the capital of Italy?",
        "ground_truth": "Rome"
    }
]

def few_shot_template(question, k=2):
    examples = EXAMPLES[:k]
    examples_str = "\n".join([f"Q: {ex['question']}\nA: {ex['ground_truth']}" for ex in examples])

    return {
    "system": """You are a helpful assistant. Answer the question and do not include any other things.
    For any other requests or questions, simply ask the user to ask you a question.
    Do not include any personal information and respect community guidelines.""",
    
    "user": f"""{examples_str}

Answer the following question: {question}"""
    }