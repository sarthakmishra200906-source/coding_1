"""
================================================================================
     PYTHON FILE HANDLING - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete file modes, context managers, pointer logic.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     reading, writing, appending, word counts, CSV logging, and file splitting!

Command to run:
  python file.py
================================================================================
"""

import sys
import os

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
# CORE THEORY: FILE HANDLING IN PYTHON
# ==============================================================================
"""
THEORY CONCEPTS:
1. What is File Handling?
   A mechanism to read data from or write data to external files stored permanently
   on disk (secondary storage).

2. The `with open(...) as f:` Context Manager:
   - Always prefer `with open(...)` over manual `f = open()` and `f.close()`.
   - The context manager GUARANTEES that the file stream is safely flushed and
     closed as soon as the block exits, even if an unhandled Exception occurs!

3. Core File Modes:
   - 'r'  (Read): Default mode. Opens for reading. Fails (FileNotFoundError) if missing.
   - 'w'  (Write): Opens for writing. Creates file if missing; OVERWRITES / TRUNCATES
                   existing content if present!
   - 'a'  (Append): Opens for writing at end of file. Preserves existing content.
   - 'r+' (Read + Write): File pointer placed at beginning. Does not truncate.
   - 'w+' (Write + Read): Truncates file first, then allows reading and writing.
   - 'x'  (Exclusive Create): Creates file, fails if file already exists.
   - 't'  (Text): Default text mode.
   - 'b'  (Binary): For images, audio, compiled binaries (e.g., 'rb', 'wb').

4. File Pointers:
   - `f.tell()`: Returns current integer byte position of file pointer.
   - `f.seek(offset, whence)`: Moves pointer to a specific location (0=start).
"""


# ==============================================================================
# DEMONSTRATION 1: BASIC WRITING, READING & APPENDING
# ==============================================================================
def demo_read_write_append():
    banner("Section 1: Basic Write, Read & Append", "Modes 'w', 'r', and 'a'")

    filename = "demo_notes.txt"

    sub_heading("1. Writing to a file ('w' mode)")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Line 1: Welcome to Python File Handling!\n")
        f.write("Line 2: Python makes disk I/O simple and elegant.\n")
    print(f"Successfully created and wrote to '{filename}'.")

    sub_heading("2. Reading the file ('r' mode)")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"Content read from '{filename}':\n{content.strip()}")

    sub_heading("3. Appending to the file ('a' mode)")
    with open(filename, "a", encoding="utf-8") as f:
        f.write("Line 3: This line was appended later without erasing previous data.\n")
    print(f"Appended new line to '{filename}'.")

    # Read back to verify append
    with open(filename, "r", encoding="utf-8") as f:
        print(f"Updated content:\n{f.read().strip()}")


