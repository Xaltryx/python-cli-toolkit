import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python extension_counter.py <folder>")
    sys.exit(1)

folder = Path(sys.argv[1]).resolve()

extension_counter = {}

if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        if file.is_file():
            extension_counter[file.suffix] = extension_counter.get(file.suffix, 0) + 1
else:
    print("Please enter an existed folder.")
    sys.exit(1)
    
sorted_by_key = dict(sorted(extension_counter.items()))

print(sorted_by_key)