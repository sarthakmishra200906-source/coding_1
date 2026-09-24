"""
================================================================================
   MODULE 07: COMPREHENSIONS (LIST, SET, DICT & GENERATOR EXPRESSIONS)
================================================================================
This script covers:
  1. List comprehensions with conditionals
  2. Set comprehensions (automatic deduplication)
  3. Dictionary comprehensions (key: value mapping)
  4. Generator expressions (memory-efficient lazy evaluation with ())
  5. Nested comprehensions (flattening matrices)
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
    banner("1. List Comprehension: [expr for item in iterable if cond]")
    # Squares of even numbers
    evens_squared = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Squares of evens (1..10): {evens_squared}")

    banner("2. Set Comprehension: {expr for item in iterable if cond}")
    words = ["apple", "banana", "apple", "cherry", "banana"]
    unique_lengths = {len(w) for w in words}
    print(f"Words: {words}")
    print(f"Unique word lengths: {unique_lengths}")

    banner("3. Dictionary Comprehension: {key: value for item in iterable}")
    students = [("Sarthak", 95), ("Rahul", 72), ("Priya", 88)]
    student_dict = {name: score for name, score in students}
    print(f"Student Score Mapping: {student_dict}")

    banner("4. Generator Expression vs List Comprehension")
    # List comprehension creates entire list in memory
    list_comp = [x * 2 for x in range(5)]
    # Generator expression creates lazy iterator in parentheses
    gen_exp = (x * 2 for x in range(5))

    print(f"List comp: {list_comp} (Size in RAM: {sys.getsizeof(list_comp)} bytes)")
    print(f"Gen exp:   {gen_exp} (Size in RAM: {sys.getsizeof(gen_exp)} bytes)")
    print(f"Unpacking Gen exp: {list(gen_exp)}")

    banner("5. Nested Comprehension (Flattening a 2D Matrix)")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [val for row in matrix for val in row]
    print(f"Original 2D Matrix: {matrix}")
    print(f"Flattened 1D List:  {flattened}")


if __name__ == "__main__":
    main()