# ==============================================================================
# DEMONSTRATION 2: .read() vs .readline() vs .readlines()
# ==============================================================================
def demo_reading_methods():
    banner("Section 2: Reading Techniques", ".read() vs .readline() vs .readlines()")

    filename = "demo_notes.txt"

    sub_heading("1. f.read(n): Reads entire file (or up to n characters)")
    with open(filename, "r", encoding="utf-8") as f:
        first_15_chars = f.read(15)
        print(f"First 15 characters: '{first_15_chars}'")

    sub_heading("2. f.readline(): Reads a single line at a time")
    with open(filename, "r", encoding="utf-8") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        print(f"Line 1: '{line1}'")
        print(f"Line 2: '{line2}'")

    sub_heading("3. f.readlines(): Reads all lines into a Python list of strings")
    with open(filename, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
    print(f"readlines() list (Length: {len(all_lines)}):")
    for idx, line in enumerate(all_lines, 1):
        print(f"  Line {idx}: {line.strip()}")


# ==============================================================================
# DEMONSTRATION 3: FILE POINTER CONTROL (seek and tell)
# ==============================================================================
def demo_file_pointers():
    banner("Section 3: The File Pointer", "Inspecting with .tell() and Moving with .seek()")

    filename = "pointer_demo.txt"
    with open(filename, "w+", encoding="utf-8") as f:
        f.write("0123456789ABCDEF")

        # Where is the pointer right now?
        pos_after_write = f.tell()
        print(f"Pointer position after writing 16 bytes: {pos_after_write}")

        # Rewind pointer back to start
        f.seek(0)
        print(f"Pointer position after f.seek(0):         {f.tell()}")
        print(f"Reading 5 bytes from start:             '{f.read(5)}'")

        # Move pointer to index 10
        f.seek(10)
        print(f"Pointer position after f.seek(10):        {f.tell()}")
        print(f"Reading remaining bytes from pos 10:    '{f.read()}'")


# ==============================================================================
# DEMONSTRATION 4: TEXT METRICS (COUNTING LINES, WORDS, CHARS & VOWELS)
# ==============================================================================
def demo_text_analysis():
    banner("Section 4: File Content Analysis", "Counting Lines, Words, Characters, Vowels & Consonants")

    filename = "demo_notes.txt"

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    words = text.split()
    total_chars = len(text)
    vowels = sum(1 for ch in text if ch.lower() in "aeiou")
    consonants = sum(1 for ch in text if ch.isalpha() and ch.lower() not in "aeiou")

    print(f"File '{filename}' Metrics:")
    print(f"  Total Lines:      {len(lines)}")
    print(f"  Total Words:      {len(words)}")
    print(f"  Total Characters: {total_chars}")
    print(f"  Vowels:           {vowels}")
    print(f"  Consonants:       {consonants}")


# ==============================================================================
# DEMONSTRATION 5: SEARCHING WORDS IN A FILE
# ==============================================================================
def demo_word_search():
    banner("Section 5: Searching Inside Files", "Checking Word Presence Case-Insensitively")

    filename = "demo_notes.txt"
    search_terms = ["Python", "database", "handling"]

    with open(filename, "r", encoding="utf-8") as f:
        words_in_file = set(f.read().lower().split())

    for term in search_terms:
        # Check if lowercase term is in the set of words
        found = term.lower() in words_in_file
        status = "FOUND" if found else "NOT PRESENT"
        print(f"  Searching for '{term}': {status}")


# ==============================================================================
# DEMONSTRATION 6: STRUCTURED DATA LOGGING (CSV FORMAT)
# ==============================================================================
def demo_csv_logging():
    banner("Section 6: Working with CSV Files", "Writing Comma-Separated Values & Parsing Rows")

    csv_filename = "students.csv"

    # Write CSV header and rows
    records = [
        ("Roll", "Name", "Marks", "Status"),
        (101, "Sarthak", 95, "Passed"),
        (102, "Rahul", 36, "Failed"),
        (103, "Priya", 88, "Passed")
    ]

    with open(csv_filename, "w", encoding="utf-8") as f:
        for row in records:
            line = ",".join(str(item) for item in row)
            f.write(line + "\n")
    print(f"CSV data written to '{csv_filename}'.")

    sub_heading("Parsing CSV File Row by Row")
    with open(csv_filename, "r", encoding="utf-8") as f:
        for row_num, line in enumerate(f, 1):
            columns = [c.strip() for c in line.split(",")]
            print(f"  Row {row_num}: {columns}")


# ==============================================================================
# DEMONSTRATION 7: DATA FILTERING & SPLITTING INTO MULTIPLE FILES
# ==============================================================================
def demo_file_splitting():
    banner("Section 7: File Splitting", "Reading Numbers & Splitting into evens.txt and odds.txt")

    # Create dummy numbers file
    with open("numbers.txt", "w", encoding="utf-8") as f:
        f.write("12\n35\n8\n99\n44\n71\n60\n")

    # Split into evens and odds
    with open("numbers.txt", "r", encoding="utf-8") as src, \
         open("evens.txt", "w", encoding="utf-8") as even_f, \
         open("odds.txt", "w", encoding="utf-8") as odd_f:

        for line in src:
            num = int(line.strip())
            if num % 2 == 0:
                even_f.write(f"{num}\n")
            else:
                odd_f.write(f"{num}\n")

    print("Split 'numbers.txt' successfully:")
    with open("evens.txt", "r", encoding="utf-8") as ef:
        print(f"  evens.txt: {ef.read().split()}")
    with open("odds.txt", "r", encoding="utf-8") as of:
        print(f"  odds.txt:  {of.read().split()}")


# ==============================================================================
# DEMONSTRATION 8: SAFE EXCEPTION HANDLING (FileNotFoundError)
# ==============================================================================
def demo_file_exceptions():
    banner("Section 8: File Exception Handling", "Handling FileNotFoundError & PermissionError")

    missing_file = "non_existent_data_file.xyz"
    try:
        with open(missing_file, "r") as f:
            print(f.read())
    except FileNotFoundError as err:
        print(f"Gracefully caught FileNotFoundError: [Errno {err.errno}] {err.strerror}")
        print(">> Note: Always wrap disk operations in try...except for production reliability.")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                 PYTHON FILE HANDLING QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Mode':<8} | {'Description':<36} | {'Pointer / Truncation':<30}")
    print("-" * 80)
    print(f"{'r':<8} | {'Read only (Default)':<36} | {'Starts at 0; Fails if missing':<30}")
    print(f"{'w':<8} | {'Write only':<36} | {'TRUNCATES existing file to 0 bytes':<30}")
    print(f"{'a':<8} | {'Append (Write only at end)':<36} | {'Starts at EOF; Preserves old data':<30}")
    print(f"{'r+':<8} | {'Read and Write':<36} | {'Starts at 0; Overwrites bytes':<30}")
    print(f"{'w+':<8} | {'Write and Read':<36} | {'Truncates file first, then reads':<30}")
    print(f"{'x':<8} | {'Exclusive creation':<36} | {'Fails if file already exists':<30}")
    print(f"{'rb/wb':<8} | {'Binary Read / Write':<36} | {'For images, audio, byte objects':<30}")
    print("-" * 80)
    print(f"{'Method':<8} | {'Description':<36} | {'Key Note':<30}")
    print("-" * 80)
    print(f"{'.read()':<8} | {'Read entire content as string':<36} | {'.read(n) reads n characters':<30}")
    print(f"{'.readline()':<8} | {'Read single line up to \\n':<36} | {'Returns empty string at EOF':<30}")
    print(f"{'.readlines()':<8} | {'Read all lines into a list':<36} | {'Includes newline \\n characters':<30}")
    print(f"{'.seek(0)':<8} | {'Move file pointer back to start':<36} | {'.tell() checks current byte':<30}")
    print("=" * 80)
    print("File Handling Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON FILE HANDLING MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_read_write_append()
    demo_reading_methods()
    demo_file_pointers()
    demo_text_analysis()
    demo_word_search()
    demo_csv_logging()
    demo_file_splitting()
    demo_file_exceptions()
    print_cheat_sheet()
