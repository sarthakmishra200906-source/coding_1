"""
===============================================================================
PYTHON TUTORIAL: CHAPTER 8. ERRORS AND EXCEPTIONS
===============================================================================
Until now error messages haven’t been more than mentioned, but if you have
tried out the examples you have probably seen some. There are (at least) two
distinguishable kinds of errors: syntax errors and exceptions.
===============================================================================
"""

import sys
import os

# =============================================================================
# 8.1. SYNTAX ERRORS
# =============================================================================
# Syntax errors, also known as parsing errors, are perhaps the most common kind
# of complaint you get while you are still learning Python:
#
# Example (Invalid Syntax):
# -------------------------
#   while True print('Hello world')
#              ^^^^^
#   SyntaxError: invalid syntax
#
# Explanation:
# ------------
# The parser repeats the offending line and displays little arrows pointing at
# the place where the error was detected. Note that this is not always the place
# that needs to be fixed. In the example, the error is detected at the function
# print(), since a colon (':') is missing just before it.
#
# The file name (<stdin> in our example) and line number are printed so you
# know where to look in case the input came from a file.

print("=" * 70)
print("8.1. SYNTAX ERRORS")
print("=" * 70)
print("Syntax errors are detected by the parser before code execution starts.")
print("Demonstrating corrected syntax (with ':' after while True):")

# Corrected example:
counter = 0
while True:
    print("  -> Hello world (fixed missing colon)")
    counter += 1
    if counter >= 1:
        break

print()


# =============================================================================
# 8.2. EXCEPTIONS
# =============================================================================
# Even if a statement or expression is syntactically correct, it may cause an
# error when an attempt is made to execute it. Errors detected during execution
# are called exceptions and are not unconditionally fatal: you will soon learn
# how to handle them in Python programs. Most exceptions are not handled by
# programs, however, and result in error messages as shown here:
#
# 1) ZeroDivisionError:
#    >>> 10 * (1/0)
#    Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#        10 * (1/0)
#              ~^~
#    ZeroDivisionError: division by zero
#
# 2) NameError:
#    >>> 4 + spam*3
#    Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#        4 + spam*3
#            ^^^^
#    NameError: name 'spam' is not defined
#
# 3) TypeError:
#    >>> '2' + 2
#    Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#        '2' + 2
#        ~~~~^~~
#    TypeError: can only concatenate str (not "int") to str
#
# The last line of the error message indicates what happened. Exceptions come
# in different types, and the type is printed as part of the message: the types
# in the example are ZeroDivisionError, NameError, and TypeError. The string
# printed as the exception type is the name of the built-in exception that
# occurred. This is true for all built-in exceptions, but need not be true for
# user-defined exceptions (although it is a useful convention). Standard
# exception names are built-in identifiers (not reserved keywords).
#
# The rest of the line provides detail based on the type of exception and what
# caused it.
#
# The preceding part of the error message shows the context where the exception
# occurred, in the form of a stack traceback. In general it contains a stack
# traceback listing source lines; however, it will not display lines read from
# standard input.

print("=" * 70)
print("8.2. EXCEPTIONS (DEMONSTRATING COMMON RUNTIME ERRORS)")
print("=" * 70)

# Handling ZeroDivisionError
try:
    result = 10 * (1 / 0)
except ZeroDivisionError as err:
    print(f"Caught ZeroDivisionError : {err}")

# Handling NameError
try:
    result = 4 + spam * 3  # type: ignore  # noqa: F821
except NameError as err:
    print(f"Caught NameError         : {err}")

# Handling TypeError
try:
    result = '2' + 2  # type: ignore
except TypeError as err:
    print(f"Caught TypeError         : {err}")

print()


