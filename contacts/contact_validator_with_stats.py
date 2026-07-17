import sys
from pathlib import Path
import csv
import json
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
correct_file_name = f"correct_contact_address_{file.stem}.csv"
wrong_file_name = f"wrong_contact_address_{file.stem}.json"
right_contact = []
wrong_contact = []

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

        headers_correct = [actual_name_key, actual_email_key, actual_phone_key]

        for row in data:
            contact = {}

            phone = row[actual_phone_key]
            email = row[actual_email_key]
            name = row[actual_name_key]

            phone_bool = is_valid_phone(phone)
            email_bool = is_valid_email(email)

            contact[actual_name_key] = name
            contact[actual_email_key] = email
            contact[actual_phone_key] = phone

            if phone_bool and email_bool:
                right_contact.append(contact)
            elif phone_bool and not email_bool:
                contact['reason'] = "bad email"
                wrong_contact.append(contact)
            elif not phone_bool and email_bool:
                contact['reason'] = "bad phone"
                wrong_contact.append(contact)
            elif not phone_bool and not email_bool:
                contact['reason'] = "bad phone and email"
                wrong_contact.append(contact)

    with open(correct_file_name, "w", newline='', encoding='utf-8') as correct_f:
        writer = csv.DictWriter(correct_f, fieldnames=headers_correct)
        writer.writeheader()
        writer.writerows(right_contact)
        print(f"Finished {correct_file_name}")

    with open(wrong_file_name, "w", newline='', encoding='utf-8') as wrong_f:
        writer = json.dump(wrong_contact, wrong_f, indent=2)
        print(f"Finished {wrong_file_name}")

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