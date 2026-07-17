import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python filter.py <folder>")
    sys.exit(1)

folder = Path(sys.argv[1]).resolve()

if folder.exists() and folder.is_dir():
    for file in folder.iterdir():
        if file.is_file():
            print(file.name)
else:
    print("Please enter an existed folder.")