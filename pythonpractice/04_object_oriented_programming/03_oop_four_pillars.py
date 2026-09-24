"""
================================================================================
          COMPLETE PYTHON MASTERCLASS: FROM BASIC TO ADVANCED
================================================================================
A comprehensive, all-in-one revision notebook and interactive lab.
Covers the entire Python curriculum with in-depth theory, definitions,
runnable examples, error handling demonstrations, and cheat sheets.

CURRICULUM MODULES:
  Module 1: Fundamentals, Variables, Data Types & Operators
  Module 2: Control Flow (Conditionals, Loops & Loop-Else)
  Module 3: Functions, Arguments (*args/**kwargs), Scope (LEGB) & Recursion
  Module 4: Core Data Structures (Strings, Lists, Tuples, Sets, Dicts)
  Module 5: Object-Oriented Programming (The 4 Pillars of OOP)
  Module 6: File Handling & Context Managers (Text, CSV & Pointers)
  Module 7: Exception Handling (try/except/else/finally & Custom Errors)
  Module 8: Advanced Python (Comprehensions, Generators & Decorators)
  Module 9: Master Revision Cheat Sheet & Complexity Guide

Run this script:
  python classqobtheoryandpractical.py
================================================================================
"""

import sys
import os
from abc import ABC, abstractmethod
import time

# Ensure safe UTF-8 output across all Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# UI & FORMATTING HELPERS
# ==============================================================================
def module_banner(mod_num: int, title: str, subtitle: str):
    print("\n" + "=" * 80)
    print(f"  MODULE {mod_num}: {title.upper()}")
    print(f"  >> {subtitle}")
    print("=" * 80)


def sub_heading(text: str):
    print(f"\n--- [ {text} ] ---")


# ==============================================================================
# MODULE 1: FUNDAMENTALS, DATA TYPES & OPERATORS
# ==============================================================================
"""
THEORY - MODULE 1:
1. Python Characteristics:
   - High-level, interpreted, dynamically-typed (types checked at runtime).
   - Everything in Python is an OBJECT (even integers, functions, and classes).
2. Primitive Data Types:
   - int: Arbitrary precision integers (e.g., 42).
   - float: Double-precision floating point numbers (e.g., 3.14159).
   - complex: Complex numbers with real and imaginary parts (e.g., 3 + 4j).
   - bool: Boolean values (True, False). Subclass of int (True==1, False==0).
   - str: Immutable sequence of Unicode characters.
   - NoneType: Represents the absence of a value (None).
3. Operators:
   - Arithmetic: +, -, *, /, // (floor division), % (modulo), ** (exponentiation)
   - Comparison: ==, !=, >, <, >=, <=
   - Logical: and, or, not (short-circuit evaluation)
   - Identity: `is`, `is not` (checks if two variables point to same MEMORY ID)
   - Membership: `in`, `not in` (checks if element exists in a collection)
   - Bitwise: &, |, ^, ~, <<, >>
"""

def demo_module_1():
    module_banner(1, "Fundamentals, Variables & Operators", "Data Types, Identity vs Equality, Type Casting")

    sub_heading("1. Primitive Types & Dynamic Typing")
    age = 20
    gpa = 9.4
    name = "Sarthak"
    is_student = True
    no_data = None

    print(f"age:        {age:<8} | Type: {type(age).__name__}")
    print(f"gpa:        {gpa:<8} | Type: {type(gpa).__name__}")
    print(f"name:       {name:<8} | Type: {type(name).__name__}")
    print(f"is_student: {str(is_student):<8} | Type: {type(is_student).__name__}")
    print(f"no_data:    {str(no_data):<8} | Type: {type(no_data).__name__}")

    sub_heading("2. Explicit Type Casting")
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_int)
    print(f"String '{num_str}' -> int: {num_int} -> float: {num_float}")

    sub_heading("3. Arithmetic & Floor Division vs True Division")
    print(f"17 / 5  = {17 / 5}   (True Float Division)")
    print(f"17 // 5 = {17 // 5}     (Floor Division / Integer quotient)")
    print(f"17 % 5  = {17 % 5}     (Modulo / Remainder)")
    print(f"2 ** 8  = {2 ** 8}   (Exponentiation: 2 to power 8)")

    sub_heading("4. Equality (==) vs Identity (is)")
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a

    print(f"list_a: {list_a} (id: {hex(id(list_a))})")
    print(f"list_b: {list_b} (id: {hex(id(list_b))})")
    print(f"list_c: {list_c} (id: {hex(id(list_c))})")

    print(f"list_a == list_b: {list_a == list_b}  (True because contents are identical)")
    print(f"list_a is list_b: {list_a is list_b} (False because they are distinct memory objects!)")
    print(f"list_a is list_c: {list_a is list_c}  (True because list_c references the exact same memory!)")


