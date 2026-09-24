"""
================================================================================
   MODULE 03: FUNCTIONS, ARGUMENTS & SCOPE (LEGB) IN PYTHON
================================================================================
This script covers:
  1. Function definition, return values, type hints
  2. Positional, Keyword, Default, and Arbitrary arguments (*args, **kwargs)
  3. The LEGB Scope Rule (Local, Enclosing, Global, Built-in)
  4. The global and nonlocal keywords
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


# Global variable at module level
module_counter = 0


def increment_global():
    global module_counter
    module_counter += 1


def main():
    banner("1. Argument Types & Flexibility")

    # Positional, Default, *args (tuple), **kwargs (dict)
    def create_profile(username: str, role: str = "Member", *badges, **details):
        print(f"User: {username} | Role: {role}")
        print(f"Badges (*args tuple):   {badges}")
        print(f"Details (**kwargs dict): {details}")

    create_profile("sarthak_dev", "Admin", "Pythonista", "Top Contributor", location="Delhi", points=1250)

    banner("2. The LEGB Scope Resolution Rule")
    print("Python resolves names in this order: Local -> Enclosing -> Global -> Built-in")

    app_name = "GlobalApp"  # Global to nested functions

    def outer():
        tier = "EnclosingTier"  # Enclosing

        def inner():
            session_id = 9999   # Local
            print(f"  Inside inner(): Local={session_id}, Enclosing={tier}, Global={app_name}")

        inner()

    outer()

    banner("3. Modifying Outer Scopes: global and nonlocal")
    print(f"Module counter before: {module_counter}")
    increment_global()
    print(f"Module counter after increment_global(): {module_counter}")

    def outer_counter():
        num = 10
        def inner_increment():
            nonlocal num
            num += 5
        inner_increment()
        return num

    print(f"Enclosing num after inner nonlocal increment: {outer_counter()}")


if __name__ == "__main__":
    main()
