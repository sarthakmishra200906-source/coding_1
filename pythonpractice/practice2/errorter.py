# ==============================================================================
# PYTHON ERRORS AND EXCEPTIONS MASTERCLASS SCRIPT
# ==============================================================================
# Run this script in your terminal to see how each exception mechanism works!
# ==============================================================================

import sys

print("=== 1. HANDLING BASIC EXCEPTIONS (Try, Except, Else, Finally) ===")
# This section demonstrates catching standard runtime errors gracefully.
try:
    num1 = int(input("Enter a number to divide 10 by: "))
    result = 10 / num1
except ZeroDivisionError:
    print("Caught error: Division by zero is not allowed!")
except ValueError:
    print("Caught error: You must enter a valid integer!")
else:
    # Runs ONLY if no exceptions occurred in the try block
    print(f"Success! Result is: {result}")
finally:
    # Runs ALWAYS, regardless of success or failure (used for cleanup)
    print("Executing final cleanup actions.\n")


print("=== 2. INSPECTING EXCEPTION ARGUMENTS & INSTANCES ===")
# You can bind the caught exception to a variable using 'as err' to read its details.
try:
    raise Exception("Database connection failed", 500)
except Exception as inst:
    print(f"Exception type: {type(inst)}")
    print(f"Stored arguments (.args): {inst.args}")
    print(f"Direct string representation: {inst}")
    x, y = inst.args
    print(f"Unpacked values -> Code: {y}, Message: {x}\n")


print("=== 3. RAISING AND RE-RAISING EXCEPTIONS ===")
# The 'raise' keyword lets you force an error, and you can re-raise it if needed.
try:
    try:
        raise NameError("CriticalSystemFailure")
    except NameError:
        print("Caught inner NameError, logging it, and re-raising...")
        raise  # Re-raises the exact same exception to outer blocks
except NameError as err:
    print(f"Caught outer re-raised exception: {err}\n")


print("=== 4. EXCEPTION CHAINING (from / from None) ===")
# Linking an underlying cause to a new wrapper exception using 'from'.
try:
    try:
        open("non_existent_database.sqlite")
    except OSError as original_error:
        # Raising a high-level error while keeping the cause attached
        raise RuntimeError("Failed to initialize application storage") from original_error
except RuntimeError as wrapped_err:
    print(f"Caught wrapped error: {wrapped_err}")
    print(f"Direct cause: {wrapped_err.__cause__}\n")


print("=== 5. ENRICHING EXCEPTIONS WITH NOTES (.add_note()) ===")
# Adding extra dynamic context to an exception after it has been caught.
try:
    raise TypeError("Invalid data format passed")
except TypeError as e:
    e.add_note("Context Note 1: Received data from API endpoint v2.")
    e.add_note("Context Note 2: Expected a JSON object, got a string.")
    try:
        raise
    except TypeError as final_err:
        print("--- Exception Output with Added Notes ---")
        print(final_err)
        for note in final_err.__notes__:
            print(f"  -> {note}")
        print("-----------------------------------------\n")


print("=== 6. USER-DEFINED CUSTOM EXCEPTIONS ===")
# Creating custom error classes by inheriting from the base Exception class.
class InsufficientFundsError(Exception):
    """Custom exception raised when an account has less than the required balance."""
    def __init__(self, balance, amount_needed):
        self.balance = balance
        self.amount_needed = amount_needed
        super().__init__(f"Attempted to withdraw {amount_needed}, but balance is only {balance}.")

# Using our custom exception
account_balance = 100
withdrawal_amount = 250

try:
    if withdrawal_amount > account_balance:
        raise InsufficientFundsError(account_balance, withdrawal_amount)
except InsufficientFundsError as custom_err:
    print(f"Caught Custom Exception: {custom_err}")
    print(f"  -> Deficit amount: {custom_err.amount_needed - custom_err.balance}\n")


print("=== 7. EXCEPTION GROUPS & EXCEPT* (Python 3.11+) ===")
# Grouping multiple independent exceptions together and filtering them with except*
def trigger_batch_failures():
    excs = [
        OSError("Disk write failed"),
        TimeoutError("Network request timed out"),
        ValueError("Invalid configuration value")
    ]
    raise ExceptionGroup("Batch Processing Errors", excs)

try:
    trigger_batch_failures()
except* OSError as os_group:
    print(f"Handled filtered OS/Network group: {os_group.exceptions}")
except* ValueError as val_group:
    print(f"Handled filtered Value error group: {val_group.exceptions}")

print("\nAll error handling paradigms successfully demonstrated!")