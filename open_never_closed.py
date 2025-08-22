# WARNING: This script intentionally leaks file handles by not closing files.
# It is provided ONLY for testing static analyzers (e.g., Semgrep) and education.

import os
from datetime import datetime

LOG_PATH = "leaky.log"
CONFIG_PATH = "leaky.cfg"

def func1():
    # ruleid:open-never-closed
    fd = open('foo')
    x = 123

def write_log_bad(message: str):
    # BAD: open() without close()
    f = open(LOG_PATH, "a")  # noqa: SIM115  # some linters flag "open without with"
    timestamp = datetime.utcnow().isoformat()
    f.write(f"[{timestamp}] {message}\n")
    # forgot: f.close()

def read_config_bad() -> str:
    # BAD: an exception path means the file never gets closed
    f = open(CONFIG_PATH, "r")  # noqa: SIM115
    data = f.read()
    # Simulate an error before close
    if "boom" in data:
        raise ValueError("config triggered an error; file never closed!")
    # also forgot: f.close()
    return data

def write_many_bad(n: int):
    # BAD: repeatedly opening without closing in a loop
    for i in range(n):
        fh = open(LOG_PATH, "a")  # noqa: SIM115
        fh.write(f"line {i}\n")
        # no fh.close()

def main():
    # Prepare a tiny config to read
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w") as c:
            c.write("key=value\n")
    write_log_bad("starting up")
    try:
        print("Config contents:", read_config_bad())
    except Exception as e:
        print("Encountered error while reading config:", e)
    write_many_bad(3)
    print("Done. (But several files were not closed.)")

if __name__ == "__main__":
    main()