# =============================================================================
# 8.3. HANDLING EXCEPTIONS
# =============================================================================
# It is possible to write programs that handle selected exceptions. Look at the
# following example, which asks the user for input until a valid integer has
# been entered, but allows the user to interrupt the program (using Control-C
# or whatever the operating system supports); note that a user-generated
# interruption is signalled by raising the KeyboardInterrupt exception.
#
# Interactive Example:
# --------------------
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
# The try statement works as follows:
# 1. First, the try clause (the statement(s) between the try and except
#    keywords) is executed.
# 2. If no exception occurs, the except clause is skipped and execution of
#    the try statement is finished.
# 3. If an exception occurs during execution of the try clause, the rest of the
#    clause is skipped. Then, if its type matches the exception named after the
#    except keyword, the except clause is executed, and then execution continues
#    after the try/except block.
# 4. If an exception occurs which does not match the exception named in the
#    except clause, it is passed on to outer try statements; if no handler is
#    found, it is an unhandled exception and execution stops with an error message.
#
# A try statement may have more than one except clause, to specify handlers for
# different exceptions. At most one handler will be executed. Handlers only
# handle exceptions that occur in the corresponding try clause, not in other
# handlers of the same try statement.
#
# Multiple Exceptions:
# --------------------
# In Python 3, when an except clause catches multiple exceptions, they MUST be
# specified as a parenthesized tuple:
#
#   except (RuntimeError, TypeError, NameError):
#       pass
# (Note: In Python 2, 'except RuntimeError, TypeError, NameError:' was permitted,
#  but in Python 3 this is a SyntaxError.)

print("=" * 70)
print("8.3. HANDLING EXCEPTIONS")
print("=" * 70)

# Simulated input parsing with ValueError handling:
test_inputs = ["not_a_number", "42"]
for sample in test_inputs:
    try:
        val = int(sample)
        print(f"Successfully converted '{sample}' to integer: {val}")
    except ValueError:
        print(f"Oops! '{sample}' was not a valid number. Handled ValueError.")

print()

# -----------------------------------------------------------------------------
# Polymorphism in Exception Handling (Inheritance Hierarchies)
# -----------------------------------------------------------------------------
# A class in an except clause matches exceptions which are instances of the
# class itself or one of its derived classes (but not the other way around — an
# except clause listing a derived class does not match instances of its base classes).
# For example, the following code will print B, C, D in that order:

print("--- Exception Class Inheritance Hierarchy ---")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("Caught D")
    except C:
        print("Caught C")
    except B:
        print("Caught B")

# Note: If the except clauses were reversed (with 'except B' first), it would
# have printed B, B, B — because B is the base class for both C and D, and the
# first matching except clause is triggered!

print()

# -----------------------------------------------------------------------------
# Exception Arguments and the 'as' keyword
# -----------------------------------------------------------------------------
# When an exception occurs, it may have associated values, also known as the
# exception’s arguments. The presence and types of the arguments depend on the
# exception type.
#
# The except clause may specify a variable after the exception name. The
# variable is bound to the exception instance which typically has an args
# attribute that stores the arguments. For convenience, builtin exception types
# define __str__() to print all the arguments without explicitly accessing .args.

print("--- Inspecting Exception Arguments (.args and __str__) ---")
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print("type(inst) :", type(inst))  # The exception type
    print("inst.args  :", inst.args)   # Arguments stored in .args
    print("inst       :", inst)        # __str__ allows args to be printed directly
    x, y = inst.args                   # Unpack args
    print("x =", x)
    print("y =", y)

print()

# BaseException is the common base class of all exceptions. One of its
# subclasses, Exception, is the base class of all the non-fatal exceptions.
# Exceptions which are not subclasses of Exception are not typically handled,
# because they are used to indicate that the program should terminate.
# They include SystemExit which is raised by sys.exit() and KeyboardInterrupt
# which is raised when a user wishes to interrupt the program.
#
# Exception can be used as a wildcard that catches (almost) everything.
# However, it is good practice to be as specific as possible with the types
# of exceptions that we intend to handle, and to allow any unexpected exceptions
# to propagate on.
#
# The most common pattern for handling Exception is to print or log the
# exception and then re-raise it (allowing a caller to handle the exception as well):

print("--- Wildcard Exception Handling Pattern ---")


def read_config_file(filename):
    try:
        with open(filename, 'r') as f:
            s = f.readline()
            return int(s.strip())
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


read_config_file("non_existent_file.txt")
print()

