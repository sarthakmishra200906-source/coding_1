"""
================================================================================
   CLASS VARIABLES VS INSTANCE VARIABLES - THEORY & PRACTICAL REVISION GUIDE
================================================================================
This script is designed to be:
  1. A THOROUGH STUDY NOTE: Class namespace vs Instance namespace, attribute shadowing.
  2. AN EXECUTABLE LAB: Run it in your terminal to see live demonstrations of
     memory sharing, shadowing pitfalls, and attribute resolution!

Command to run:
  python obj1.py
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
# CORE THEORY: CLASS VARIABLES VS INSTANCE VARIABLES
# ==============================================================================
"""
THEORY CONCEPTS:
1. Class Variables (Static Attributes):
   - Defined directly within the class body (outside any method).
   - SHARED by all instances of the class.
   - Stored in the Class's namespace dictionary (`Car.__dict__`).
   - If a class variable is modified via `Car.variable = new_value`, the change
     is reflected across ALL existing and future instances (unless shadowed).

2. Instance Variables:
   - Defined inside methods (most commonly inside `__init__`) using `self.var`.
   - UNIQUE to each individual object.
   - Stored in the Instance's namespace dictionary (`car1.__dict__`).

3. The "Shadowing" Trap (Huge Exam Gotcha):
   - If you write `car1.brand = "Audi"`, you do NOT change the class variable!
   - Instead, Python creates a BRAND NEW instance variable on `car1` named `brand`,
     which "shadows" (hides) the class variable for `car1` only.
   - `car2.brand` and `Car.brand` remain completely unaffected!
