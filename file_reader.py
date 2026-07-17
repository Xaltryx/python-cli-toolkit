import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python file_reader.py <folder>")
    sys.exit(1)

item = Path(sys.argv[1]).resolve()

try:
    with open(item, 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print(f"File not found: {item}")
    sys.exit(1)
except PermissionError:
    print(f"No permission to read: {item}")
    sys.exit(1)

