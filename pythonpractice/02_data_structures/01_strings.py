"""
================================================================================
         PYTHON STRINGS - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete definitions, memory concepts & cheat sheet.
  2. AN EXECUTABLE LAB: Run it in your terminal to see every string algorithm
     and method in action!

Command to run:
  python string.py
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
# CORE THEORY: WHAT IS A STRING IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Definition:
   A string in Python is an IMMUTABLE sequence of Unicode characters enclosed in
   single (' '), double (" "), or triple (''' ''' or \"\"\" \"\"\") quotes.

2. Immutability:
   Once created, a string's content CANNOT be altered in-place.
   Any method that transforms a string (like .upper(), .replace()) actually
   returns a BRAND NEW string object in memory.

3. Indexing:
   Python uses zero-based indexing for forward lookup, and negative indexing
   from the end:
     String:   P   Y   T   H   O   N
     Forward:  0   1   2   3   4   5
     Reverse: -6  -5  -4  -3  -2  -1

4. Slicing Syntax:
   string[start : stop : step]
   - start: Starting index (inclusive, default = 0)
   - stop:  Ending index (exclusive, default = len)
   - step:  Stride / direction (default = 1; negative step reverses direction)
"""


# ==============================================================================
# DEMONSTRATION 1: INDEXING & ADVANCED SLICING
# ==============================================================================
def demo_indexing_and_slicing():
    banner("Section 1: Indexing & Slicing", "Zero-based, Negative Indices & Reversal")

    text = "Python Programming"
    print(f"Sample text: '{text}' (Length: {len(text)})")

    sub_heading("Forward & Negative Indexing")
    print(f"First character  text[0]:   '{text[0]}'")
    print(f"Last character   text[-1]:  '{text[-1]}'")
    print(f"Middle character text[7]:   '{text[7]}'")

    sub_heading("Slicing [start:stop:step]")
    print(f"text[0:6]   (First 6 chars):   '{text[0:6]}'")
    print(f"text[7:]    (From index 7 on): '{text[7:]}'")
    print(f"text[:6]    (From start to 6): '{text[:6]}'")
    print(f"text[::2]   (Every 2nd char):  '{text[::2]}'")
    print(f"text[::-1]  (Full Reversal):   '{text[::-1]}'")


# ==============================================================================
# DEMONSTRATION 2: WORD-BY-WORD REVERSAL VS FULL REVERSAL
# ==============================================================================
def demo_reversing():
    banner("Section 2: Reversal Algorithms", "Full Reversal vs Word-by-Word Reversal")

    sentence = "Python is amazingly powerful"
    print(f"Original Sentence: '{sentence}'")

    sub_heading("1. Full Sentence Reversal")
    print(f"Result (sentence[::-1]): '{sentence[::-1]}'")

    sub_heading("2. Reverse Each Word Individually (Preserve Word Order)")
    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    result = " ".join(reversed_words)
    print("Explanation: .split() breaks words -> slice [::-1] reverses each -> ' '.join() reconnects.")
    print(f"Result: '{result}'")


# ==============================================================================
# DEMONSTRATION 3: VOWEL, CONSONANT & CHARACTER ANALYSIS
# ==============================================================================
def demo_char_counts():
    banner("Section 3: Character Analysis", "Counting Vowels, Consonants, Digits & Spaces")

    sample = "Hello World! Python 3.14 is Cool."
    print(f"Analyzing text: '{sample}'")

    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    special = 0

    for ch in sample:
        if ch.lower() in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1

    print(f"  Vowels:     {vowels}")
    print(f"  Consonants: {consonants}")
    print(f"  Digits:     {digits}")
    print(f"  Spaces:     {spaces}")
    print(f"  Special:    {special}")
    print(f"  Total:      {len(sample)} characters")


# ==============================================================================
# DEMONSTRATION 4: FIRST NON-REPEATING CHARACTER
# ==============================================================================
def demo_first_non_repeating():
    banner("Section 4: First Non-Repeating Character", "Finding the First Unique Character")

    test_words = ["swiss", "programming", "aabbcc"]

    for word in test_words:
        found_char = None
        for ch in word:
            # count() checks frequency across the entire word
            if word.count(ch) == 1:
                found_char = ch
                break

        if found_char:
            print(f"In '{word}': First unique character is '{found_char}'")
        else:
            print(f"In '{word}': No non-repeating character found!")


# ==============================================================================
# DEMONSTRATION 5: WHITESPACE STRIPPING & CLEANING
# ==============================================================================
def demo_stripping():
    banner("Section 5: Whitespace Handling", ".strip(), .lstrip(), .rstrip()")

    messy = "   >>> Hello Pythonista! <<<    "
    print(f"Raw String:    '{messy}'")
    print(f".strip():      '{messy.strip()}'     (Removes both leading and trailing spaces)")
    print(f".lstrip():     '{messy.lstrip()}'  (Removes left-side leading spaces only)")
    print(f".rstrip():     '{messy.rstrip()}' (Removes right-side trailing spaces only)")


# ==============================================================================
# DEMONSTRATION 6: CHARACTER FREQUENCY COUNTER
# ==============================================================================
def demo_frequency_counter():
    banner("Section 6: Frequency Counter", "Tracking Frequency without Duplicate Prints")

    text = "engineering"
    print(f"Analyzing word: '{text}'")

    seen = set()
    print("Frequency of each unique letter:")
    for ch in text:
        if ch not in seen:
            seen.add(ch)
            print(f"  '{ch}': appears {text.count(ch)} time(s)")


