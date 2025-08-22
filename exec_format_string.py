# exec_format_string_bad.py
# WARNING: Intentionally vulnerable Python code.
# Demonstrates an exec format string injection issue.
# For testing analyzers (Semgrep, Bandit, etc.) ONLY.

def run_command():
    user_input = input("Enter a Python expression: ")
    
    # BAD: user input embedded directly in format string and executed
    code = "result = {}".format(user_input)
    exec(code, globals())  # CWE-94: Code Injection
    
    print("Execution finished. Result =", result)

if __name__ == "__main__":
    run_command()
