import sys
import subprocess
import platform
import time
from pathlib import Path
import json
import shlex

if len(sys.argv) != 2:
    print("Usage: python command_batch_runner.py <txt>")
    sys.exit(1)

txt = Path(sys.argv[1]).resolve()
commands = []

try:
    with open(txt, "r") as f:
        for command in f:
            commands.append(command.strip())

        if len(commands) == 0:
            print("No commands found")
            sys.exit(1)

    dicts = {
        'summary':
            {
                'total':0,
                "success":0,
                "failure":0,
                'timeout':0
            },
        'results':[],
    }
    for command in commands:
        dicts['summary']['total'] += 1
        result_dict = {"command": command}
        command_list = shlex.split(command)

        if platform.system() == "Windows":
            full_command = ["cmd.exe", "/c"] + command_list
        else:
            full_command = command_list

        start_time = time.perf_counter()
        try:
            result = subprocess.run(
                full_command, capture_output=True, text=True, timeout=10
            )
            end_time = time.perf_counter()
            if result.returncode == 0:
                dicts['summary']['success'] += 1
                result_dict['status'] = "success"
                result_dict['error'] = result.stderr
            else:
                dicts['summary']['failure'] += 1
                result_dict['status'] = "failure"
                result_dict['error'] = result.stderr or "Command exited with code 1, no error output produced."

            result_dict['output'] = result.stdout
            result_dict['duration_seconds'] = round(end_time - start_time, 2)

        except FileNotFoundError as e:
            end_time = time.perf_counter()
            dicts['summary']['failure'] += 1
            result_dict['status'] = "failure"
            result_dict['output'] = ""
            result_dict['error'] = f"Executable not found: {e}"
            result_dict['duration_seconds'] = round(end_time - start_time, 2)

        except subprocess.TimeoutExpired as e:
            end_time = time.perf_counter()
            dicts['summary']['timeout'] += 1
            result_dict['status'] = "timeout"
            result_dict['output'] = e.stdout or ""
            result_dict['error'] = e.stderr or "Command timed out after 10 seconds."
            result_dict['duration_seconds'] = round(end_time - start_time, 2)

        dicts['results'].append(result_dict)

    with open(f"{txt.stem}_stats.json", "w") as f:
        json.dump(dicts, f, indent=2)
        print("Finished Writing Stats.")
        sys.exit(0)

except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(1)
except json.decoder.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    sys.exit(1)
except PermissionError as e:
    print(f"Permission error: {e}")
    sys.exit(1)