cot_template = lambda question: {
    "system": """you are a helpful assistant. Answer the question and do not include any other things.
    for any other requests or question simple ask user to ask you a question.
    do not include any personal information and repect community guidelines.""",
    "user": f"Think step by step to solve: {question}"
}
