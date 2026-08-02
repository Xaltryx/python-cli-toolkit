import platform
import subprocess
import sys

if platform.system() == "Windows":
    cmd = ["cmd", "/c", "dir"]
else:
    cmd = ["ls", "-la"]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    sys.exit(0)

except FileNotFoundError as e:
    print(f"Command not found: {e}")
    sys.exit(1)
except subprocess.TimeoutExpired as e:
    print(f"Timeout: {e}")
    sys.exit(1)