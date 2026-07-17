import sys
from pathlib import Path
import re

if len(sys.argv) < 2:
    print("Usage: python EmailScoop.py <file>")
    sys.exit(1)

file = Path(sys.argv[1]).resolve()

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

try:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = f_read.read()
        emails = re.findall(email_pattern, data)

        # Print them line by line if found, otherwise let the user know
        if emails:
            for email in emails:
                print(email)
        else:
            print("No emails found in this file.")

except FileNotFoundError:
    print(f"File not found: {file}")
    sys.exit(1)
except PermissionError:
    print(f"No permission to read: {file}")
    sys.exit(1)
except UnicodeDecodeError as e:
    print(f"File cant be read: {e}")
    sys.exit(1)