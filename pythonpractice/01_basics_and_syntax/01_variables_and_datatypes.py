"""
================================================================================
   MODULE 01: VARIABLES & DATA TYPES IN PYTHON
================================================================================
This script covers:
  1. Primitive types (int, float, complex, bool, str, None)
  2. Type casting & dynamic typing
  3. Memory IDs, mutability overview
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
    banner("1. Python Primitive Data Types")
    integer_val = 100
    float_val = 3.14159
    complex_val = 2 + 3j
    boolean_val = True
    string_val = "Hello Python"
    none_val = None

    print(f"integer_val: {integer_val:<12} | Type: {type(integer_val).__name__}")
    print(f"float_val:   {float_val:<12} | Type: {type(float_val).__name__}")
    print(f"complex_val: {str(complex_val):<12} | Type: {type(complex_val).__name__} (Real: {complex_val.real}, Imag: {complex_val.imag})")
    print(f"boolean_val: {str(boolean_val):<12} | Type: {type(boolean_val).__name__} (int value: {int(boolean_val)})")
    print(f"string_val:  {string_val:<12} | Type: {type(string_val).__name__}")
    print(f"none_val:    {str(none_val):<12} | Type: {type(none_val).__name__}")

    banner("2. Type Conversion (Type Casting)")
    raw_input = "250"
    as_int = int(raw_input)
    as_float = float(as_int)
    as_str = str(as_float)

    print(f"Original String: '{raw_input}'")
    print(f"Cast to int:     {as_int}  (Type: {type(as_int).__name__})")
    print(f"Cast to float:   {as_float} (Type: {type(as_float).__name__})")
    print(f"Back to string:  '{as_str}' (Type: {type(as_str).__name__})")

    banner("3. Python Variable Assignment & Reassignment")
    x = 10
    print(f"x = 10         -> Value: {x}, Memory ID: {hex(id(x))}")
    x = "Now a string!"
    print(f"x = 'string'   -> Value: '{x}', Memory ID: {hex(id(x))}")
    print(">> Python is dynamically typed: variable types can change at runtime.")


if __name__ == "__main__":
    main()
