import sys
from pathlib import Path
import csv
import re

if len(sys.argv) < 2:
    print("Usage: python csv_phone_validator.py <file>")
    sys.exit(1)

file = Path(sys.argv[1]).resolve()

try:
    with open(file, 'r') as f_read:
        data = csv.DictReader(f_read)
        fieldnames_read = data.fieldnames

        if not fieldnames_read:
            print(f"The file {file} is empty or has no header row.")
            sys.exit(1)

        actual_key = None

        for name in fieldnames_read:
            if 'phone' in name.lower().strip() or 'mobile' in name.lower().strip() :
                actual_key = name
                break

        if actual_key is None:
            raise KeyError
            
        for row in data:
            phone = row[actual_key]
            if bool(re.search(r"^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$", phone)):
                continue

            reasons = []

            if len(phone) == 0:
                reasons.append("phone number field is empty")
            elif bool(re.search(r"[^0-9-]", phone)):
                reasons.append("contains a non-digit character")
            else:
                if len(re.sub(r"^\+?1[-.\s]*", "", phone)) < 10:
                    reasons.append("less than 10 digits")
                elif len(re.sub(r"^\+?1[-.\s]*", "", phone)) > 10:
                    reasons.append("more than 10 digits")
                if not bool(re.search(r"^\+?1", phone)):
                    reasons.append("starts with a non-US country code")

            print(f"Invalid phone {phone}: {', '.join(reasons)} — row: {row}")
                    
except FileNotFoundError:
    print(f"File not found: {file}")
    sys.exit(1)
except PermissionError:
    print(f"No permission to read: {file}")
    sys.exit(1)
except csv.Error as e:
    print(f"CSV error: {e}")
    sys.exit(1)
except KeyError:
    print(f"Error: The column phone number was not found in the CSV headers!")
    sys.exit(1)
except re.error as e:
    print(f"Regex compilation failed! Error details: {e}")
    sys.exit(1)
