import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python path_checker.py <folder>")
    sys.exit(1)

item = Path(sys.argv[1]).resolve()

if item.exists():
    if item.is_file():
        print("The existed item is a file.")
    elif item.is_dir():
        print("The existed item is a folder.")
else:
    print("The item doesnt exist.")