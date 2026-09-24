"""
================================================================================
         PYTHON LISTS - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Complete definitions, memory concepts & cheat sheet.
  2. AN EXECUTABLE LAB: Run it in your terminal to see every list algorithm
     and method in action!

Command to run:
  python list.py
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
# CORE THEORY: WHAT IS A LIST IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Definition:
   A list is an ORDERED, MUTABLE collection of elements enclosed in square
   brackets []. Lists can store heterogeneous data types (integers, strings, floats,
   objects, even other lists).

2. Mutability (Key Difference from Tuples & Strings):
   Lists can be modified in-place: you can add, update, replace, and delete elements
   without creating a new object in memory.

3. In-Place (.sort()) vs New Object (sorted()):
   - `my_list.sort()`: Modifies the original list directly in-place and returns None.
   - `sorted(my_list)`: Leaves the original list untouched and returns a NEW sorted list.

4. List Comprehension:
   A concise, Pythonic way to construct new lists:
     [expression for item in iterable if condition]
"""


# ==============================================================================
# DEMONSTRATION 1: BASIC OPERATIONS, SUM & AVERAGE
# ==============================================================================
def demo_sum_and_average():
    banner("Section 1: Sum and Average", "Manual Loop Calculation vs Built-in sum()")

    numbers = [12, 45, 67, 23, 89, 34, 90, 23, 56]
    print(f"Sample List: {numbers} (Count: {len(numbers)})")

    # Manual calculation
    total_sum = 0
    for n in numbers:
        total_sum += n
    average = total_sum / len(numbers)

    print(f"Manual Total Sum: {total_sum}")
    print(f"Manual Average:   {average:.2f}")
    print(f"Built-in sum():   {sum(numbers)} | Built-in Avg: {sum(numbers)/len(numbers):.2f}")


# ==============================================================================
# DEMONSTRATION 2: FINDING MINIMUM & MAXIMUM MANUALLY
# ==============================================================================
def demo_min_max():
    banner("Section 2: Finding Largest & Smallest", "Algorithm Without Using min() or max()")

    numbers = [34, 12, 89, 5, 78, 99, 23]
    print(f"Examining List: {numbers}")

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    print(f"Largest Element:  {largest}  (Verified with max: {max(numbers)})")
    print(f"Smallest Element: {smallest}   (Verified with min: {min(numbers)})")


# ==============================================================================
# DEMONSTRATION 3: SECOND LARGEST ELEMENT (CLASSIC EXAM QUESTION)
# ==============================================================================
def demo_second_largest():
    banner("Section 3: Second Largest Element", "Single-Pass Algorithm Handling Duplicates")

    # List with duplicates and extreme values
    numbers = [10, 45, 90, 85, 90, 23, 67]
    print(f"List with duplicate highest: {numbers}")

    # Track both first and second largest simultaneously
    first_largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num

    print(f"First Largest:  {first_largest}")
    print(f"Second Largest: {second_largest}")


# ==============================================================================
# DEMONSTRATION 4: REMOVING DUPLICATES (PRESERVING ORDER)
# ==============================================================================
def demo_remove_duplicates():
    banner("Section 4: Duplicate Removal", "Preserving Insertion Order vs Set Conversion")

    raw_list = [1, 2, 2, 3, 4, 1, 5, 6, 4, 7]
    print(f"Original List: {raw_list}")

    # Method A: Preserving original order using a loop
    unique_ordered = []
    seen = set()
    for item in raw_list:
        if item not in seen:
            seen.add(item)
            unique_ordered.append(item)

    # Method B: Quick set conversion (Note: Sets do not guarantee order)
    unique_set = list(set(raw_list))

    print(f"Preserving Order: {unique_ordered}")
    print(f"Via set():        {unique_set}")


# ==============================================================================
# DEMONSTRATION 5: MERGE & SORT (BUBBLE SORT VS TIMSORT)
# ==============================================================================
def demo_sorting():
    banner("Section 5: Merging & Sorting", "Manual Bubble Sort Algorithm vs sorted()")

    list1 = [5, 2, 9, 1]
    list2 = [8, 3, 7, 4]
    combined = list1 + list2
    print(f"Combined List: {combined}")

    # Manual Bubble Sort Algorithm
    arr = combined.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"Bubble Sorted: {arr}")
    print(f"sorted() Func: {sorted(combined)}")


