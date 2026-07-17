import sys
from pathlib import Path
import csv

if len(sys.argv) < 3:
    print("Usage: python filter_csv_by_age.py <file> <age>")
    sys.exit(1)

file = Path(sys.argv[1]).resolve()

try:
    age = int(sys.argv[2])
except ValueError:
    print("Please write a number in the age filed.")
    sys.exit(1)
filtered_rows = []
new_file_name = f"filtered_{file.name}_by_age_more_than_{age}.csv"

try:
    with open(file, 'r') as f_read:
        data = csv.DictReader(f_read)
        fieldnames_read = data.fieldnames

        if not fieldnames_read:
            print(f"The file {file} is empty or has no header row.")
            sys.exit(1)
        
        actual_key = None

        for name in fieldnames_read:
            if name.lower().strip() == 'age':
                actual_key = name
                break
        if actual_key is None:
            raise KeyError
        with open(new_file_name, "w", newline = "") as f_write:
            writer = csv.DictWriter(f_write,fieldnames= fieldnames_read)
            writer.writeheader()

        for row in data:
            try:
                if int(row[actual_key]) > age:
                    filtered_rows.append(row)

                if len(filtered_rows) >= 1000:
                    with open(new_file_name, "a", newline = "") as f_write:
                        writer = csv.DictWriter(f_write,fieldnames= fieldnames_read)
                        writer.writerows(filtered_rows)
                        filtered_rows.clear()
            except ValueError:
                print(f"The age field doesn't contain an integer in: {row}")

        with open(new_file_name, "a", newline = "") as f_write:
            writer = csv.DictWriter(f_write,fieldnames= fieldnames_read)
            writer.writerows(filtered_rows)
            filtered_rows.clear()
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
except KeyError:
    print(f"Error: The column 'age' was not found in the CSV headers!")
    sys.exit(1)