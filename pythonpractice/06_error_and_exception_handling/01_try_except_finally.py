"""
================================================================================
   MODULE 06: EXCEPTION HANDLING (TRY, EXCEPT, ELSE, FINALLY)
================================================================================
This script covers:
  1. Catching specific built-in exceptions (ZeroDivisionError, ValueError, TypeError)
  2. The role of the else block (runs only if NO errors occur)
  3. The role of the finally block (guaranteed execution for cleanup)
  4. Inspecting exception arguments (.args)
================================================================================
"""

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(title: str):
    print("\n" + "=" * 75)
    print(f"  {title.upper()}")
    print("=" * 75)


def safe_calculator(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "/":
            return a / b
        elif operation == "int_cast":
            return int(a)
    except ZeroDivisionError as err:
        print(f"  [ZeroDivisionError caught]: Cannot divide by zero! ({err})")
    except TypeError as err:
        print(f"  [TypeError caught]: Incompatible operand types! ({err})")
    except ValueError as err:
        print(f"  [ValueError caught]: Invalid literal for conversion! ({err})")
    else:
        print("  [Else block]: Operation completed cleanly!")
    finally:
        print("  [Finally block]: Cleanup hook executed.")
    return None


def main():
    banner("1. Successful Execution (Try -> Else -> Finally)")
    res1 = safe_calculator(10, 2, "/")
    print(f"Result: {res1}\n")

    banner("2. Division by Zero (Try -> Except ZeroDivisionError -> Finally)")
    res2 = safe_calculator(10, 0, "/")
    print(f"Result: {res2}\n")

    banner("3. Type Error (Try -> Except TypeError -> Finally)")
    res3 = safe_calculator("10", 5, "+")
    print(f"Result: {res3}\n")

    banner("4. Value Error (Try -> Except ValueError -> Finally)")
    res4 = safe_calculator("NotANumber", None, "int_cast")
    print(f"Result: {res4}\n")


if __name__ == "__main__":
    main()
