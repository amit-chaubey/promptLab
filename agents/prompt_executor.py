import importlib
import json
from datetime import datetime
from config import MODEL_PROVIDERS
from evaluation.evaluate import evaluate_response

def load_model_runner(model_key):
    module = importlib.import_module(MODEL_PROVIDERS[model_key])
    return getattr(module, f"run_{model_key}")

def log_result(entry, file_path):
    with open(file_path, "a") as f:
        f.write(json.dumps(entry) + "\n")

def run_prompt(model_key, prompt_dict, ground_truth=None):
    model_runner = load_model_runner(model_key)
    output = model_runner(prompt_dict)

    log_entry = {
        "timestamp": str(datetime.now()),
        "model": model_key,
        "input": prompt_dict,
        "output": output,
        "ground_truth": ground_truth,
    }

    log_result(log_entry, "logs/prompt_logs.jsonl")

    if ground_truth:
        score = evaluate_response(output, ground_truth)
        log_result({**log_entry, "score": score}, "logs/evaluation_logs.jsonl")

    return output

        