# ==============================================================================
# DEMONSTRATION 7: CASE CONVERSIONS & TOGGLING
# ==============================================================================
def demo_case_conversions():
    banner("Section 7: Case Conversions", "Manual Toggling vs Built-in .swapcase()")

    text = "PyThOn 3.14 Is AWESOME!"
    print(f"Original Text: '{text}'")

    # Manual toggle using islower() / isupper()
    manual_toggled = []
    for ch in text:
        if ch.islower():
            manual_toggled.append(ch.upper())
        elif ch.isupper():
            manual_toggled.append(ch.lower())
        else:
            manual_toggled.append(ch)
    manual_result = "".join(manual_toggled)

    print(f"Manual Toggle:      '{manual_result}'")
    print(f"Built-in .swapcase():'{text.swapcase()}'")
    print(f".upper():           '{text.upper()}'")
    print(f".lower():           '{text.lower()}'")
    print(f".title():           '{text.title()}'")


# ==============================================================================
# DEMONSTRATION 8: LONGEST & SHORTEST WORD IN A SENTENCE
# ==============================================================================
def demo_longest_word():
    banner("Section 8: Longest & Shortest Word", "Extracting Extreme Lengths from Text")

    sentence = "Data Structures and Object Oriented Programming in Python"
    print(f"Sentence: '{sentence}'")

    words = sentence.split()
    longest = max(words, key=len)
    shortest = min(words, key=len)

    print(f"Longest word:  '{longest}' (Length: {len(longest)})")
    print(f"Shortest word: '{shortest}' (Length: {len(shortest)})")


# ==============================================================================
# DEMONSTRATION 9: STRING COMPRESSION ALGORITHM (RUN-LENGTH ENCODING)
# ==============================================================================
def demo_compression():
    banner("Section 9: String Compression", "Run-Length Encoding ('aabcccccaaa' -> 'a2b1c5a3')")

    def compress(text: str) -> str:
        if not text:
            return ""

        compressed_parts = []
        count = 1

        for i in range(len(text)):
            # If next character matches, increment count
            if i + 1 < len(text) and text[i] == text[i + 1]:
                count += 1
            else:
                # Character changed or end of string reached
                compressed_parts.append(text[i] + str(count))
                count = 1

        result = "".join(compressed_parts)
        # Return compressed version only if it actually saves space
        return result if len(result) < len(text) else text

    raw_sample = "aabcccccaaa"
    compressed = compress(raw_sample)
    print(f"Raw Input:        '{raw_sample}' (Length: {len(raw_sample)})")
    print(f"Compressed Form:  '{compressed}' (Length: {len(compressed)})")


# ==============================================================================
# DEMONSTRATION 10: PALINDROMES & ANAGRAMS
# ==============================================================================
def demo_palindrome_and_anagram():
    banner("Section 10: Palindromes & Anagrams", "Slicing Check & Sorted Frequency Matching")

    sub_heading("Palindrome Check (Reads same forwards and backwards)")
    words = ["radar", "level", "python", "madam"]
    for w in words:
        is_pal = (w == w[::-1])
        status = "PALINDROME" if is_pal else "NOT a palindrome"
        print(f"  '{w}': {status}")

    sub_heading("Anagram Check (Contains same letters in any order)")
    pair1 = ("listen", "silent")
    pair2 = ("hello", "world")

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1.lower()) == sorted(str2.lower())

    print(f"  '{pair1[0]}' & '{pair1[1]}': Is Anagram? {is_anagram(*pair1)}")
    print(f"  '{pair2[0]}' & '{pair2[1]}': Is Anagram? {is_anagram(*pair2)}")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                    PYTHON STRINGS QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Method / Syntax':<24} | {'Description':<32} | {'Example':<18}")
    print("-" * 80)
    print(f"{'s[start:stop:step]':<24} | {'Extract substring / slice':<32} | {'s[1:5], s[::-1]':<18}")
    print(f"{'.split(sep)':<24} | {'Split string into list':<32} | {'s.split(\" \")':<18}")
    print(f"{'sep.join(list)':<24} | {'Combine list into string':<32} | {'\" \".join(words)':<18}")
    print(f"{'.strip()':<24} | {'Remove leading/trailing spaces':<32} | {'\"  hi \".strip()':<18}")
    print(f"{'.find(sub)':<24} | {'Index of substring (-1 if not)':<32} | {'s.find(\"py\")':<18}")
    print(f"{'.count(sub)':<24} | {'Frequency count of substring':<32} | {'s.count(\"a\")':<18}")
    print(f"{'.replace(old, new)':<24} | {'Replace occurrences':<32} | {'s.replace(\"a\", \"b\")':<18}")
    print(f"{'.lower() / .upper()':<24} | {'Convert case':<32} | {'s.lower(), s.upper()':<18}")
    print(f"{'.swapcase()':<24} | {'Toggle lowercase and uppercase':<32} | {'s.swapcase()':<18}")
    print(f"{'.isalpha() / .isdigit()':<24} | {'Type check booleans':<32} | {'\"123\".isdigit()':<18}")
    print("=" * 80)
    print("String Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON STRINGS MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_indexing_and_slicing()
    demo_reversing()
    demo_char_counts()
    demo_first_non_repeating()
    demo_stripping()
    demo_frequency_counter()
    demo_case_conversions()
    demo_longest_word()
    demo_compression()
    demo_palindrome_and_anagram()
    print_cheat_sheet()