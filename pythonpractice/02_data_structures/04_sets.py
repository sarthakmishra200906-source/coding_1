"""
================================================================================
         PYTHON SETS - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete set theory, hashing, mathematical operations.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     set operations, methods, O(1) membership testing, and frozenset!

Command to run:
  python set.py
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
# CORE THEORY: WHAT IS A SET IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Definition:
   A set is an UNORDERED, MUTABLE collection of UNIQUE, HASHABLE elements
   enclosed in curly braces {}.

2. Core Characteristics:
   - Duplicates Forbidden: Adding duplicate items has no effect.
   - Unordered: Elements have no predictable order. Indexing (s[0]) and slicing
     are NOT supported.
   - Extremely Fast Lookups: Implemented internally via Hash Tables, offering
     O(1) average time complexity for membership testing (`item in set`).

3. The Empty Set Trap (Exam Classic):
   - `s = {}`     --> Creates an EMPTY DICTIONARY, NOT a set!
   - `s = set()`  --> Creates an EMPTY SET!

4. frozenset:
   An immutable version of a set. Once created, elements cannot be added or
   removed. Because it is immutable, a frozenset is hashable and can be used as
   a dictionary key or element of another set!
"""


# ==============================================================================
# DEMONSTRATION 1: CREATION, DUPLICATE REMOVAL & THE EMPTY SET TRAP
# ==============================================================================
def demo_creation_and_trap():
    banner("Section 1: Creation & The Empty Set Trap", "Unique Elements & Syntax Rules")

    # Eliminating duplicates automatically
    raw_nums = {1, 2, 3, 2, 4, 1, 5, 3}
    print(f"Set created from {{1, 2, 3, 2, 4, 1, 5, 3}}: {raw_nums}")

    sub_heading("The Empty Set Trap")
    dict_empty = {}
    set_empty = set()

    print(f"dict_empty = {{}}    -> Type: {type(dict_empty)} (IT IS A DICTIONARY!)")
    print(f"set_empty  = set() -> Type: {type(set_empty)}  (PROPER EMPTY SET)")


# ==============================================================================
# DEMONSTRATION 2: ADDING ELEMENTS (.add vs .update)
# ==============================================================================
def demo_adding():
    banner("Section 2: Adding Elements", ".add() for Singles, .update() for Iterables")

    tech_set = {"Python", "JavaScript"}
    print(f"Initial Set: {tech_set}")

    # .add(): Adds a single element
    tech_set.add("Go")
    print(f"After .add('Go'):                     {tech_set}")

    # .update(): Unpacks and adds elements from an iterable (list, tuple, or set)
    tech_set.update(["Rust", "Docker", "Python"])  # 'Python' duplicate ignored
    print(f"After .update(['Rust', 'Docker'...]): {tech_set}")


# ==============================================================================
# DEMONSTRATION 3: REMOVING ELEMENTS (.remove vs .discard vs .pop)
# ==============================================================================
def demo_removing():
    banner("Section 3: Removing Elements", ".remove() (Strict) vs .discard() (Safe) vs .pop()")

    colors = {"red", "green", "blue", "yellow", "orange"}
    print(f"Initial Colors: {colors}")

    # 1. .discard(): Safely removes if present; DOES NOT raise error if missing
    colors.discard("blue")
    print(f"After .discard('blue'):   {colors}")
    colors.discard("magenta")  # Not present, won't crash!
    print("Called .discard('magenta') (Missing item) -> No crash!")

    # 2. .remove(): Removes if present; RAISES KeyError if missing
    colors.remove("green")
    print(f"After .remove('green'):    {colors}")

    try:
        colors.remove("magenta")  # Will crash!
    except KeyError as err:
        print(f"Calling .remove('magenta') raised KeyError as expected: {err}")

    # 3. .pop(): Removes and returns an arbitrary element
    popped = colors.pop()
    print(f"After .pop():              {colors} (Popped arbitrary element: '{popped}')")


# ==============================================================================
# DEMONSTRATION 4: MATHEMATICAL SET OPERATIONS
# ==============================================================================
def demo_math_operations():
    banner("Section 4: Mathematical Set Operations", "Union, Intersection, Difference & Symmetric Difference")

    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}

    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")

    # 1. UNION (|): All unique elements from both sets
    union_res = set_A | set_B  # or set_A.union(set_B)
    print(f"\nUnion (A | B):               {union_res}")

    # 2. INTERSECTION (&): Elements present in BOTH sets
    intersect_res = set_A & set_B  # or set_A.intersection(set_B)
    print(f"Intersection (A & B):        {intersect_res}")

    # 3. DIFFERENCE (-): Elements in A that are NOT in B
    diff_A_B = set_A - set_B  # or set_A.difference(set_B)
    diff_B_A = set_B - set_A  # or set_B.difference(set_A)
    print(f"Difference (A - B):          {diff_A_B} (In A, but not B)")
    print(f"Difference (B - A):          {diff_B_A} (In B, but not A)")

    # 4. SYMMETRIC DIFFERENCE (^): Elements in EITHER set, but NOT in both
    sym_diff = set_A ^ set_B  # or set_A.symmetric_difference(set_B)
    print(f"Symmetric Difference (A ^ B):{sym_diff}")


