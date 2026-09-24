"""
================================================================================
   MODULE 01: OPERATORS & EXPRESSIONS IN PYTHON
================================================================================
This script covers:
  1. Arithmetic & Floor Division vs True Division
  2. Comparison & Logical Operators (short-circuiting)
  3. Identity (`is`, `is not`) vs Equality (`==`, `!=`)
  4. Membership (`in`, `not in`)
  5. Bitwise Operators
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
    banner("1. Arithmetic Operators")
    a = 15
    b = 4
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b):          {a + b}")
    print(f"Subtraction (a - b):       {a - b}")
    print(f"Multiplication (a * b):    {a * b}")
    print(f"True Division (a / b):     {a / b} (Always returns float)")
    print(f"Floor Division (a // b):   {a // b} (Discards fractional part)")
    print(f"Modulo / Remainder (a % b):{a % b}")
    print(f"Exponentiation (a ** b):   {a ** b} (15 to the power 4)")

    banner("2. Identity (is) vs Equality (==)")
    list1 = [10, 20, 30]
    list2 = [10, 20, 30]
    list3 = list1

    print(f"list1: {list1} -> Memory ID: {hex(id(list1))}")
    print(f"list2: {list2} -> Memory ID: {hex(id(list2))}")
    print(f"list3: {list3} -> Memory ID: {hex(id(list3))}")

    print(f"list1 == list2: {list1 == list2}  (Checks VALUES - they match!)")
    print(f"list1 is list2: {list1 is list2} (Checks MEMORY POINTER - different objects!)")
    print(f"list1 is list3: {list1 is list3}  (True - both reference the exact same memory!)")

    banner("3. Membership Operators (in, not in)")
    frameworks = ["Django", "FastAPI", "Flask"]
    print(f"Frameworks: {frameworks}")
    print(f"'FastAPI' in frameworks:     {'FastAPI' in frameworks}")
    print(f"'Spring' not in frameworks:  {'Spring' not in frameworks}")

    banner("4. Bitwise Operators (Binary level)")
    x = 5  # 0b0101
    y = 3  # 0b0011
    print(f"x = {x} (bin: {bin(x)}), y = {y} (bin: {bin(y)})")
    print(f"x & y (AND): {x & y} (bin: {bin(x & y)})")
    print(f"x | y (OR):  {x | y} (bin: {bin(x | y)})")
    print(f"x ^ y (XOR): {x ^ y} (bin: {bin(x ^ y)})")
    print(f"~x    (NOT): {~x}")
    print(f"x << 1 (Shift Left):  {x << 1}")
    print(f"x >> 1 (Shift Right): {x >> 1}")


if __name__ == "__main__":
    main()
