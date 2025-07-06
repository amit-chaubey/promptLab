from .metrics import basic_accuracy

def evaluate_response(output, ground_truth):
    """Evaluate a single response against ground truth"""
    accuracy = basic_accuracy(output, ground_truth)
    return accuracy

def evaluate_model(output, ground_truth):
    accuracy = basic_accuracy(output, ground_truth)
    return {
        "accuracy": accuracy,
    }