# ==============================================================================
# DEMONSTRATION 6: PARTITIONING EVEN AND ODD NUMBERS
# ==============================================================================
def demo_even_odd_partition():
    banner("Section 6: Even / Odd Separation", "Partitioning into Separate Sub-Lists")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]

    print(f"Original: {nums}")
    print(f"Evens:    {evens}")
    print(f"Odds:     {odds}")


# ==============================================================================
# DEMONSTRATION 7: PALINDROME NUMBERS IN A LIST
# ==============================================================================
def demo_palindromes():
    banner("Section 7: Palindromic Numbers", "Detecting Symmetric Numbers in a List")

    candidates = [121, 12345, 1331, 45654, 9876]
    for num in candidates:
        s = str(num)
        is_pal = (s == s[::-1])
        status = "PALINDROME" if is_pal else "Normal"
        print(f"  {num:>6}: {status}")


# ==============================================================================
# DEMONSTRATION 8: LIST INTERSECTION & COMMON ELEMENTS
# ==============================================================================
def demo_intersection():
    banner("Section 8: List Intersection", "Finding Shared Elements Between Two Lists")

    l1 = [10, 20, 30, 40, 50]
    l2 = [30, 40, 50, 60, 70]

    # Manual loop check
    common_manual = [x for x in l1 if x in l2]
    # Set intersection
    common_set = list(set(l1) & set(l2))

    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"Common Elements: {common_manual}")


# ==============================================================================
# DEMONSTRATION 9: ESSENTIAL LIST METHODS (.append, .extend, .pop, .insert)
# ==============================================================================
def demo_list_methods():
    banner("Section 9: Core List Mutation Methods", "In-Place Modification Operations")

    fruits = ["apple", "banana"]
    print(f"Starting List:         {fruits}")

    fruits.append("cherry")
    print(f"After .append('cherry'): {fruits}")

    fruits.extend(["date", "elderberry"])
    print(f"After .extend([...]):   {fruits}  (Unpacks and adds multiple)")

    fruits.insert(1, "blueberry")
    print(f"After .insert(1, ...):  {fruits}  (Inserts at index 1)")

    popped_item = fruits.pop()
    print(f"After .pop():           {fruits}  (Removed last item: '{popped_item}')")

    fruits.remove("banana")
    print(f"After .remove('banana'): {fruits}  (Removed specific value)")

    fruits.reverse()
    print(f"After .reverse():       {fruits}  (Reversed in-place)")


# ==============================================================================
# DEMONSTRATION 10: LIST COMPREHENSION POWER
# ==============================================================================
def demo_list_comprehension():
    banner("Section 10: List Comprehension", "[expression for item in iterable if condition]")

    # 1. Squares of even numbers
    squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Squares of evens (1..10): {squares}")

    # 2. String manipulation
    words = ["hello", "python", "world"]
    uppercased = [w.upper() for w in words]
    print(f"Uppercased words:         {uppercased}")

    # 3. Flattening a 2D matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Original 2D Matrix:       {matrix}")
    print(f"Flattened 1D List:        {flattened}")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                    PYTHON LISTS QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Method / Syntax':<24} | {'Description':<32} | {'Time Complexity':<18}")
    print("-" * 80)
    print(f"{'my_list[i]':<24} | {'Index access (get/set)':<32} | {'O(1)':<18}")
    print(f"{'.append(x)':<24} | {'Add element at the end':<32} | {'O(1)':<18}")
    print(f"{'.extend(iterable)':<24} | {'Append all items from iterable':<32} | {'O(K)':<18}")
    print(f"{'.insert(i, x)':<24} | {'Insert x at index i':<32} | {'O(N)':<18}")
    print(f"{'.remove(x)':<24} | {'Remove first occurrence of x':<32} | {'O(N)':<18}")
    print(f"{'.pop(i)':<24} | {'Remove & return item at index':<32} | {'O(1) end, O(N) mid':<18}")
    print(f"{'.sort()':<24} | {'Sort list in-place (None)':<32} | {'O(N log N)':<18}")
    print(f"{'sorted(list)':<24} | {'Return a new sorted list':<32} | {'O(N log N)':<18}")
    print(f"{'.reverse()':<24} | {'Reverse list in-place':<32} | {'O(N)':<18}")
    print(f"{'[x for x in L if c]':<24} | {'List comprehension':<32} | {'O(N)':<18}")
    print("=" * 80)
    print("List Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON LISTS MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_sum_and_average()
    demo_min_max()
    demo_second_largest()
    demo_remove_duplicates()
    demo_sorting()
    demo_even_odd_partition()
    demo_palindromes()
    demo_intersection()
    demo_list_methods()
    demo_list_comprehension()
    print_cheat_sheet()