import sys
from pathlib import Path
import csv
try:
    from validators import is_valid_email, is_valid_phone
except ModuleNotFoundError as e:
    print(f"Can't find validators.py: {e}")
    sys.exit(1)
except ImportError as e:
    print(f"Cant find the functions, make sure you have the correct file: {e}")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)

file = Path(sys.argv[1]).resolve()
right_contact = []
wrong_contact = []
stats = {"Total":0, 'Valid Emails':0, 'Valid Phones':0}

try:
    with open(file, 'r', encoding= 'utf-8') as f_read:
        data = csv.DictReader(f_read)
        fieldnames_read = data.fieldnames

        if not fieldnames_read:
            print(f"The file {file} is empty or has no header row.")
            sys.exit(1)

        actual_phone_key = None
        actual_email_key = None
        actual_name_key = None

        for key in fieldnames_read:
            if 'name' in key.lower().strip() and actual_name_key is None:
                actual_name_key = key
            if ('phone' in key.lower().strip() or 'mobile' in key.lower().strip()) and actual_phone_key is None:
                actual_phone_key = key
            if 'email' in key.lower().strip() and actual_email_key is None:
                actual_email_key = key

            if actual_phone_key is not None and actual_email_key is not None and actual_name_key is not None:
                break

        if actual_phone_key is None or actual_email_key is None or actual_name_key is None:
            raise KeyError

        for row in data:
            stats['Total'] += 1
            phone = row[actual_phone_key]
            email = row[actual_email_key]
            name = row[actual_name_key]

            phone_bool = is_valid_phone(phone)
            email_bool = is_valid_email(email)

            if email_bool:
                stats['Valid Emails'] += 1

            if phone_bool:
                stats['Valid Phones'] += 1

except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(1)
except PermissionError as e:
    print(f"No permission to read: {e}")
    sys.exit(1)
except csv.Error as e:
    print(f"CSV error: {e}")
    sys.exit(1)
except KeyError as e:
    print(f"Error: The column phone number or email or name key was not found in the CSV headers!: {e}")
    sys.exit(1)

if stats['Total'] > 0:
    print(f"Total: {stats['Total']}, Valid email: {stats['Valid Emails']}, Valid phone: {stats['Valid Phones']}")
    sys.exit(0)
else:
    print("No data found.")
    sys.exit(1)