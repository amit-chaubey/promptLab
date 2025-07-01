import importlib
import json
from datetime import datetime


def log_result(entry, file_path):
    with open(file_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
        