# ==============================================================================
# DEMONSTRATION 5: SUBSET, SUPERSET & DISJOINT CHECKS
# ==============================================================================
def demo_relation_checks():
    banner("Section 5: Set Relationships", ".issubset(), .issuperset(), .isdisjoint()")

    small = {1, 2}
    medium = {1, 2, 3, 4}
    disjoint_set = {9, 10}

    print(f"small:        {small}")
    print(f"medium:       {medium}")
    print(f"disjoint_set: {disjoint_set}")

    print(f"\nIs 'small' a subset of 'medium'?         {small.issubset(medium)} (or small <= medium)")
    print(f"Is 'medium' a superset of 'small'?       {medium.issuperset(small)} (or medium >= small)")
    print(f"Are 'small' and 'disjoint_set' disjoint? {small.isdisjoint(disjoint_set)} (No shared elements)")


# ==============================================================================
# DEMONSTRATION 6: MEMBERSHIP SPEED (O(1) LOOKUP) & DUPLICATE STRIPPING
# ==============================================================================
def demo_practical_use_cases():
    banner("Section 6: Practical Applications", "O(1) Fast Membership & Dropping List Duplicates")

    # Fast duplicate drop
    numbers_with_dups = [10, 20, 30, 20, 40, 10, 50, 30]
    unique_numbers = list(set(numbers_with_dups))
    print(f"Original with duplicates: {numbers_with_dups}")
    print(f"Unique via list(set(...)): {unique_numbers}")

    # Fast membership testing
    admin_users = {"sarthak", "rahul", "priya", "admin"}
    test_user = "sarthak"
    if test_user in admin_users:
        print(f"Access GRANTED for '{test_user}' in O(1) time complexity!")


# ==============================================================================
# DEMONSTRATION 7: FROZENSET (IMMUTABLE SET)
# ==============================================================================
def demo_frozenset():
    banner("Section 7: Frozenset (Immutable Set)", "Hashable Sets for Dict Keys & Nested Sets")

    frozen = frozenset([1, 2, 3, 4])
    print(f"Frozenset: {frozen} -> Type: {type(frozen)}")

    try:
        frozen.add(5)
    except AttributeError as err:
        print(f"Attempting to add to frozenset raises AttributeError: {err}")

    # Frozensets CAN be used as dictionary keys!
    groups = {
        frozenset(["read", "write"]): "Editor Role",
        frozenset(["read"]): "Viewer Role"
    }
    user_perms = frozenset(["read", "write"])
    print(f"Role for permissions {user_perms}: '{groups[user_perms]}'")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                    PYTHON SETS QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Operation':<24} | {'Operator':<12} | {'Method Equivalent':<22} | {'Explanation':<16}")
    print("-" * 80)
    print(f"{'Empty Set':<24} | {'set()':<12} | {'N/A':<22} | {'{} is a dictionary!'}")
    print(f"{'Add element':<24} | {'N/A':<12} | {'.add(x)':<22} | {'Add single item'}")
    print(f"{'Add multiple':<24} | {'N/A':<12} | {'.update(iterable)':<22} | {'Unpack & add items'}")
    print(f"{'Remove (strict)':<24} | {'N/A':<12} | {'.remove(x)':<22} | {'Raises KeyError'}")
    print(f"{'Remove (safe)':<24} | {'N/A':<12} | {'.discard(x)':<22} | {'No error if missing'}")
    print(f"{'Union':<24} | {'A | B':<12} | {'A.union(B)':<22} | {'All unique items'}")
    print(f"{'Intersection':<24} | {'A & B':<12} | {'A.intersection(B)':<22} | {'Common items'}")
    print(f"{'Difference':<24} | {'A - B':<12} | {'A.difference(B)':<22} | {'In A, not in B'}")
    print(f"{'Symmetric Diff':<24} | {'A ^ B':<12} | {'A.symmetric_diff(B)':<22} | {'In either, not both'}")
    print(f"{'Subset Check':<24} | {'A <= B':<12} | {'A.issubset(B)':<22} | {'True if all in B'}")
    print("=" * 80)
    print("Set Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON SETS MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_creation_and_trap()
    demo_adding()
    demo_removing()
    demo_math_operations()
    demo_relation_checks()
    demo_practical_use_cases()
    demo_frozenset()
    print_cheat_sheet()