# -----------------------------------------------------------------------------
# The Optional 'else' Clause
# -----------------------------------------------------------------------------
# The try … except statement has an optional else clause, which, when present,
# must follow all except clauses. It is useful for code that must be executed
# if the try clause does not raise an exception.
#
# The use of the else clause is better than adding additional code to the try
# clause because it avoids accidentally catching an exception that wasn’t
# raised by the code being protected by the try … except statement.

print("--- The 'else' Clause ---")
sample_args = ["error.py", "non_existent_sample.txt"]

for arg in sample_args:
    try:
        f = open(arg, 'r', encoding='utf-8')
    except OSError:
        print(f"Cannot open '{arg}'")
    else:
        print(f"'{arg}' has {len(f.readlines())} lines")
        f.close()

print()

# -----------------------------------------------------------------------------
# Exceptions in Called Functions
# -----------------------------------------------------------------------------
# Exception handlers do not handle only exceptions that occur immediately in
# the try clause, but also those that occur inside functions that are called
# (even indirectly) in the try clause:

print("--- Catching Exceptions from Nested Functions ---")


def this_fails():
    return 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error from inside this_fails():', err)

print()


# =============================================================================
# 8.4. RAISING EXCEPTIONS
# =============================================================================
# The raise statement allows the programmer to force a specified exception to
# occur.
#
# The sole argument to raise indicates the exception to be raised. This must be
# either an exception instance or an exception class (a class that derives from
# BaseException, such as Exception or one of its subclasses). If an exception
# class is passed, it will be implicitly instantiated by calling its constructor
# with no arguments:
#
#   raise ValueError  # Shorthand for 'raise ValueError()'
#
# Re-raising Exceptions:
# ----------------------
# If you need to determine whether an exception was raised but don’t intend to
# handle it, a simpler form of the raise statement allows you to re-raise the
# exception:
#
#   try:
#       raise NameError('HiThere')
#   except NameError:
#       print('An exception flew by!')
#       raise

print("=" * 70)
print("8.4. RAISING AND RE-RAISING EXCEPTIONS")
print("=" * 70)

try:
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by! Re-raising...')
        raise
except NameError as caught_err:
    print(f"Caught re-raised exception in outer handler: {caught_err}")

print()


# =============================================================================
# 8.5. EXCEPTION CHAINING
# =============================================================================
# If an unhandled exception occurs inside an except section, it will have the
# exception being handled attached to it and included in the error message:
#
#   try:
#       open("database.sqlite")
#   except OSError:
#       raise RuntimeError("unable to handle error")
#
# Explicit Chaining ('raise ... from exc'):
# ----------------------------------------
# To indicate that an exception is a direct consequence of another, the raise
# statement allows an optional 'from' clause. This can be useful when you are
# transforming exceptions.
#
# Disabling Exception Chaining ('raise ... from None'):
# ---------------------------------------------------
# It also allows disabling automatic exception chaining using 'from None'.

print("=" * 70)
print("8.5. EXCEPTION CHAINING")
print("=" * 70)


def connect_database():
    raise ConnectionError("Connection to database server timed out.")


# 1. Explicit chaining using 'from'
print("--- 1. Explicit Chaining with 'from' ---")
try:
    try:
        connect_database()
    except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc
except RuntimeError as err:
    print(f"Caught exception: {err}")
    print(f"Direct cause (__cause__): {err.__cause__}")

print()

# 2. Suppressing chaining with 'from None'
print("--- 2. Suppressing Context with 'from None' ---")
try:
    try:
        open('database.sqlite')
    except OSError:
        raise RuntimeError("Clean error without underlying OS context") from None
except RuntimeError as err:
    print(f"Caught exception: {err}")
    print(f"Direct cause (__cause__): {err.__cause__} (chaining disabled)")

print()


# =============================================================================
# 8.6. USER-DEFINED EXCEPTIONS
# =============================================================================
# Programs may name their own exceptions by creating a new exception class
# (see Classes for more about Python classes). Exceptions should typically be
# derived from the Exception class, either directly or indirectly.
#
# Exception classes can be defined which do anything any other class can do,
# but are usually kept simple, often only offering a number of attributes that
# allow information about the error to be extracted by handlers for the exception.
#
# Most exceptions are defined with names that end in “Error”, similar to the
# naming of the standard exceptions.
#
# Many standard modules define their own exceptions to report errors that may
# occur in functions they define.

