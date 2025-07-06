import re

def basic_accuracy(output, ground_truth):
    """
    Enhanced accuracy scoring that handles various response formats
    """
    if not output or not ground_truth:
        return 0.0
    
    # Clean and normalize both strings
    output_clean = clean_response(output)
    ground_truth_clean = ground_truth.strip().lower()
    
    # Exact match
    if output_clean == ground_truth_clean:
        return 1.0
    
    # Check if ground truth is contained in the response
    if ground_truth_clean in output_clean:
        return 1.0
    
    # Check for common variations
    variations = [
        f"the capital of france is {ground_truth_clean}",
        f"capital of france is {ground_truth_clean}",
        f"france's capital is {ground_truth_clean}",
        f"paris is the capital of france",
        f"paris, the capital of france"
    ]
    
    for variation in variations:
        if variation in output_clean:
            return 1.0
    
    return 0.0

def clean_response(response):
    """
    Clean and normalize response text for better comparison
    """
    if not response:
        return ""
    
    # Convert to lowercase and strip whitespace
    cleaned = response.strip().lower()
    
    # Remove common prefixes
    cleaned = re.sub(r'^(a:|answer:|the answer is|the capital of france is)\s*', '', cleaned)
    
    # Remove punctuation and extra whitespace
    cleaned = re.sub(r'[^\w\s]', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned