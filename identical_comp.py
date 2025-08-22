# identical_is_comparison.py
# This script intentionally demonstrates the "is" comparison issue.
# It is for educational/testing purposes with static analysis tools (e.g., Semgrep).

def check_number(x):
    # BAD: using `is` for value comparison
    if x is 5:  # This may work sometimes due to small integer caching, but is unreliable
        print("x is 5 (using 'is')")
    else:
        print("x is not 5 (using 'is')")

    # GOOD: using equality comparison
    if x == 5:
        print("x equals 5 (using '==')")
    else:
        print("x does not equal 5 (using '==')")

if __name__ == "__main__":
    for val in [5, int("5")]:
        print(f"Testing value: {val}")
        check_number(val)
        print("----")
