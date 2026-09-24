"""
================================================================================
     PYTHON DICTIONARIES - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete dictionary theory, hash tables, views & merging.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     access patterns, safety checks, frequency counters, and comprehensions!

Command to run:
  python dictonary.py
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
# CORE THEORY: WHAT IS A DICTIONARY IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Definition:
   A dictionary is a MUTABLE, ORDERED (since Python 3.7) collection of KEY-VALUE
   pairs enclosed in curly braces {key: value}.

2. The Rules of Keys:
   - Unique: Duplicate keys are not allowed. If a key is repeated, the last value
     overwrites earlier values.
   - Immutable / Hashable: Keys must be immutable types (strings, numbers, tuples).
     Mutable types like lists and sets CANNOT be used as keys.

3. Safe vs Unsafe Access:
   - `dict[key]`: Unsafe if key might be absent. Raises `KeyError`.
   - `dict.get(key, default)`: Safe! Returns None (or custom fallback) if key missing.

4. Performance:
   Lookups, inserts, and deletes have average O(1) time complexity due to internal
   hash table indexing!
"""


# ==============================================================================
# DEMONSTRATION 1: CREATION, ACCESS & SAFE RETRIEVAL (.get)
# ==============================================================================
def demo_creation_and_access():
    banner("Section 1: Creation & Safe Retrieval", "Direct Lookup vs .get(key, fallback)")

    student = {
        "name": "Sarthak",
        "roll_no": 101,
        "branch": "Computer Science",
        "cgpa": 9.4
    }
    print(f"Student Record: {student}")

    sub_heading("Accessing Existing Keys")
    print(f"Direct access student['name']:      {student['name']}")
    print(f"Safe access student.get('branch'):   {student.get('branch')}")

    sub_heading("Accessing Missing Keys (Unsafe vs Safe)")
    try:
        print(student["scholarship"])  # Missing key!
    except KeyError as err:
        print(f"Direct access student['scholarship'] raised KeyError: {err}")

    # Safe retrieval with fallback default
    safe_val = student.get("scholarship", "Not Eligible / Not Recorded")
    print(f"Safe access student.get('scholarship', default): '{safe_val}'")


# ==============================================================================
# DEMONSTRATION 2: MODIFYING, ADDING & UPDATING
# ==============================================================================
def demo_mutation():
    banner("Section 2: Modifying & Adding Elements", "Direct Assignment & .setdefault()")

    config = {"theme": "dark", "font_size": 14}
    print(f"Initial Config: {config}")

    # Updating existing key
    config["font_size"] = 16
    # Adding a brand new key
    config["line_numbers"] = True
    print(f"After updates:  {config}")

    # .setdefault(key, default): Returns value if key exists, inserts default if not!
    val1 = config.setdefault("theme", "light")      # Already exists -> returns "dark"
    val2 = config.setdefault("autosave", "enabled") # Doesn't exist -> inserts "enabled"
    print(f"Config after setdefault: {config}")
    print(f"  val1: {val1} (kept original)")
    print(f"  val2: {val2} (newly inserted)")


# ==============================================================================
# DEMONSTRATION 3: REMOVING ELEMENTS (.pop, del, .popitem, .clear)
# ==============================================================================
def demo_deleting():
    banner("Section 3: Removing Elements", ".pop() vs del vs .popitem()")

    inventory = {"apples": 50, "bananas": 30, "oranges": 20, "grapes": 15}
    print(f"Inventory: {inventory}")

    # 1. .pop(key): Removes key and returns its value
    removed_bananas = inventory.pop("bananas")
    print(f"After .pop('bananas'): {inventory} (Returned: {removed_bananas})")

    # 2. del keyword: Deletes without returning value
    del inventory["apples"]
    print(f"After del inventory['apples']: {inventory}")

    # 3. .popitem(): Removes and returns the LAST inserted key-value pair as a tuple
    last_item = inventory.popitem()
    print(f"After .popitem(): {inventory} (Popped pair: {last_item})")


# ==============================================================================
# DEMONSTRATION 4: DICTIONARY VIEWS (.keys, .values, .items)
# ==============================================================================
def demo_views_and_looping():
    banner("Section 4: Views & Iteration Patterns", ".keys(), .values() & .items()")

    laptop = {"brand": "Dell", "cpu": "i7", "ram_gb": 16, "ssd_gb": 512}

    print("Keys view:  ", list(laptop.keys()))
    print("Values view:", list(laptop.values()))
    print("Items view: ", list(laptop.items()))

    sub_heading("Unpacking in a for-loop")
    for key, value in laptop.items():
        print(f"  {key:<10} --> {value}")


