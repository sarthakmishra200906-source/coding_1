"""
================================================================================
   MODULE 06: CUSTOM EXCEPTIONS & EXCEPTION CHAINING
================================================================================
This script covers:
  1. Creating custom domain exceptions (subclassing Exception)
  2. Raising and re-raising exceptions (raise)
  3. Exception chaining (raise ... from cause)
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


# Custom Application Exception Hierarchy
class ApplicationError(Exception):
    """Base error for the application."""
    pass


class InvalidAgeError(ApplicationError):
    """Raised when an age is outside legal limits."""
    def __init__(self, age: int, message: str = "Age must be between 18 and 100"):
        super().__init__(f"{message} (Got: {age})")
        self.age = age


def register_voter(name: str, age: int):
    if age < 18:
        raise InvalidAgeError(age, "Applicant is underage for voter registration")
    print(f"[VOTER REGISTERED] Welcome, {name}!")


def main():
    banner("1. Custom User-Defined Exception")
    try:
        register_voter("Sarthak", 20)
        register_voter("MinorUser", 15)
    except InvalidAgeError as err:
        print(f"Caught custom exception: {err}")
        print(f"Stored rejected age attribute: {err.age}")

    banner("2. Exception Chaining (raise ... from)")
    try:
        try:
            # Simulating raw system error
            int("invalid_payload")
        except ValueError as original_error:
            # Wrap into higher-level domain error while attaching the cause
            raise ApplicationError("Failed to parse incoming payload") from original_error
    except ApplicationError as wrapped:
        print(f"High-level error: {wrapped}")
        print(f"Underlying cause: {wrapped.__cause__}")


if __name__ == "__main__":
    main()