print("=" * 70)
print("8.6. USER-DEFINED EXCEPTIONS")
print("=" * 70)


class CustomApplicationError(Exception):
    """Base class for exceptions in this module."""
    pass


class TransitionError(CustomApplicationError):
    """Raised when an operation attempts a state transition that's not allowed."""
    def __init__(self, prev_state, next_state, message):
        self.prev_state = prev_state
        self.next_state = next_state
        self.message = message
        super().__init__(f"{message}: Cannot move from {prev_state} to {next_state}")


try:
    raise TransitionError("Pending", "Cancelled", "Invalid state transition")
except TransitionError as err:
    print(f"Caught user-defined exception: {err}")
    print(f"  -> Previous State: {err.prev_state}")
    print(f"  -> Target State  : {err.next_state}")

print()


# =============================================================================
# 8.7. DEFINING CLEAN-UP ACTIONS (finally)
# =============================================================================
# The try statement has another optional clause which is intended to define
# clean-up actions that must be executed under all circumstances.
#
# Key Points on 'finally':
# ------------------------
# 1. If a finally clause is present, it will execute as the last task before
#    the try statement completes.
# 2. The finally clause runs whether or not the try statement produces an exception.
# 3. If an exception occurs and is not handled by except, it is re-raised AFTER
#    the finally clause has been executed.
# 4. If the finally clause executes a break, continue, or return statement,
#    exceptions are not re-raised. (This can be confusing and is discouraged;
#    from Python 3.14 the compiler emits a SyntaxWarning for it, PEP 765).
# 5. In real world applications, the finally clause is useful for releasing
#    external resources (such as files or network connections), regardless of
#    whether the use of the resource was successful.

print("=" * 70)
print("8.7. DEFINING CLEAN-UP ACTIONS (try ... finally)")
print("=" * 70)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("  [divide] Division by zero!")
    else:
        print("  [divide] Result is", result)
    finally:
        print("  [divide] Executing finally clause (always runs)")


print("Test 1: divide(2, 1)")
divide(2, 1)

print("\nTest 2: divide(2, 0)")
divide(2, 0)

print("\nTest 3: divide('2', '1') [Unhandled TypeError caught by caller]")
try:
    divide("2", "1")
except TypeError as err:
    print(f"  [caller] Caught re-raised TypeError: {err}")

print()


# =============================================================================
# 8.8. PREDEFINED CLEAN-UP ACTIONS (with statement)
# =============================================================================
# Some objects define standard clean-up actions to be undertaken when the object
# is no longer needed, regardless of whether or not the operation using the object
# succeeded or failed.
#
# Example of suboptimal code:
#   for line in open("myfile.txt"):
#       print(line, end="")
# The problem with this code is that it leaves the file open for an indeterminate
# amount of time after this part of the code has finished executing.
#
# The with statement allows objects like files to be used in a way that ensures
# they are always cleaned up promptly and correctly:
#
#   with open("myfile.txt") as f:
#       for line in f:
#           print(line, end="")
#
# After the statement is executed, the file f is always closed, even if a
# problem was encountered while processing the lines.

print("=" * 70)
print("8.8. PREDEFINED CLEAN-UP ACTIONS (with STATEMENT)")
print("=" * 70)

# Creating and reading a temporary demo file with 'with':
temp_filename = "temp_cleanup_demo.txt"
with open(temp_filename, "w") as f:
    f.write("Line 1: Predefined cleanup demo\nLine 2: Automatically closed!\n")

with open(temp_filename, "r") as f:
    for line in f:
        print("  ", line.strip())

# Clean up temporary demonstration file
if os.path.exists(temp_filename):
    os.remove(temp_filename)

print("File was safely read and closed via context manager.")
print()