# ==============================================================================
# MODULE 2: CONTROL FLOW & ITERATION
# ==============================================================================
"""
THEORY - MODULE 2:
1. Conditional Branching:
   - `if`, `elif`, `else` with indentation (standard 4 spaces).
   - Ternary Operator: `value_if_true if condition else value_if_false`
2. Loops:
   - `for item in iterable`: Used when the number of iterations is known or
     iterating over collections.
   - `while condition`: Used when iteration depends on a dynamic boolean condition.
3. Loop Control Statements:
   - `break`: Terminates loop execution immediately.
   - `continue`: Skips remainder of current iteration and proceeds to next.
   - `pass`: Null operation; placeholder for future code.
4. The Loop-Else Construct (Unique to Python!):
   - `else` attached to a `for` or `while` loop runs ONLY IF the loop finishes
     normally WITHOUT hitting a `break` statement!
"""

def demo_module_2():
    module_banner(2, "Control Flow & Logic", "Conditionals, Loops, Ternary Operator & Loop-Else")

    sub_heading("1. Ternary Operator")
    score = 85
    result_status = "Distinction" if score >= 75 else "Pass"
    print(f"Score {score} -> Result: {result_status}")

    sub_heading("2. for Loop with range(start, stop, step)")
    print("Even numbers from 2 to 10: ", end="")
    for i in range(2, 11, 2):
        print(i, end=" ")
    print()

    sub_heading("3. Python's Unique 'for...else' (Prime Number Check)")
    candidate_numbers = [11, 15]
    for num in candidate_numbers:
        # Check if num has any factors
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                print(f"  {num} is COMPOSITE (divided by {factor}). Loop broke early.")
                break
        else:
            # Executes ONLY IF loop completed without encountering break!
            print(f"  {num} is PRIME! (for-loop finished without breaking).")


# ==============================================================================
# MODULE 3: FUNCTIONS, SCOPE (LEGB) & RECURSION
# ==============================================================================
"""
THEORY - MODULE 3:
1. Functions:
   Modular, reusable blocks of logic defined with the `def` keyword.
2. Argument Types:
   - Positional: Passed in strict order.
   - Keyword: Passed by name (`func(b=2, a=1)`).
   - Default Arguments: Assigned fallback values if omitted (`def f(x=10)`).
   - Variable-Length Arguments:
     * `*args`: Collects extra positional arguments into a TUPLE.
     * `**kwargs`: Collects extra keyword arguments into a DICTIONARY.
3. Scope Resolution (LEGB Rule):
   Python looks for variables in this exact order:
   L - Local (inside current function)
   E - Enclosing (inside enclosing outer function for nested functions)
   G - Global (module-level variables)
   B - Built-in (built-in functions like len, print, range)
   To modify globals inside local scope: `global` keyword.
   To modify enclosing vars in nested functions: `nonlocal` keyword.
4. Recursion:
   A function calling itself with a base case to terminate execution.
"""

def demo_module_3():
    module_banner(3, "Functions, Scope & Recursion", "Flexible Arguments, LEGB Hierarchy & Recursive Algorithms")

    sub_heading("1. Arbitrary Arguments (*args and **kwargs)")
    def order_summary(customer: str, *items, **metadata):
        print(f"Customer: {customer}")
        print(f"Items Ordered (Tuple *args): {items}")
        print(f"Metadata (Dict **kwargs):     {metadata}")

    order_summary("Sarthak", "Python Book", "Mechanical Keyboard", delivery="Express", payment="UPI")

    sub_heading("2. LEGB Variable Scope (Local vs Global)")
    global_var = "I am Global"

    def outer_func():
        enclosing_var = "I am Enclosing"

        def inner_func():
            local_var = "I am Local"
            print(f"  Accessing inside inner_func: '{local_var}' | '{enclosing_var}' | '{global_var}'")

        inner_func()

    outer_func()

    sub_heading("3. Recursion: Factorial & Fibonacci")
    def factorial(n: int) -> int:
        # Base case
        if n <= 1:
            return 1
        # Recursive step
        return n * factorial(n - 1)

    print(f"5! (Factorial): {factorial(5)}")

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    fib_series = [fibonacci(i) for i in range(8)]
    print(f"First 8 Fibonacci numbers: {fib_series}")


