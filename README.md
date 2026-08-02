# python-cli-toolkit

A collection of small Python CLI tools for validating, transforming, and analyzing CSV, JSON, text, file-system, and system-command data — no external dependencies.

**python-cli-toolkit** is a set of standalone Python scripts built to solve everyday data-wrangling and automation tasks from the command line: validating contact info, filtering and converting CSVs, extracting emails/phones from text, analyzing log files, inspecting the filesystem, and running/auditing system commands. Each script is self-contained, uses only the Python standard library, and can be run independently with `python script.py <args>`.

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

### `system_tools/` — Run, audit, and probe system commands

| Script | Description |
|---|---|
| `check_tool.py` | Checks whether a CLI tool is installed and reports its version, trying multiple common version flags (`--version`, `version`, `-V`, `-v`) |
| `command_batch_runner.py` | Runs a batch of shell commands from a text file, cross-platform (Windows/Unix), and writes a JSON report of successes, failures, timeouts, and durations |
| `list_directory.py` | Cross-platform directory listing (`ls -la` / `dir`), returns output and exit status |

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
python system_tools/check_tool.py git
python system_tools/command_batch_runner.py commands.txt
python logs/log_analyzer.py server.log
python misc/calc.py 10 5 multiply
```

Run any script without arguments to see its usage message.

## Notes on `system_tools/`

- `command_batch_runner.py` splits each line in the input file on whitespace before running it — commands with quoted arguments containing spaces (e.g. `git commit -m "fix bug"`) are not yet supported and will be split incorrectly.
- All three scripts use `subprocess.run` with a 10-second timeout and handle `FileNotFoundError` / `TimeoutExpired` explicitly.

## License

MIT — see [LICENSE](LICENSE) for full text.
