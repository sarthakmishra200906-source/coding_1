"""
================================================================================
   MODULE 07: GENERATORS, YIELD & ITERATORS IN PYTHON
================================================================================
This script covers:
  1. The Iterator protocol (__iter__ and __next__)
  2. Generator functions using the `yield` keyword
  3. Infinite / Large sequence streaming with minimal RAM footprint
  4. Generator pipeline chaining
================================================================================
"""

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def banner(title: str):
    print("\n" + "=" * 75)
    print(f"  {title.upper()}")
    print("=" * 75)


# 1. Custom Iterator Class
class CountdownIterator:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


# 2. Generator Function using `yield`
def fibonacci_generator(limit: int):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def main():
    banner("1. Custom Class Iterator (__iter__ and __next__)")
    countdown = CountdownIterator(3)
    print(f"Calling next(countdown): {next(countdown)}")
    print(f"Calling next(countdown): {next(countdown)}")
    print(f"Calling next(countdown): {next(countdown)}")
    try:
        next(countdown)
    except StopIteration:
        print("StopIteration raised as expected when sequence ended!")

    banner("2. Generator Function with `yield`")
    print("Generating first 8 Fibonacci numbers on-the-fly:")
    for num in fibonacci_generator(8):
        print(num, end=" ")
    print()

    banner("3. Memory Footprint Comparison")
    # 1 Million numbers via list vs generator
    huge_gen = (x * 2 for x in range(1_000_000))
    print(f"Memory size of generator producing 1,000,000 items: {sys.getsizeof(huge_gen)} bytes!")
    print(">> Generators compute elements lazily on demand, keeping memory constant.")


if __name__ == "__main__":
    main()