# ==============================================================================
# MODULE 4: CORE DATA STRUCTURES REVISION
# ==============================================================================
"""
THEORY - MODULE 4:
Python provides 4 primary built-in collection types:
1. List: Ordered, Mutable, Heterogeneous, allows duplicates (`[1, 2, 3]`).
2. Tuple: Ordered, IMMUTABLE, allows duplicates, hashable (`(1, 2, 3)`).
3. Set: UNORDERED, Mutable, NO duplicates, O(1) lookup (`{1, 2, 3}`).
4. Dictionary: Key-Value pairs, unique hashable keys, O(1) lookup (`{'a': 1}`).
"""

def demo_module_4():
    module_banner(4, "Core Data Structures", "Strings, Lists, Tuples, Sets & Dictionaries")

    sub_heading("1. Strings (Slicing & Methods)")
    text = "Python Programming"
    print(f"Original: '{text}'")
    print(f"Reversed text[::-1]: '{text[::-1]}'")
    print(f"Uppercase & Split:   {text.upper().split()}")

    sub_heading("2. Lists (Mutation & Second Largest Algorithm)")
    nums = [14, 55, 99, 99, 32, 87]
    print(f"Original List: {nums}")
    # Second largest single-pass algorithm
    first = second = float("-inf")
    for n in nums:
        if n > first:
            second, first = first, n
        elif n > second and n != first:
            second = n
    print(f"Largest: {first} | Second Largest: {second}")

    sub_heading("3. Tuples (Immutability & Unpacking)")
    point = (10, 20, 30)
    x, y, z = point
    print(f"Tuple: {point} -> Unpacked: x={x}, y={y}, z={z}")

    sub_heading("4. Sets (Mathematical Operations)")
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"Union (set1 | set2):        {set1 | set2}")
    print(f"Intersection (set1 & set2): {set1 & set2}")
    print(f"Difference (set1 - set2):   {set1 - set2}")

    sub_heading("5. Dictionaries (Safe .get() & Frequency Counting)")
    word = "abracadabra"
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    print(f"Frequency of letters in '{word}':\n  {freq}")


# ==============================================================================
# MODULE 5: OBJECT-ORIENTED PROGRAMMING (THE 4 PILLARS)
# ==============================================================================
"""
THEORY - MODULE 5:
OOP structures software around Objects rather than functions and logic.
The 4 Pillars:
1. Encapsulation: Bundling data and methods; hiding private attributes (__name)
   via Python's name mangling mechanism.
2. Inheritance: Reusing parent attributes and methods in child classes via `super()`.
   Supports Single, Multilevel, and Multiple inheritance with MRO.
3. Polymorphism: Same interface/method name exhibiting different behaviors
   (Method Overriding & Duck Typing).
4. Abstraction: Hiding implementation details using Abstract Base Classes (`abc.ABC`).
"""

# Abstract Base Class
class BankAccount(ABC):
    def __init__(self, owner: str, opening_balance: float):
        self.owner = owner                # Public attribute
        self._account_type = "Generic"    # Protected attribute (convention)
        self.__balance = opening_balance  # Private attribute (Name Mangled)

    # Getter
    def get_balance(self) -> float:
        return self.__balance

    # Setter with validation
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    # Abstract method: must be implemented by children
    @abstractmethod
    def calculate_interest(self) -> float:
        pass


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, opening_balance: float, interest_rate: float):
        super().__init__(owner, opening_balance)
        self._account_type = "Savings"
        self.interest_rate = interest_rate

    # Concrete implementation of abstract method (Abstraction + Polymorphism)
    def calculate_interest(self) -> float:
        return self.get_balance() * (self.interest_rate / 100.0)


