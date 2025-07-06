from prompts.zero_shot import zero_shot_template
from prompts.few_shot import few_shot_template
from prompts.cot_shot import cot_template
from agents.prompt_executor import run_prompt
from config import validate_api_keys

if __name__=="__main__":
    # Validate API keys on startup
    validate_api_keys()
    
    question = "What is the capital of France?"
    ground_truth = "Paris"

    shots = {
        "zero_shot": zero_shot_template(question),
        "few_shot": few_shot_template(question, k=2),
        "few_shot_3": few_shot_template(question, k=3),
        "few_shot_5": few_shot_template(question, k=5),
        "cot_shot": cot_template(question),
    }

    for model in ["gemini", "deepseek", "claude", "gpt"]:
        for shot_type, prompt in shots.items():
            print(f"\n[{model.upper()} - {shot_type}]")
            result = run_prompt(model, prompt, ground_truth)
            print(result)