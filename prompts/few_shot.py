EXAMPLES = [
    {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4"
    },
    {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    {
        "question": "What is the capital of Italy?",
    }
]

def few_shot_template(question, k):
    examples = EXAMPLES[:k]
    examples_str = "\n".join([f"Q: {ex['question']}\nA: {ex['answer']}" for ex in examples])

    return {
    "system": """ou are a helpful assistant. Answer the question and do not include any other things.
    for any other requests or question simple ask user to ask you a question.
    do not include any personal information and repect community guidelines.""",
    
    "user": f"""{examples_str }Answer the following question: {question}"""
    }