def demo_module_5():
    module_banner(5, "Object-Oriented Programming (OOP)", "The 4 Pillars: Encapsulation, Inheritance, Polymorphism & Abstraction")

    sub_heading("1. Encapsulation & Private Data Protection")
    acc = SavingsAccount(owner="Sarthak", opening_balance=50000.0, interest_rate=7.5)
    print(f"Account Owner (Public):       {acc.owner}")
    print(f"Account Type (Protected):     {acc._account_type}")
    print(f"Balance via Getter:           ${acc.get_balance():,.2f}")

    try:
        # Direct private access raises AttributeError
        print(acc.__balance)
    except AttributeError as err:
        print(f"Direct access acc.__balance failed: {err}")
        print(">> Protected by Name Mangling! Real attribute name is: _BankAccount__balance")

    sub_heading("2. Inheritance, super() & Abstraction Implementation")
    interest = acc.calculate_interest()
    print(f"Calculated Annual Interest:   ${interest:,.2f}")


# ==============================================================================
# MODULE 6: FILE HANDLING & CONTEXT MANAGERS
# ==============================================================================
"""
THEORY - MODULE 6:
1. File Modes:
   - 'r': Read (default; fails if file missing).
   - 'w': Write (truncates file to 0 bytes; creates if missing).
   - 'a': Append (writes at end of file; preserves existing content).
   - 'r+': Read and write.
2. Context Manager (`with open(...) as f:`):
   - Guarantees the file is closed automatically upon exiting the block,
     even if an unhandled Exception occurs.
3. Pointer Control:
   - `f.tell()`: Check byte position.
   - `f.seek(offset)`: Relocate pointer.
"""

def demo_module_6():
    module_banner(6, "File Handling & Context Managers", "Modes, Auto-Cleanup, Pointer Manipulation & CSV Logs")

    filename = "master_demo.txt"

    sub_heading("1. Writing and Appending with Context Manager")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Line 1: Python Master Guide\nLine 2: Built for comprehensive revision\n")

    with open(filename, "a", encoding="utf-8") as f:
        f.write("Line 3: Appended without data loss\n")

    sub_heading("2. Reading and Pointer Control (.seek and .tell)")
    with open(filename, "r", encoding="utf-8") as f:
        print(f"Pointer at start: {f.tell()}")
        first_10 = f.read(10)
        print(f"Read first 10 chars: '{first_10}' | Pointer now at: {f.tell()}")

        # Seek back to beginning
        f.seek(0)
        print(f"After f.seek(0), pointer reset to: {f.tell()}")
        full_content = f.read()

    print(f"\nFull file content:\n{full_content.strip()}")


# ==============================================================================
# MODULE 7: ERROR & EXCEPTION HANDLING
# ==============================================================================
"""
THEORY - MODULE 7:
1. Syntax Errors vs Runtime Exceptions:
   - SyntaxError: Detected during parsing before execution.
   - Exception: Occurs during execution (ZeroDivisionError, ValueError, etc.).
2. The Complete Exception Block:
   - `try`: Code that might raise an exception.
   - `except ExceptionType as err`: Catches and handles the exception.
   - `else`: Runs ONLY IF no exception was raised in `try`.
   - `finally`: Runs ALWAYS (used for mandatory cleanup).
3. Custom Exceptions:
   Created by subclassing Python's built-in `Exception` class.
"""

# Custom Exception Definition
class InsufficientFundsError(Exception):
    """Raised when an account withdrawal exceeds available balance."""
    def __init__(self, current_balance: float, withdrawal_amount: float):
        super().__init__(f"Cannot withdraw ${withdrawal_amount:,.2f}; balance is only ${current_balance:,.2f}")
        self.current_balance = current_balance
        self.withdrawal_amount = withdrawal_amount


def demo_module_7():
    module_banner(7, "Error & Exception Handling", "try / except / else / finally, Built-in Errors & Custom Exceptions")

    sub_heading("1. Handling Built-in Errors (try / except / else / finally)")
    def safe_divide(a, b):
        try:
            res = a / b
        except ZeroDivisionError as err:
            print(f"  [ERROR] Cannot divide by zero! ({err})")
        except TypeError as err:
            print(f"  [ERROR] Invalid types for division! ({err})")
        else:
            print(f"  [SUCCESS] {a} / {b} = {res}")
        finally:
            print("  [CLEANUP] Division transaction finished.")

    safe_divide(10, 2)
    print()
    safe_divide(10, 0)

    sub_heading("2. Custom User-Defined Exception")
    balance = 100.0
    withdraw = 250.0

    try:
        if withdraw > balance:
            raise InsufficientFundsError(balance, withdraw)
    except InsufficientFundsError as custom_err:
        print(f"Caught Custom Exception: {custom_err}")


