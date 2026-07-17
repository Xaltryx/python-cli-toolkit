import sys
from pathlib import Path
import json

if len(sys.argv) < 3:
    print("Usage: python json_config_reader.py <file> <key>")
    sys.exit(1)

file = sys.argv[1]
key = sys.argv[2]

try:
    with open(file, 'r') as j:
        data = json.load(j)
        print(data[key])
except FileNotFoundError:
    print(f"File not found: {file}")
    sys.exit(1)
except PermissionError:
    print(f"No permission to read: {file}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    sys.exit(1)
except KeyError as e:
    print(f"Configuration Error: Missing expected data key: {e}")
    sys.exit(1)