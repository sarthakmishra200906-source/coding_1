# Python Revision & Masterclass Handbook 🐍📘
> **One-Stop Comprehensive Revision from Basic to Advanced Python**

This repository has been formatted and elevated with the assistance of **Google Antigravity** into a complete, textbook-grade study suite and interactive terminal lab for revising Python.

---

## 🌟 What's Inside

Every concept includes **in-depth theory notes, memory architecture explanations, runnable code demonstrations, and time complexity cheat sheets**.

### 📂 Directory Structure

```
coding_1/
│
├── README.md                                  # Complete repository overview and master guide
├── .gitignore                                 # Clean git environment rules
│
└── pythonpractice/
    ├── 01_basics_and_syntax/                  # MODULE 1: BASICS
    │   ├── 01_variables_and_datatypes.py      # Primitive types, dynamic typing, type casting
    │   ├── 02_operators_and_expressions.py    # Arithmetic, identity (is), membership (in), bitwise
    │   └── 03_conditionals_and_loops.py      # if/else, ternary, loops, for...else, number algorithms
    │
    ├── 02_data_structures/                    # MODULE 2: DATA STRUCTURES
    │   ├── 01_strings.py                      # Slicing, reversals, run-length compression, palindromes
    │   ├── 02_lists.py                        # In-place vs sorted(), second largest, Bubble sort
    │   ├── 03_tuples.py                       # Immutability, (5,) trap, packing, *unpacking
    │   ├── 04_sets.py                         # Unordered, unique, math ops (|, &, -, ^), frozenset
    │   └── 05_dictionaries.py                 # O(1) hash maps, safe .get(), frequency counters, | merge
    │
    ├── 03_functions_and_algorithms/           # MODULE 3: FUNCTIONS & ALGORITHMS
    │   ├── 01_functions_and_scope.py          # def, *args, **kwargs, LEGB scope, global, nonlocal
    │   ├── 02_recursion_and_math.py           # Factorial, Fibonacci, Euclidean GCD, Strong numbers
    │   └── 03_lambda_map_filter.py            # Lambdas, map(), filter(), reduce(), sort keys
    │
    ├── 04_object_oriented_programming/        # MODULE 4: OOP MASTERCLASS
    │   ├── 01_classes_and_objects.py          # Blueprints, __init__, self, @classmethod, @staticmethod
    │   ├── 02_class_vs_instance_vars.py       # Namespaces, __dict__, the Shadowing pitfall
    │   └── 03_oop_four_pillars.py             # Encapsulation, Inheritance, Polymorphism, Abstraction
    │
    ├── 05_file_handling/                      # MODULE 5: DISK I/O
    │   ├── 01_text_files_and_modes.py         # Modes ('r','w','a','r+'), with context manager, seek/tell
    │   └── 02_csv_and_data_splitting.py       # Tabular CSV processing, even/odd file partitioning
    │
    ├── 06_error_and_exception_handling/       # MODULE 6: DEFENSIVE CODING
    │   ├── 01_try_except_finally.py           # try, except, else, finally, built-in exception types
    │   └── 02_custom_exceptions_and_chaining.py# Custom errors, raise, exception chaining (from)
    │
    ├── 07_advanced_python/                    # MODULE 7: ADVANCED TOPICS
    │   ├── 01_comprehensions.py               # List, set, dict comprehensions, generator expressions
    │   ├── 02_generators_and_iterators.py     # yield keyword, lazy evaluation, memory profiling
    │   └── 03_decorators_and_dunders.py       # @decorator syntax, timing, operator overloading (+, ==)
    │
    └── practice2/
        └── classqobtheoryandpractical.py      # ALL-IN-ONE MASTER TOUR (Modules 1 - 9 in a single script)
```

---

## 🚀 Running the Modules

### The All-In-One Script (Modules 1 to 9):
To run the complete interactive Python curriculum in your terminal:

```powershell
python pythonpractice/practice2/classqobtheoryandpractical.py
```

### Or Run Any Specific Topic Individually:

```powershell
# Basics & Control Flow
python pythonpractice/01_basics_and_syntax/01_variables_and_datatypes.py
python pythonpractice/01_basics_and_syntax/02_operators_and_expressions.py
python pythonpractice/01_basics_and_syntax/03_conditionals_and_loops.py

# Core Data Structures
python pythonpractice/02_data_structures/01_strings.py
python pythonpractice/02_data_structures/02_lists.py
python pythonpractice/02_data_structures/03_tuples.py
python pythonpractice/02_data_structures/04_sets.py
python pythonpractice/02_data_structures/05_dictionaries.py

# Functions & Algorithms
python pythonpractice/03_functions_and_algorithms/01_functions_and_scope.py
python pythonpractice/03_functions_and_algorithms/02_recursion_and_math.py
python pythonpractice/03_functions_and_algorithms/03_lambda_map_filter.py

# Object-Oriented Programming (OOP)
python pythonpractice/04_object_oriented_programming/01_classes_and_objects.py
python pythonpractice/04_object_oriented_programming/02_class_vs_instance_vars.py
python pythonpractice/04_object_oriented_programming/03_oop_four_pillars.py

# File Handling & Exceptions
python pythonpractice/05_file_handling/01_text_files_and_modes.py
python pythonpractice/05_file_handling/02_csv_and_data_splitting.py
python pythonpractice/06_error_and_exception_handling/01_try_except_finally.py
python pythonpractice/06_error_and_exception_handling/02_custom_exceptions_and_chaining.py

# Advanced Python
python pythonpractice/07_advanced_python/01_comprehensions.py
python pythonpractice/07_advanced_python/02_generators_and_iterators.py
python pythonpractice/07_advanced_python/03_decorators_and_dunders.py
```

---

## 📊 Quick Complexity Reference

| Structure | Mutability | Ordering | Duplicates? | Primary Syntax | Average Lookup |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | Mutable | Ordered | Allowed | `[1, 2, 3]` | $O(1)$ by index / $O(N)$ by value |
| **Tuple** | **Immutable** | Ordered | Allowed | `(1, 2, 3)` | $O(1)$ by index / Hashable |
| **Set** | Mutable | **Unordered** | **Forbidden** | `{1, 2, 3}` | $O(1)$ average membership |
| **Dict** | Mutable | Ordered (3.7+) | Unique Keys | `{'key': 'value'}` | $O(1)$ average key access |
| **String** | **Immutable** | Ordered | Allowed | `"Python"` | $O(1)$ by index |

---

## 🏆 The 4 Pillars of OOP Quick Reference
1. **Encapsulation**: Bundling state and behavior; protecting private data (`__balance`) via Name Mangling (`_Class__balance`) and getters/setters.
2. **Inheritance**: Reusing code hierarchically (`class Child(Parent):`); using `super().__init__()` for constructor chaining.
3. **Polymorphism**: Same interface, different behavior via Method Overriding and Duck Typing.
4. **Abstraction**: Enforcing design contracts using `from abc import ABC, abstractmethod`.