# ==============================================================================
# MODULE 8: ADVANCED PYTHON (COMPREHENSIONS, GENERATORS & DECORATORS)
# ==============================================================================
"""
THEORY - MODULE 8:
1. Comprehensions:
   Concise syntax to build lists, sets, or dictionaries in a single readable line.
2. Generators & `yield`:
   Functions that return an iterator which produces values on-demand (lazy evaluation).
   Saves massive amounts of memory because the entire dataset is not stored in RAM!
3. Decorators:
   A function that takes another function as an argument, extends its behavior,
   and returns a new function without modifying the original code.
"""

# Decorator definition
def execution_timer(func):
    """Decorator to measure and display function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"  [@timer] '{func.__name__}' executed in {elapsed * 1000:.3f} ms")
        return result
    return wrapper


def demo_module_8():
    module_banner(8, "Advanced Python", "Comprehensions, Generators (yield) & Decorators (@)")

    sub_heading("1. List, Set & Dict Comprehensions")
    squares = [x**2 for x in range(1, 6)]
    even_set = {x for x in [1, 2, 2, 3, 4, 4, 5] if x % 2 == 0}
    num_to_cube = {x: x**3 for x in range(1, 4)}

    print(f"List Comprehension (Squares): {squares}")
    print(f"Set Comprehension (Evens):     {even_set}")
    print(f"Dict Comprehension (Cubes):    {num_to_cube}")

    sub_heading("2. Generators and Memory-Efficient Iteration (yield)")
    def countdown(n: int):
        while n > 0:
            yield n
            n -= 1

    gen = countdown(3)
    print(f"Generator Object: {gen} (Lazy evaluation, values not in memory yet)")
    print(f"  First next(gen):  {next(gen)}")
    print(f"  Second next(gen): {next(gen)}")
    print(f"  Third next(gen):  {next(gen)}")

    sub_heading("3. Function Decorators (@execution_timer)")
    @execution_timer
    def compute_sum_of_squares(limit: int) -> int:
        return sum(x**2 for x in range(limit))

    total = compute_sum_of_squares(50000)
    print(f"  Result: {total}")


# ==============================================================================
# MODULE 9: MASTER PYTHON CHEAT SHEET & QUICK ROADMAP
# ==============================================================================
def print_master_cheat_sheet():
    module_banner(9, "Master Python Cheat Sheet", "Essential Rules, Complexities & Concepts")

    print(f"{'Category':<16} | {'Key Syntax / Concept':<34} | {'Complexity / Rule':<24}")
    print("-" * 80)
    print(f"{'Data Types':<16} | {'int, float, bool, str, None':<34} | {'Dynamic, strongly typed':<24}")
    print(f"{'List':<16} | {'[1, 2, 3], .append(), .pop()':<34} | {'O(1) end, O(N) search':<24}")
    print(f"{'Tuple':<16} | {'(1, 2, 3), (single,)':<34} | {'Immutable, Hashable':<24}")
    print(f"{'Set':<16} | {'{1, 2, 3}, set() for empty':<34} | {'O(1) avg lookup, Unique':<24}")
    print(f"{'Dictionary':<16} | {'{k: v}, .get(k, default)':<34} | {'O(1) avg lookup, Hashable keys':<24}")
    print(f"{'Functions':<16} | {'def f(*args, **kwargs):':<34} | {'LEGB Scope resolution':<24}")
    print(f"{'OOP Pillars':<16} | {'Encapsulation, Inheritance, Poly, Abs':<34} | {'super(), abc.ABC':<24}")
    print(f"{'File Handling':<16} | {'with open(file, mode) as f:':<34} | {'Auto close, safe I/O':<24}")
    print(f"{'Exceptions':<16} | {'try / except / else / finally':<34} | {'Exception hierarchy':<24}")
    print(f"{'Advanced':<16} | {'Comprehensions, yield, @decorators':<34} | {'Pythonic & Memory Efficient':<24}")
    print("=" * 80)
    print("Python Masterclass revision tour completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT: RUNS ALL MODULES SEQUENTIALLY
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  WELCOME TO THE COMPLETE PYTHON MASTERCLASS (BASIC TO ADVANCED)")
    print("#  All-In-One Revision Lab & Interactive Curriculum")
    print("#" * 80)

    demo_module_1()
    demo_module_2()
    demo_module_3()
    demo_module_4()
    demo_module_5()
    demo_module_6()
    demo_module_7()
    demo_module_8()
    print_master_cheat_sheet()