# =============================================================================
# 8.9. RAISING AND HANDLING MULTIPLE UNRELATED EXCEPTIONS (Python 3.11+)
# =============================================================================
# There are situations where it is necessary to report several exceptions that
# have occurred. This is often the case in concurrency frameworks, when several
# tasks may have failed in parallel, but there are also other use cases where
# it is desirable to continue execution and collect multiple errors rather
# than raise the first exception.
#
# The builtin ExceptionGroup wraps a list of exception instances so that they
# can be raised together. It is an exception itself, so it can be caught like
# any other exception.
#
# By using 'except*' instead of 'except', we can selectively handle only the
# exceptions in the group that match a certain type. In the following example,
# each except* clause extracts from the group exceptions of a certain type while
# letting all other exceptions propagate.

print("=" * 70)
print("8.9. MULTIPLE UNRELATED EXCEPTIONS (ExceptionGroup & except*)")
print("=" * 70)


def sample_grouped_tasks():
    excs = [OSError('disk read error'), SystemError('low-level subsystem error')]
    raise ExceptionGroup('Multiple background task failures occurred', excs)


# Catching an ExceptionGroup as a whole:
try:
    sample_grouped_tasks()
except Exception as e:
    print(f"Caught with regular except: {type(e).__name__} -> {e}")

print()

# Handling selectively using except*:
print("Selective handling with except*:")


def nested_group_example():
    raise ExceptionGroup(
        "group1",
        [
            OSError("File missing"),
            SystemError("Memory bus error"),
            ExceptionGroup(
                "group2",
                [
                    OSError("Network timeout"),
                    RecursionError("Maximum recursion depth exceeded")
                ]
            )
        ]
    )


try:
    try:
        nested_group_example()
    except* OSError as e:
        print(f"  -> Handled OSErrors: {e.exceptions}")
    except* SystemError as e:
        print(f"  -> Handled SystemErrors: {e.exceptions}")
except* RecursionError as e:
    print(f"  -> Outer handler caught unhandled RecursionError: {e.exceptions}")

print()

# -----------------------------------------------------------------------------
# Pattern for Accumulating Exceptions in Loops:
# -----------------------------------------------------------------------------
# excs = []
# for test in tests:
#     try:
#         test.run()
#     except Exception as e:
#         excs.append(e)
# if excs:
#     raise ExceptionGroup("Test Failures", excs)


# =============================================================================
# 8.10. ENRICHING EXCEPTIONS WITH NOTES (add_note() - Python 3.11+)
# =============================================================================
# When an exception is created in order to be raised, it is usually initialized
# with information that describes the error that has occurred. There are cases
# where it is useful to add information after the exception was caught.
#
# For this purpose, exceptions have a method add_note(note) that accepts a
# string and adds it to the exception’s notes list. The standard traceback
# rendering includes all notes, in the order they were added, after the exception.

print("=" * 70)
print("8.10. ENRICHING EXCEPTIONS WITH NOTES (add_note())")
print("=" * 70)

try:
    raise TypeError('Invalid configuration argument type')
except Exception as e:
    e.add_note('Note 1: Added while parsing config.yaml')
    e.add_note('Note 2: Value was expected to be an integer, got string.')
    print("Caught exception with notes:")
    print(f"  Exception: {e}")
    if hasattr(e, "__notes__"):
        for note in e.__notes__:
            print(f"  [Note] {note}")

print()

# Example: Adding notes to individual errors before grouping them:
print("Adding notes to individual errors within an ExceptionGroup:")


def failing_operation():
    raise OSError('Operation failed')


collected_exceptions = []
for iteration in range(3):
    try:
        failing_operation()
    except Exception as err:
        err.add_note(f"Encountered during batch run iteration #{iteration + 1}")
        collected_exceptions.append(err)

try:
    raise ExceptionGroup("Batch processing failures", collected_exceptions)
except ExceptionGroup as eg:
    print(f"Caught ExceptionGroup: {eg.message}")
    for idx, sub_err in enumerate(eg.exceptions, 1):
        print(f"  Error #{idx}: {sub_err}")
        if hasattr(sub_err, "__notes__"):
            for note in sub_err.__notes__:
                print(f"    -> {note}")

print("\n" + "=" * 70)
print("END OF CHAPTER 8: ALL ERRORS FIXED AND CONCEPTS DEMONSTRATED!")
print("=" * 70)
