# WARNING: This script is intentionally VULNERABLE. 
# It is provided solely for testing security scanners (e.g., Semgrep) and education.
# Do NOT use in production or expose to untrusted input.

def vulnerable_calculator():
    # User input is evaluated directly -> EVAL INJECTION
    expr = input("Enter a Python expression to evaluate: ")
    result = eval(expr)  # CWE-94 / CWE-95: Use of eval with untrusted input
    print("Result:", result)

if __name__ == "__main__":
    vulnerable_calculator()
