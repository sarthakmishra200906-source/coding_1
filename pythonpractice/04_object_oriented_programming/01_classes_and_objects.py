"""
================================================================================
     PYTHON CLASSES & OBJECTS - COMPLETE THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Class vs Object, `self`, methods, dunder representations.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     instantiation, instance/class/static methods, and string formatting!

Command to run:
  python obj.py
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
# CORE THEORY: WHAT ARE CLASSES AND OBJECTS IN PYTHON?
# ==============================================================================
"""
THEORY CONCEPTS:
1. Class (The Blueprint):
   A user-defined prototype or blueprint from which individual objects are created.
   It defines a set of attributes (data) and methods (behavior) that characterize
   any object instantiated from it.

2. Object / Instance (The Real-World Entity):
   A concrete instance of a class that exists in memory. If 'Student' is the class,
   'Sarthak' (with Roll No 101, Marks 95) is a specific object.

3. The `__init__()` Constructor:
   A special lifecycle method automatically invoked when a new object is created.
   Its primary role is to initialize the instance variables of the object.

4. The `self` Parameter:
   - `self` represents the specific instance of the class currently calling the method.
   - When you write `student1.display()`, Python converts it internally into:
     `Student.display(student1)`.
   - `self` binds attributes to individual objects so that student1's data does
     not overwrite student2's data!

5. The Three Method Types:
   - Instance Method: Takes `self`. Can read and modify instance state.
   - Class Method (@classmethod): Takes `cls`. Works with the class state (not instance).
   - Static Method (@staticmethod): Takes neither `self` nor `cls`. Pure utility function.
"""


# ==============================================================================
# STUDENT CLASS DEFINITION
# ==============================================================================
class Student:
    """Comprehensive Student class modeling academic attributes and methods."""

    # CLASS VARIABLE (Shared by every student instance)
    university_name = "National Institute of Science & Technology"
    total_students_enrolled = 0

    def __init__(self, name: str, roll_no: int, marks: float):
        # INSTANCE VARIABLES (Unique to each individual student)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

        # Increment class counter every time an object is initialized
        Student.total_students_enrolled += 1

    # 1. INSTANCE METHOD: Needs `self` to operate on individual student data
    def calculate_grade(self) -> str:
        if self.marks >= 90:
            return "A+ (Outstanding)"
        elif self.marks >= 75:
            return "A (Very Good)"
        elif self.marks >= 50:
            return "B (Average)"
        elif self.marks >= 40:
            return "C (Pass)"
        else:
            return "F (Fail)"

    # 2. INSTANCE METHOD: Generates a complete report card
    def get_report(self) -> str:
        return f"Roll {self.roll_no}: {self.name:<12} | Marks: {self.marks:>5.1f} | Grade: {self.calculate_grade()}"

    # 3. CLASS METHOD (@classmethod): Operates on the class level (`cls`)
    @classmethod
    def get_enrollment_stats(cls) -> str:
        return f"Total Enrolled Students across {cls.university_name}: {cls.total_students_enrolled}"

    # 4. STATIC METHOD (@staticmethod): Utility method with no access to self or cls
    @staticmethod
    def is_passing_mark(mark: float) -> bool:
        """Determines if a mark qualifies for passing without needing an instance."""
        return mark >= 40.0

    # 5. DUNDER METHOD __str__: User-friendly string representation (used by print(obj))
    def __str__(self) -> str:
        return f"Student(Name='{self.name}', Roll={self.roll_no}, Marks={self.marks})"

    # 6. DUNDER METHOD __repr__: Unambiguous developer representation
    def __repr__(self) -> str:
        return f"Student('{self.name}', {self.roll_no}, {self.marks})"


# ==============================================================================
# DEMONSTRATION 1: CREATING OBJECTS (INSTANTIATION)
# ==============================================================================
def demo_instantiation():
    banner("Section 1: Instantiation & Attribute Binding", "Creating Distinct Objects in Memory")

    # Creating two distinct student objects
    s1 = Student("Sarthak", 101, 94.5)
    s2 = Student("Rahul", 102, 68.0)
    s3 = Student("Priya", 103, 38.0)

    print(f"Object 1: {s1}")
    print(f"Object 2: {s2}")
    print(f"Object 3: {s3}")

    sub_heading("Verifying Unique Memory Addresses")
    print(f"Memory id(s1): {hex(id(s1))}")
    print(f"Memory id(s2): {hex(id(s2))}")
    print(">> Notice: Each object resides in a distinct memory location with its own independent state.")


# ==============================================================================
# DEMONSTRATION 2: INSTANCE METHODS & BEHAVIOR
# ==============================================================================
def demo_instance_methods():
    banner("Section 2: Calling Instance Methods", "How self routes execution to the right instance")

    s1 = Student("Sarthak", 101, 94.5)
    s2 = Student("Rahul", 102, 68.0)
    s3 = Student("Priya", 103, 38.0)

    sub_heading("Report Cards via Instance Methods")
    print(s1.get_report())
    print(s2.get_report())
    print(s3.get_report())


# ==============================================================================
# DEMONSTRATION 3: CLASS METHODS VS STATIC METHODS
# ==============================================================================
def demo_class_and_static_methods():
    banner("Section 3: Class Methods vs Static Methods", "@classmethod (cls) vs @staticmethod")

    sub_heading("Class Method (@classmethod) in Action")
    print(Student.get_enrollment_stats())

    sub_heading("Static Method (@staticmethod) in Action")
    test_scores = [35.0, 42.5, 89.0]
    for score in test_scores:
        status = "PASSED" if Student.is_passing_mark(score) else "FAILED"
        print(f"  Score {score:>4.1f}: {status}")


# ==============================================================================
# DEMONSTRATION 4: DUNDER METHODS (__str__ & __repr__)
# ==============================================================================
def demo_dunder_methods():
    banner("Section 4: Magic / Dunder Methods", "__str__ for End-Users vs __repr__ for Developers")

    s = Student("Aarav", 105, 88.0)

    print(f"str(s)  -> Used by print(): {str(s)}")
    print(f"repr(s) -> Used in debugger: {repr(s)}")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("                 CLASSES & OBJECTS QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Concept / Keyword':<22} | {'Role':<32} | {'Key Syntax / Note':<22}")
    print("-" * 80)
    print(f"{'class':<22} | {'Blueprint defining state & logic':<32} | {'class ClassName:':<22}")
    print(f"{'object':<22} | {'Concrete instance in memory':<32} | {'obj = ClassName()':<22}")
    print(f"{'__init__':<22} | {'Constructor to initialize data':<32} | {'def __init__(self, ...):':<22}")
    print(f"{'self':<22} | {'Pointer to current instance':<32} | {'First parameter of methods':<22}")
    print(f"{'Instance Variable':<22} | {'Unique data per object':<32} | {'self.variable_name':<22}")
    print(f"{'Class Variable':<22} | {'Shared data across all objects':<32} | {'ClassName.variable_name':<22}")
    print(f"{'@classmethod':<22} | {'Operates on class via cls':<32} | {'def func(cls, ...):':<22}")
    print(f"{'@staticmethod':<22} | {'Standalone utility function':<32} | {'def func(...): (No self)':<22}")
    print(f"{'__str__':<22} | {'Readable string for print()':<32} | {'def __str__(self):':<22}")
    print("=" * 80)
    print("Classes & Objects Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  PYTHON CLASSES & OBJECTS MASTERCLASS - THEORY & PRACTICAL LAB")
    print("#" * 80)

    demo_instantiation()
    demo_instance_methods()
    demo_class_and_static_methods()
    demo_dunder_methods()
    print_cheat_sheet()