# ==============================================================================
# DEMONSTRATION 5: MERGING DICTIONARIES (.update vs | operator)
# ==============================================================================
def demo_merging():
    banner("Section 5: Merging Dictionaries", ".update() vs Modern Union Operator (|)")

    defaults = {"theme": "light", "notifications": True, "volume": 50}
    user_prefs = {"theme": "dark", "volume": 80, "language": "Hindi"}

    print(f"Defaults:    {defaults}")
    print(f"User Prefs:  {user_prefs}")

    # Python 3.9+ Union operator (|) creates a brand new merged dict
    merged = defaults | user_prefs
    print(f"Merged (|):  {merged}  (Notice user_prefs values took precedence!)")

    # In-place update via .update()
    copy_defaults = defaults.copy()
    copy_defaults.update(user_prefs)
    print(f"Via .update:{copy_defaults}")


# ==============================================================================
# DEMONSTRATION 6: FREQUENCY COUNTER ALGORITHMS (EXAM FAVORITE)
# ==============================================================================
def demo_frequency_counter():
    banner("Section 6: Frequency Counter Algorithm", "Counting Occurrences with .get(key, 0)")

    sample_text = "mississippi"
    print(f"Input string: '{sample_text}'")

    char_counts = {}
    for ch in sample_text:
        # If ch not in dict, get returns 0; then add 1
        char_counts[ch] = char_counts.get(ch, 0) + 1

    print("Character Frequencies:")
    for ch, count in sorted(char_counts.items()):
        print(f"  '{ch}': appears {count} times")

    # Word Frequency in a sentence
    sentence = "to be or not to be that is the question"
    word_counts = {}
    for word in sentence.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    print(f"\nWord Frequencies in '{sentence}':")
    print(f"  {word_counts}")


# ==============================================================================
# DEMONSTRATION 7: DICTIONARY COMPREHENSIONS
# ==============================================================================
def demo_comprehensions():
    banner("Section 7: Dictionary Comprehension", "{key: value for x in iterable if cond}")

    # 1. Number to its square mapping
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Squares (1..5): {squares}")

    # 2. Filtered dictionary (only passing grades)
    raw_scores = {"Aarav": 88, "Neha": 34, "Rohan": 92, "Simran": 39, "Karan": 75}
    passed_students = {name: score for name, score in raw_scores.items() if score >= 40}
    print(f"All Scores:    {raw_scores}")
    print(f"Passed Only:   {passed_students}")

    # 3. Inverting a dictionary (swap keys and values)
    codes = {"IN": "India", "US": "United States", "UK": "United Kingdom"}
    inverted = {country: code for code, country in codes.items()}
    print(f"Inverted dict: {inverted}")


# ==============================================================================
# DEMONSTRATION 8: NESTED DICTIONARIES
# ==============================================================================
def demo_nested_dicts():
    banner("Section 8: Nested Dictionaries", "Multi-Level Data Modeling")

    company = {
        "emp1": {"name": "Sarthak", "role": "Lead Architect", "skills": ["Python", "Cloud"]},
        "emp2": {"name": "Priya", "role": "Data Scientist", "skills": ["Python", "TensorFlow"]}
    }

    print(f"Company DB: {company}")
    print(f"emp1 role:  {company['emp1']['role']}")
    print(f"emp2 skill: {company['emp2']['skills'][0]}")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                 PYTHON DICTIONARIES QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Operation / Method':<24} | {'Description':<32} | {'Time Complexity':<18}")
    print("-" * 80)
    print(f"{'d[key]':<24} | {'Direct lookup (KeyError if missing)':<32} | {'O(1)':<18}")
    print(f"{'.get(key, default)':<24} | {'Safe lookup (Returns default)':<32} | {'O(1)':<18}")
    print(f"{'d[key] = value':<24} | {'Insert or update key-value':<32} | {'O(1)':<18}")
    print(f"{'.pop(key)':<24} | {'Remove key & return value':<32} | {'O(1)':<18}")
    print(f"{'del d[key]':<24} | {'Delete key without return':<32} | {'O(1)':<18}")
    print(f"{'.popitem()':<24} | {'Remove last inserted (k, v) pair':<32} | {'O(1)':<18}")
    print(f"{'.keys() / .values()':<24} | {'Return dynamic view of keys/values':<32} | {'O(1)':<18}")
    print(f"{'.items()':<24} | {'Return view of (key, value) pairs':<32} | {'O(1)':<18}")
    print(f"{'d1 | d2':<24} | {'Merge dicts (Python 3.9+)':<32} | {'O(N + M)':<18}")
    print(f"{'.update(d2)':<24} | {'In-place merge of d2 into d1':<32} | {'O(M)':<18}")
    print(f"{'.setdefault(k, v)':<24} | {'Get value or insert default if not':<32} | {'O(1)':<18}")
    print("=" * 80)
    print("Dictionary Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON DICTIONARIES MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_creation_and_access()
    demo_mutation()
    demo_deleting()
    demo_views_and_looping()
    demo_merging()
    demo_frequency_counter()
    demo_comprehensions()
    demo_nested_dicts()
    print_cheat_sheet()