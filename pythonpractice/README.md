# Python Complete Master Revision Guide 🚀
> **The All-In-One Study Handbook & Interactive Lab: From Basic to Advanced**

Welcome to your structured, comprehensive Python revision repository. Every module is paired with in-depth theory, definition notes, and standalone executable examples with clear console output.

---

## 📚 Curriculum & Directory Structure

```
pythonpractice/
│
├── 01_basics_and_syntax/
│   ├── 01_variables_and_datatypes.py      # Primitive types, dynamic typing, type casting
│   ├── 02_operators_and_expressions.py    # Arithmetic, identity (is), membership (in), bitwise
│   └── 03_conditionals_and_loops.py      # if/else, ternary, loops, for...else, prime/Armstrong
│
├── 02_data_structures/
│   ├── 01_strings.py                      # Slicing, reversals, run-length compression, palindromes
│   ├── 02_lists.py                        # In-place vs sorted(), second largest, Bubble sort
│   ├── 03_tuples.py                       # Immutability, (5,) gotcha, packing, *unpacking
│   ├── 04_sets.py                         # Unordered, unique, math ops (|, &, -, ^), frozenset
│   └── 05_dictionaries.py                 # O(1) hash maps, safe .get(), frequency counters, | merge
│
├── 03_functions_and_algorithms/
│   ├── 01_functions_and_scope.py          # def, *args, **kwargs, LEGB scope, global, nonlocal
│   ├── 02_recursion_and_math.py           # Factorial, Fibonacci, Euclidean GCD, Strong numbers
│   └── 03_lambda_map_filter.py            # Anonymous functions, map(), filter(), reduce(), sort keys
│
├── 04_object_oriented_programming/
│   ├── 01_classes_and_objects.py          # Blueprints, __init__, self, @classmethod, @staticmethod
│   ├── 02_class_vs_instance_vars.py       # Namespaces, __dict__, the Shadowing pitfall
│   └── 03_oop_four_pillars.py             # Encapsulation, Inheritance, Polymorphism, Abstraction (ABC)
│
├── 05_file_handling/
│   ├── 01_text_files_and_modes.py         # Modes ('r','w','a','r+'), with context manager, seek/tell
│   ├── 02_csv_and_data_splitting.py       # Tabular CSV processing, even/odd file partitioning
│   └── (Additional exercises in practice2/file2.py - file8.py)
│
├── 06_error_and_exception_handling/
│   ├── 01_try_except_finally.py           # try, except, else, finally, built-in exception types
│   └── 02_custom_exceptions_and_chaining.py# Subclassing Exception, raise, exception chaining (from)
│
├── 07_advanced_python/
│   ├── 01_comprehensions.py               # List, set, dict comprehensions, generator expressions
│   ├── 02_generators_and_iterators.py     # yield keyword, lazy evaluation, memory comparison
│   └── 03_decorators_and_dunders.py       # @decorator syntax, timing, operator overloading (+, ==)
│
├── practice2/
│   └── classqobtheoryandpractical.py      # THE ALL-IN-ONE MASTER COMPILATION (Modules 1 - 9)
```

---

## ⚡ Quick Start: Running Any Module

Run the **All-In-One Masterclass** (covers all 9 modules from Basic to Advanced in one script):
```powershell
python practice2/classqobtheoryandpractical.py
```

Or run any focused module individually:
```powershell
# Basics
python 01_basics_and_syntax/01_variables_and_datatypes.py
python 01_basics_and_syntax/02_operators_and_expressions.py
python 01_basics_and_syntax/03_conditionals_and_loops.py

# Data Structures
python 02_data_structures/01_strings.py
python 02_data_structures/02_lists.py
python 02_data_structures/03_tuples.py
python 02_data_structures/04_sets.py
python 02_data_structures/05_dictionaries.py

# Functions & Algorithms
python 03_functions_and_algorithms/01_functions_and_scope.py
python 03_functions_and_algorithms/02_recursion_and_math.py
python 03_functions_and_algorithms/03_lambda_map_filter.py

# Object-Oriented Programming (OOP)
python 04_object_oriented_programming/01_classes_and_objects.py
python 04_object_oriented_programming/02_class_vs_instance_vars.py
python 04_object_oriented_programming/03_oop_four_pillars.py

# File Handling & Exceptions
python 05_file_handling/01_text_files_and_modes.py
python 05_file_handling/02_csv_and_data_splitting.py
python 06_error_and_exception_handling/01_try_except_finally.py
python 06_error_and_exception_handling/02_custom_exceptions_and_chaining.py

# Advanced Python
python 07_advanced_python/01_comprehensions.py
python 07_advanced_python/02_generators_and_iterators.py
python 07_advanced_python/03_decorators_and_dunders.py
```

---

## 🧠 Master Cheat Sheet Summary

| Data Structure / Feature | Mutability | Order | Duplicate Allowed? | Primary Use Case | Time Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List (`[]`)** | Mutable | Ordered | Yes | General collections, dynamic arrays | $O(1)$ append, $O(N)$ lookup |
| **Tuple (`()`)** | **Immutable** | Ordered | Yes | Fixed records, dict keys, function returns | $O(1)$ lookup, memory efficient |
| **Set (`{}`)** | Mutable | **Unordered** | **No** | Deduplication, mathematical set operations | $O(1)$ average membership lookup |
| **Dict (`{k: v}`)** | Mutable | Ordered (3.7+) | Unique Keys | Key-value associative lookup, mappings | $O(1)$ average key access |
| **String (`""`)** | **Immutable** | Ordered | Yes | Text data, character sequences | Slicing creates new object |

---

## 🏆 The 4 Pillars of OOP Quick Reference
1. **Encapsulation**: Bundling state and behavior; protecting private data (`__balance`) via Name Mangling (`_Class__balance`) and getters/setters.
2. **Inheritance**: Reusing code hierarchically (`class Child(Parent):`); using `super().__init__()` for constructor chaining.
3. **Polymorphism**: Same interface, different behavior via Method Overriding and Duck Typing.
4. **Abstraction**: Enforcing design contracts using `from abc import ABC, abstractmethod`.
