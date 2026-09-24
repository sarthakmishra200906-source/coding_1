"""
================================================================================
   MODULE 03: LAMBDA FUNCTIONS, MAP, FILTER & SORTING KEYS
================================================================================
This script covers:
  1. Anonymous functions (lambda arguments: expression)
  2. The map() higher-order function
  3. The filter() higher-order function
  4. functools.reduce() for cumulative aggregation
  5. Sorting complex objects using custom lambda keys
================================================================================
"""

import sys
from functools import reduce

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
    banner("1. Lambda Expressions (Anonymous One-Liners)")
    square = lambda x: x ** 2
    add = lambda a, b: a + b
    print(f"square(7): {square(7)}")
    print(f"add(12, 18): {add(12, 18)}")

    banner("2. map() Function (Transforming Iterables)")
    temperatures_celsius = [0, 20, 35, 100]
    # Formula: F = C * 9/5 + 32
    temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))
    print(f"Celsius:    {temperatures_celsius}")
    print(f"Fahrenheit: {temperatures_fahrenheit}")

    banner("3. filter() Function (Extracting Matches)")
    scores = [45, 88, 32, 95, 60, 21, 74]
    passing_scores = list(filter(lambda s: s >= 50, scores))
    print(f"All Scores:     {scores}")
    print(f"Passing Scores: {passing_scores}")

    banner("4. functools.reduce() (Cumulative Aggregation)")
    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, nums)
    print(f"Product of {nums}: {product} (1 * 2 * 3 * 4 * 5 = 120)")

    banner("5. Custom Sorting Keys with Lambda")
    students = [
        {"name": "Sarthak", "cgpa": 9.4, "age": 20},
        {"name": "Aarav", "cgpa": 8.7, "age": 21},
        {"name": "Priya", "cgpa": 9.8, "age": 19}
    ]

    # Sort descending by CGPA
    sorted_by_cgpa = sorted(students, key=lambda s: s["cgpa"], reverse=True)
    print("Students sorted by CGPA (Highest first):")
    for s in sorted_by_cgpa:
        print(f"  {s['name']:<10} | CGPA: {s['cgpa']}")


if __name__ == "__main__":
    main()
