"""
================================================================================
        PYTHON TUPLES - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete definitions, immutability, memory advantages.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     tuple packing, unpacking, error handling, and method usage!

Command to run:
  python tupple.py
================================================================================
"""

import sys

# Ensure UTF-8 output across all consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# SECTION HELPERS
# ==============================================================================
def banner(title: str, subtitle: str):
    print("\n" + "=" * 80)
    print(f"  {title.upper()}")
    print(f"  >> {subtitle}")
    print("=" * 80)


def sub_heading(text: str):
    print(f"\n--- [ {text} ] ---")


# ==============================================================================
# CORE THEORY: WHAT IS A TUPLE IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Definition:
   A tuple is an ORDERED, IMMUTABLE collection of elements enclosed in
   parentheses ().

2. Why use Tuples instead of Lists?
   - Data Protection: Elements cannot be accidentally modified, deleted, or inserted.
   - Performance: Tuples are allocated in a single memory block, making them
     faster to create and iterate over compared to lists.
   - Dictionary Keys: Because tuples are immutable (hashable), they can serve as
     dictionary keys and set elements; lists CANNOT.

3. The Single-Element Trap (Frequent Exam Trick):
   - `x = (5)`   --> Python treats this as an integer (5) with math parentheses!
   - `x = (5,)`  --> Trailing comma defines it as a TUPLE!

4. Tuple Packing & Unpacking:
   Grouping multiple values into one tuple is "packing".
   Extracting elements back into distinct variables is "unpacking".