"""


# ==============================================================================
# THE CAR CLASS IMPLEMENTATION
# ==============================================================================
class Car:
    # CLASS VARIABLES (Shared across all cars)
    wheels = 4
    default_manufacturer = "BMW"
    manufacturing_year = 2024

    def __init__(self, model: str, color: str, price: float):
        # INSTANCE VARIABLES (Specific to this exact car)
        self.model = model
        self.color = color
        self.price = price

    def display_specs(self, car_id: str):
        print(f"[{car_id}] {self.default_manufacturer} {self.model} ({self.color}) - ${self.price:,.2f} | Wheels: {self.wheels}")


# ==============================================================================
# DEMONSTRATION 1: ACCESSING CLASS VS INSTANCE ATTRIBUTES
# ==============================================================================
def demo_basic_access():
    banner("Section 1: Accessing Class and Instance Attributes", "Shared vs Unique Memory")

    car1 = Car(model="X5", color="Black", price=65000.0)
    car2 = Car(model="M3", color="Alpine White", price=78000.0)

    sub_heading("Specs of Two Distinct Cars")
    car1.display_specs("Car 1")
    car2.display_specs("Car 2")

    sub_heading("Direct Namespace Inspection (__dict__)")
    print(f"car1.__dict__ (Only holds instance variables):")
    print(f"  {car1.__dict__}")
    print(f"Notice: 'wheels' and 'default_manufacturer' are NOT inside car1.__dict__!")
    print(f"They live in Car.__dict__ (the class namespace).")


# ==============================================================================
# DEMONSTRATION 2: THE SHADOWING PITFALL (MUST-KNOW FOR EXAMS)
# ==============================================================================
def demo_shadowing_trap():
    banner("Section 2: The Shadowing Pitfall", "Modifying via Instance vs via Class")

    car1 = Car("X7", "Carbon Black", 90000.0)
    car2 = Car("i4", "Mineral Blue", 55000.0)

    print("Initial State:")
    print(f"  Car.default_manufacturer:  {Car.default_manufacturer}")
    print(f"  car1.default_manufacturer: {car1.default_manufacturer}")
    print(f"  car2.default_manufacturer: {car2.default_manufacturer}")

    sub_heading("Case A: Modifying via instance (car1.default_manufacturer = 'Mercedes')")
    car1.default_manufacturer = "Mercedes"

    print("After car1 modification:")
    print(f"  car1.default_manufacturer: {car1.default_manufacturer}  <-- Shadowed! Created instance variable")
    print(f"  car2.default_manufacturer: {car2.default_manufacturer}  <-- Still BMW!")
    print(f"  Car.default_manufacturer:  {Car.default_manufacturer}  <-- Still BMW!")

    print(f"\nInspect car1.__dict__ after assignment:")
    print(f"  {car1.__dict__}")
    print(">> Notice: 'default_manufacturer' is now an instance attribute inside car1!")

    sub_heading("Case B: Modifying properly via Class (Car.default_manufacturer = 'Porsche')")
    Car.default_manufacturer = "Porsche"

    print("After Car class modification:")
    print(f"  Car.default_manufacturer:  {Car.default_manufacturer}")
    print(f"  car2.default_manufacturer: {car2.default_manufacturer}  <-- Changed to Porsche (reads from class)")
    print(f"  car1.default_manufacturer: {car1.default_manufacturer}  <-- Still Mercedes (shadowing overrides class)")


# ==============================================================================
# DEMONSTRATION 3: MUTABLE CLASS VARIABLES (DANGEROUS GOTCHA!)
# ==============================================================================
class Dealership:
    # DANGER: Mutable class variable (shared list)
    shared_inventory = []

    def __init__(self, branch_name: str):
        self.branch_name = branch_name
        # SAFE: Instance-specific list
        self.local_inventory = []


def demo_mutable_class_variables():
    banner("Section 3: Mutable Class Variables Gotcha", "Why Lists/Dicts as Class Variables are Dangerous")

    branch_delhi = Dealership("Delhi Branch")
    branch_mumbai = Dealership("Mumbai Branch")

    # Appending to shared list via one instance affects ALL instances!
    branch_delhi.shared_inventory.append("Sedan")

    print(f"Delhi added 'Sedan' to shared_inventory.")
    print(f"Delhi shared_inventory:  {branch_delhi.shared_inventory}")
    print(f"Mumbai shared_inventory: {branch_mumbai.shared_inventory}  <-- ALSO contains 'Sedan'!")

    # Safe: using instance variable
    branch_delhi.local_inventory.append("SUV")
    print(f"\nDelhi local_inventory:   {branch_delhi.local_inventory}")
    print(f"Mumbai local_inventory:  {branch_mumbai.local_inventory}  <-- Clean and independent!")
    print(">> RULE: Always initialize mutable containers (lists, dicts) inside __init__!")


# ==============================================================================
# SUMMARY TABLE & QUICK REVISION CHEAT SHEET
# ==============================================================================
def print_cheat_sheet():
    print("\n" + "=" * 80)
    print("           CLASS VS INSTANCE VARIABLES QUICK REVISION CHEAT SHEET")
    print("=" * 80)
    print(f"{'Feature':<22} | {'Class Variable':<28} | {'Instance Variable':<24}")
    print("-" * 80)
    print(f"{'Where defined':<22} | {'Inside class, outside methods':<28} | {'Inside __init__ with self':<24}")
    print(f"{'Memory':<22} | {'Single copy in Class.__dict__':<28} | {'Copy per object in obj.__dict__':<24}")
    print(f"{'Access syntax':<22} | {'ClassName.var or obj.var':<28} | {'self.var or obj.var':<24}")
    print(f"{'Modification':<22} | {'ClassName.var = new_val':<28} | {'obj.var = new_val':<24}")
    print(f"{'Shadowing':<22} | {'Hides class var if assigned on obj':<28} | {'N/A':<24}")
    print("=" * 80)
    print("Class vs Instance Variables Masterclass completed successfully!\n")


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "#" * 80)
    print("#  CLASS VS INSTANCE VARIABLES MASTERCLASS - THEORY & LAB")
    print("#" * 80)

    demo_basic_access()
    demo_shadowing_trap()
    demo_mutable_class_variables()
    print_cheat_sheet()
