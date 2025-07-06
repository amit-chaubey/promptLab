from .metrics import basic_accuracy

def evaluate_model(output, ground_truth):
    accuracy = basic_accuracy(output, ground_truth)
    return {
        "accuracy": accuracy,
    }