"""
================================================================================
   MODULE 03: RECURSION & MATHEMATICAL ALGORITHMS IN PYTHON
================================================================================
This script covers:
  1. Recursion concepts (base case vs recursive step, call stack)
  2. Factorial calculation
  3. Fibonacci series generation
  4. Greatest Common Divisor (GCD / Euclidean algorithm)
  5. Sum of digits & Strong Number checks
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


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a: int, b: int) -> int:
    # Euclidean Algorithm
    while b != 0:
        a, b = b, a % b
    return a


def is_strong_number(num: int) -> bool:
    # Sum of factorials of digits equals the original number (e.g. 145 = 1! + 4! + 5!)
    digit_fact_sum = sum(factorial(int(d)) for d in str(num))
    return digit_fact_sum == num


def main():
    banner("1. Recursion: Factorial & Call Stack")
    print(f"5! (Factorial): {factorial(5)}")
    print(f"7! (Factorial): {factorial(7)}")

    banner("2. Fibonacci Series")
    fib_series = [fibonacci(i) for i in range(10)]
    print(f"First 10 Fibonacci numbers: {fib_series}")

    banner("3. Euclidean GCD Algorithm")
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"GCD(100, 35): {gcd(100, 35)}")

    banner("4. Strong Number Verification")
    test_num = 145
    print(f"Is {test_num} a Strong Number? {is_strong_number(test_num)} (1! + 4! + 5! = 1 + 24 + 120 = 145)")


if __name__ == "__main__":
    main()
