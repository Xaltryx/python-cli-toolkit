import sys
import subprocess
import platform
import re

if len(sys.argv) != 2:
    print("Usage: python check_tool.py <tool>")
    sys.exit(1)

tool = sys.argv[1]
version_type = None
tool_exists = False
try:
    versions = ["--version", "version", "-V", "-v"]
    for version in versions:
        try:
            if platform.system() == "Windows":
                result = subprocess.run(["cmd.exe", "/c", tool, version], capture_output=True, text=True, timeout=10)
            else:
                result = subprocess.run([tool, version], capture_output=True, text=True, timeout=10)
            tool_exists = True
        except FileNotFoundError as e:
            continue

        has_digits = bool(re.search(r"[vV]?\d+(?:\.\d+)+(?:[-._\w]+)?", result.stdout))

        if has_digits:
            print(f"Found {tool} and it works perfectly.")
            sys.exit(0)

    if tool_exists:
        print(f"Tool {tool} found but it doesnt have a version.")
        sys.exit(0)
    else:
        print(f"Have not found {tool} and it doesn't work.")
        sys.exit(1)

except subprocess.TimeoutExpired as e:
    print(f"Timed out: {e}")
    sys.exit(1)
