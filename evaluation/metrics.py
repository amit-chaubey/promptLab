def basic_accuracy(output, ground_truth):
    return 1.0 if output.strip().lower() == ground_truth.strip().lower() else 0.0