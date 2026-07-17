# python-cli-toolkit

A collection of small Python CLI tools for validating, transforming, and analyzing CSV, JSON, text, and file-system data — no external dependencies.

**python-cli-toolkit** is a set of standalone Python scripts built to solve everyday data-wrangling tasks from the command line: validating contact info, filtering and converting CSVs, extracting emails/phones from text, analyzing log files, and inspecting the filesystem. Each script is self-contained, uses only the Python standard library, and can be run independently with `python script.py <args>`.

## Requirements

- Python 3.8+
- No external dependencies — everything uses the standard library only

## Structure

### `contacts/` — Validate and clean contact lists from CSV files

| Script | Description |
|---|---|
| `contact_validator_basic.py` | Splits contacts into valid/invalid CSV + JSON by email & phone |
| `contact_validator_with_stats.py` | Same, plus a summary count of valid emails/phones |
| `contact_validator_full.py` | Same, plus cross-references contacts against emails/phones found in a separate text file |
| `validators.py` | Shared email/phone regex validation used across the contact scripts |
| `extractors.py` | Shared email/phone extraction from free text |

### `csv_tools/` — Filter, validate, and convert CSV/JSON data

| Script | Description |
|---|---|
| `csv_phone_validator.py` | Flags invalid phone numbers in a CSV with a reason per row |
| `filter_csv_by_age.py` | Filters CSV rows by an age threshold, writes in batches |
| `RowWeaver.py` | Converts a CSV file into JSON |
| `get_json_value.py` | Looks up a single key's value in a JSON config file |

### `filesystem/` — Inspect and process files/folders

| Script | Description |
|---|---|
| `file_reader.py` | Reads and prints a file's contents |
| `folder_scanner.py` | Lists files in a folder, optionally filtered by extension |
| `extension_counter.py` | Counts files in a folder by extension |
| `path_checker.py` | Reports whether a given path is a file, folder, or doesn't exist |
| `Robust_File_Batch_Processor.py` | Word-counts all `.txt` files in a folder, tracks read failures |

### `logs/`

| Script | Description |
|---|---|
| `log_analyzer.py` | Parses timestamped log files into error/info/warning counts, unique messages, and busiest hour, output as JSON |

### `text_tools/`

| Script | Description |
|---|---|
| `EmailScoop.py` | Extracts all email addresses found in a text file |

### `misc/`

| Script | Description |
|---|---|
| `calc.py` | Basic command-line calculator (add/subtract/multiply/divide) |

## Usage

Each script is run directly with Python, e.g.:

```bash
python contacts/contact_validator_full.py contacts.csv notes.txt
python csv_tools/filter_csv_by_age.py people.csv 21
python logs/log_analyzer.py server.log
python misc/calc.py 10 5 multiply
```

Run any script without arguments to see its usage message.

## License

MIT
