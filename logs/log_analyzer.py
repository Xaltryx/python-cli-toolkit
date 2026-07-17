import sys
from pathlib import Path
import re
import json

starting_pattern = r"^\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]) ([01]\d|2[0-3]):[0-5]\d:[0-5]\d\b"

if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py <txt_file>")
    sys.exit(1)

txt_file = Path(sys.argv[1]).resolve()
new_json_file = f"{txt_file.stem}_stats.json"
ERROR = set()
INFO = set()
WARNING = set()
hour_count = {}
wrong_line_count = 0
counts = {'ERROR': 0, 'INFO': 0, 'WARNING': 0}

try:
    with open(txt_file, 'r', encoding='utf-8') as f_txt_read:
        for line in f_txt_read:
            if bool(re.search(starting_pattern, line)):
                type = line.split()[2]
                hour_number = line.split()[1].split(':')[0]
                message = line.split(type)[1].strip()
                if type == 'ERROR':
                    ERROR.add(message)
                    counts["ERROR"] += 1
                elif type == 'INFO':
                    INFO.add(message)
                    counts["INFO"] += 1
                elif type == 'WARNING':
                    WARNING.add(message)
                    counts["WARNING"] += 1

                if hour_number not in hour_count.keys():
                    hour_count[hour_number] = 1
                elif hour_number in hour_count.keys():
                    hour_count[hour_number] += 1

            else:
                print(f"The line contain wrong charcters and orders.: {line}")
                wrong_line_count += 1

    print(f"There were {wrong_line_count} malformed lines.")

    report = {
        'count':
            {
            'ERROR': counts["ERROR"],
            'INFO': counts["INFO"],
            'WARNING': counts["WARNING"]
        },
        'messages' :
            {
            'ERROR': list(ERROR),
            'INFO': list(INFO),
            'WARNING': list(WARNING)
        },
        "busiest_hour": max(hour_count, key=hour_count.get)
    }

    with open(new_json_file, "w", newline='', encoding='utf-8') as json_export:
        json.dump(report, json_export, indent=2)
        print(f"Finished {new_json_file}")

except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(1)
except PermissionError as e:
    print(f"No permission to read: {e}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    sys.exit(1)
except KeyError as e:
    print(f"Configuration Error: Missing expected data key: {e}")
    sys.exit(1)
