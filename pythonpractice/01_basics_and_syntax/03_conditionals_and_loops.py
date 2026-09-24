"""
================================================================================
   MODULE 01: CONDITIONALS & LOOPS IN PYTHON
================================================================================
This script covers:
  1. if, elif, else & Ternary conditional operator
  2. while loops & for loops (range function)
  3. Loop control: break, continue, pass
  4. The unique loop-else construct
  5. Practical number algorithms (Prime check, Armstrong number, Palindrome)
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


def main():
    banner("1. Conditional Branching & Ternary Operator")
    score = 88
    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 50:
        grade = "B"
    else:
        grade = "F"
    print(f"Score {score} -> Grade: {grade}")

    # Ternary shorthand: result = value_if_true if condition else value_if_false
    status = "Passed" if score >= 40 else "Failed"
    print(f"Ternary check: {status}")

    banner("2. Loops & Loop Control (break, continue, pass)")
    print("Printing 1 to 10, skipping multiples of 3, stopping before 9:")
    for num in range(1, 11):
        if num == 9:
            print("[Break at 9!]")
            break
        if num % 3 == 0:
            continue  # Skip 3 and 6
        print(num, end=" ")
    print()

    banner("3. Python's Unique for...else Construct")
    # else executes ONLY IF the loop finishes WITHOUT hitting a break
    test_number = 29
    for i in range(2, int(test_number ** 0.5) + 1):
        if test_number % i == 0:
            print(f"{test_number} is NOT prime.")
            break
    else:
        print(f"{test_number} is PRIME! (for-loop completed without breaking)")

    banner("4. Classic Number Algorithms")
    # Armstrong number check: e.g. 153 = 1^3 + 5^3 + 3^3
    arm_num = 153
    digits = [int(d) for d in str(arm_num)]
    arm_sum = sum(d ** len(digits) for d in digits)
    is_armstrong = (arm_sum == arm_num)
    print(f"Is {arm_num} an Armstrong number? {is_armstrong} (Sum of powers: {arm_sum})")

    # Palindrome number check
    pal_num = 12321
    is_palindrome = str(pal_num) == str(pal_num)[::-1]
    print(f"Is {pal_num} a Palindrome? {is_palindrome}")


if __name__ == "__main__":
    main()