"""


# ==============================================================================
# DEMONSTRATION 1: CREATION & THE SINGLE-ELEMENT GOTCHA
# ==============================================================================
def demo_creation_and_gotcha():
    banner("Section 1: Tuple Creation & Trailing Comma Rule", "Understanding Tuple Syntax")

    t1 = (10, 20, 30)
    t_empty = ()
    not_a_tuple = (50)    # Without comma
    real_tuple = (50,)    # With comma

    print(f"Standard Tuple (10, 20, 30): {t1} -> Type: {type(t1)}")
    print(f"Empty Tuple ():              {t_empty} -> Type: {type(t_empty)}")
    print(f"Trap: (50) without comma:    {not_a_tuple} -> Type: {type(not_a_tuple)} (NOT a tuple!)")
    print(f"Fix:  (50,) with comma:      {real_tuple} -> Type: {type(real_tuple)} (Proper 1-item tuple)")


# ==============================================================================
# DEMONSTRATION 2: IMMUTABILITY IN ACTION
# ==============================================================================
def demo_immutability():
    banner("Section 2: Immutability Verification", "Attempting Item Assignment")

    coordinates = (19.0760, 72.8777)
    print(f"Geographic coordinates: {coordinates}")
    print(f"Latitude  coordinates[0]: {coordinates[0]}")
    print(f"Longitude coordinates[1]: {coordinates[1]}")

    sub_heading("Attempting to modify a tuple element")
    try:
        coordinates[0] = 28.7041  # Raises TypeError!
    except TypeError as err:
        print("FAILED as expected!")
        print(f"Caught Error: {err}")
        print(">> Reason: Tuples are immutable; once created, item assignment is forbidden.")


# ==============================================================================
# DEMONSTRATION 3: THE 'MUTABLE OBJECT INSIDE TUPLE' EXCEPTION
# ==============================================================================
def demo_nested_mutability():
    banner("Section 3: Mutable Objects Inside Tuples", "A List Inside a Tuple Can Still Mutate!")

    # The tuple itself is immutable (holds references), but referenced objects may be mutable!
    hybrid = ("Sarthak", [90, 85, 95])
    print(f"Original Tuple: {hybrid}")

    sub_heading("Modifying the internal list")
    print("Modifying internal list via hybrid[1].append(100)...")
    hybrid[1].append(100)
    print(f"After append:   {hybrid}")
    print(">> Note: The tuple reference didn't change, but the mutable list inside was updated!")


# ==============================================================================
# DEMONSTRATION 4: TUPLE PACKING & UNPACKING
# ==============================================================================
def demo_packing_unpacking():
    banner("Section 4: Tuple Packing & Unpacking", "Destructuring, Swapping & Extended Unpacking (*)")

    # Packing
    student_record = "Sarthak", 101, "Computer Science", 9.4  # Parentheses are optional!
    print(f"Packed Record: {student_record} -> Type: {type(student_record)}")

    # Unpacking
    name, roll, dept, cgpa = student_record
    print(f"Unpacked -> Name: {name}, Roll: {roll}, Dept: {dept}, CGPA: {cgpa}")

    sub_heading("Variable Swap Without Temp Variable (Uses Tuple Unpacking)")
    a = 10
    b = 20
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a  # Behind the scenes, creates tuple (b, a) then unpacks into a, b
    print(f"After Swap:  a = {a}, b = {b}")

    sub_heading("Extended Unpacking with Asterisk (*)")
    scores = (98, 85, 76, 92, 88, 79)
    first, *middle, last = scores
    print(f"Scores Tuple: {scores}")
    print(f"First:  {first}")
    print(f"Middle: {middle} (Captured as a list)")
    print(f"Last:   {last}")


# ==============================================================================
# DEMONSTRATION 5: TUPLE METHODS (.count & .index)
# ==============================================================================
def demo_tuple_methods():
    banner("Section 5: Built-in Tuple Methods", "Only Two Methods: .count() and .index()")

    data = (10, 20, 30, 20, 40, 20, 50)
    print(f"Tuple Data: {data}")

    # 1. .count(x): Returns number of occurrences
    count_20 = data.count(20)
    print(f"data.count(20): {count_20} occurrence(s)")

    # 2. .index(x): Returns index of first occurrence
    idx_40 = data.index(40)
    print(f"data.index(40): Found at index {idx_40}")

    try:
        data.index(999)
    except ValueError as err:
        print(f"data.index(999) raises ValueError: '{err}'")


# ==============================================================================
# DEMONSTRATION 6: FUNCTIONS RETURNING MULTIPLE VALUES
# ==============================================================================
def demo_function_returns():
    banner("Section 6: Functions Returning Multiple Values", "Python Secretly Uses Tuples")

    def calculate_stats(numbers):
        total = sum(numbers)
        avg = total / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        return total, avg, minimum, maximum  # Returns a tuple!

    nums = [10, 20, 30, 40, 50]
    result = calculate_stats(nums)
    print(f"Function return value: {result} -> Type: {type(result)}")

    t_sum, t_avg, t_min, t_max = result
    print(f"Unpacked: Sum={t_sum}, Avg={t_avg}, Min={t_min}, Max={t_max}")


# ==============================================================================
# DEMONSTRATION 7: TUPLES AS DICTIONARY KEYS
# ==============================================================================
def demo_tuple_dict_keys():
    banner("Section 7: Tuples as Dictionary Keys", "Why Immutability Matters")

    # A 2D grid where coordinate pairs (x, y) map to city names
    cities = {
        (28.6139, 77.2090): "New Delhi",
        (19.0760, 72.8777): "Mumbai",
        (12.9716, 77.5946): "Bengaluru"
    }

    print("Dictionary with Tuple Keys:")
    for coords, city in cities.items():
        print(f"  Coordinates {coords} --> {city}")

    print("\nAttempting to use a List [1, 2] as a dict key:")
    try:
        invalid_dict = {[1, 2]: "Invalid"}
    except TypeError as err:
        print(f"FAILED as expected! Caught: {err}")
        print(">> Why? Lists are unhashable because they are mutable. Tuples are hashable!")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                    PYTHON TUPLES QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Feature / Syntax':<24} | {'Tuple Rule':<30} | {'Contrast With List':<22}")
    print("-" * 80)
    print(f"{'Syntax':<24} | {'(1, 2, 3) or 1, 2, 3':<30} | {'[1, 2, 3]':<22}")
    print(f"{'Single Item':<24} | {'(5,) (Comma mandatory!)':<30} | {'[5]':<22}")
    print(f"{'Mutability':<24} | {'Immutable (Read-only)':<30} | {'Mutable (In-place edit)':<22}")
    print(f"{'Memory & Speed':<24} | {'Faster, less memory':<30} | {'Slower, dynamic overhead':<22}")
    print(f"{'Dict Keys / Sets':<24} | {'Allowed (Hashable)':<30} | {'Forbidden (Unhashable)':<22}")
    print(f"{'.count(x)':<24} | {'Count occurrences':<30} | {'Same in both':<22}")
    print(f"{'.index(x)':<24} | {'First index of x':<30} | {'Same in both':<22}")
    print(f"{'Packing/Unpacking':<24} | {'a, b = (10, 20)':<30} | {'Also supported':<22}")
    print("=" * 80)
    print("Tuple Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON TUPLES MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_creation_and_gotcha()
    demo_immutability()
    demo_nested_mutability()
    demo_packing_unpacking()
    demo_tuple_methods()
    demo_function_returns()
    demo_tuple_dict_keys()
    print_cheat_sheet()