# ==========================================
# PYTHON CLASSES & OBJECTS PRACTICE SCRIPT
# ==========================================

# 1. Defining a Class
class Student:
    # The Constructor method (__init__) initializes object attributes
    def __init__(self, name, roll_no, marks, rank):
        self.name = name        # Instance variable for name
        self.roll_no = roll_no  # Instance variable for roll number
        self.marks = marks      # Instance variable for marks
        self.rank = rank        # Instance variable for rank

    # 2. Defining a Method (An action the object can perform)
    def display_info(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Rank: {self.rank}")

    # 3. Another Method to check pass/fail status
    def check_result(self):
        if self.marks >= 40 or self.rank <= 100:
            return "Passed"
        else:
            return "Failed"


# ==========================================
# CREATING OBJECTS (INSTANTIATION)
# ==========================================

print("1. Creating and using student objects:")

# Creating object 1
student1 = Student("Sarthak", 101, 85, 10)
# Creating object 2
student2 = Student("Rahul", 102, 35, 50)

# Accessing attributes directly using dot notation (.)
print(f"Direct attribute access -> Name: {student1.name}, Marks: {student1.marks}")

# Calling class methods on objects
print("\nCalling methods:")
student1.display_info()
print(f"Status: {student1.check_result()}")

print("-" * 40)
student2.display_info()
print(f"Status: {student2.check_result()}")
print("=" * 40)