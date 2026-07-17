import sys
from pathlib import Path
import csv
import json

if len(sys.argv) < 2:
    print("Usage: python RowWeaver.py <file>")
    sys.exit(1)

file = Path(sys.argv[1]).resolve()
new_file_name = f"{file.stem}.json"
temp = list()

try:
    with open(file, 'r') as f_read:
        data = csv.DictReader(f_read)
        fieldnames_read = data.fieldnames
        data_list = list(data)

        if not fieldnames_read:
            print(f"The file {file} is empty has no header row.")
            sys.exit(1)

        with open(new_file_name, "w") as f_write:
            writer = json.dump(data_list, f_write, indent=2)
            print(f"Finished Writing {new_file_name}")

except FileNotFoundError:
    print(f"File not found: {file}")
    sys.exit(1)
except PermissionError:
    print(f"No permission to read: {file}")
    sys.exit(1)
except csv.Error as e:
    print(f"CSV error: {e}")
    sys.exit(1)