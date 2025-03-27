from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

context = "The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by NASA, which succeeded in preparing and landing the first humans on the Moon from 1968 to 1972."
question = "Which organization was responsible for the Apollo program?"

input_text = f"""Answer the following question based on the given context.

Context: {context}

Question: {question}

Answer:"""

inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs["input_ids"], max_length=100, num_beams=4, early_stopping=True)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(answer)  # Expected: NASA