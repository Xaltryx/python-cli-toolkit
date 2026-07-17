import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python Robust_File_Batch_Processor.py <folder>")
    sys.exit(1)

folder = Path(sys.argv[1]).resolve()

stats = {"files succeeded": 0, "files failed": 0, "file errors": {}}
word_count = 0

if folder.exists() and folder.is_dir():
    for file in folder.glob("*.txt"):
        try:
            with open(file, "r") as txt:
                word_count += len(txt.read().split())
                stats['files succeeded'] += 1
        except FileNotFoundError as e:
            print(f"File not found: {file}")
            stats['files failed'] += 1
            stats["file errors"][file] = str(e)
            continue
        except PermissionError as e:
            print(f"No permission to read: {file}")
            stats['files failed'] += 1
            stats["file errors"][file] = str(e)
            continue
        except UnicodeDecodeError as e:
            print(f"Unable to read the {file}: {e}")
            stats['files failed'] += 1
            stats["file errors"][file] = str(e)
            continue
else:
    print("Please enter an existed folder.")
    sys.exit(1)

print(f"Word Count: {word_count}")
print(f"File Succeded: {stats['files succeeded']}")
print(f"File Failed: {stats['files failed']}")

print("File errors:")
for file, error in stats["file errors"].items():
    print(f"{file} : {error}")