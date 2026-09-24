"""
================================================================================
   MODULE 07: DECORATORS & MAGIC DUNDER METHODS IN PYTHON
================================================================================
This script covers:
  1. Function Decorators: extending behavior without modifying source
  2. Decorators with arguments and return values (*args, **kwargs)
  3. Core Magic Dunder Methods:
     - __str__ vs __repr__ (Representation)
     - __len__ (Container length)
     - __add__ (Operator Overloading for +)
     - __eq__ (Equality Comparison for ==)
================================================================================
"""

import sys
import time

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(title: str):
    print("\n" + "=" * 75)
    print(f"  {title.upper()}")
    print("=" * 75)


# 1. Timing Decorator
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration_ms = (time.perf_counter() - start) * 1000
        print(f"  [@decorator] '{func.__name__}' executed in {duration_ms:.3f} ms")
        return result
    return wrapper


@measure_execution_time
def compute_power(base: int, exp: int) -> int:
    return base ** exp


# 2. Vector Class showcasing Dunder Methods & Operator Overloading
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # __str__: User-friendly string
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # __repr__: Formal developer representation
    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    # Operator Overloading for + (__add__)
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector2D to another Vector2D")

    # Operator Overloading for == (__eq__)
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False


def main():
    banner("1. Function Decorators in Action")
    res = compute_power(2, 1000)
    print(f"Power computation (2^1000) finished. Digits in answer: {len(str(res))}")

    banner("2. Magic Dunder Methods & Operator Overloading")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(5, 7)
    v3 = Vector2D(3, 4)

    print(f"v1: {v1} (via __str__)")
    print(f"Developer repr: {repr(v1)} (via __repr__)")

    # Operator Overloading for +
    v_sum = v1 + v2
    print(f"v1 + v2 = {v_sum} (via __add__)")

    # Operator Overloading for ==
    print(f"v1 == v2: {v1 == v2} (via __eq__)")
    print(f"v1 == v3: {v1 == v3} (via __eq__)")


if __name__ == "__main__":
    main()
