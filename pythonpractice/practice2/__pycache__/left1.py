# ==============================================================================
# PYTHON ADVANCED TOOLS: LAMBDA, MAP, FILTER, *ARGS, **KWARGS
# ==============================================================================

print("=== 1. LAMBDA FUNCTIONS ===")
# Regular function vs Lambda function
# Regular: def square(x): return x * x
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum using lambda:", add(3, 7))
print("-" * 40)


print("=== 2. MAP FUNCTION ===")
# map() applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]

# Double every number in the list using map and a lambda function
doubled = list(map(lambda x: x * 2, numbers))
print("Original numbers:", numbers)
print("Doubled numbers using map():", doubled)
print("-" * 40)


print("=== 3. FILTER FUNCTION ===")
# filter() keeps only the items that return True for the condition
numbers = [10, 15, 20, 25, 30, 35]

# Keep only even numbers using filter and lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Original numbers:", numbers)
print("Filtered even numbers using filter():", evens)
print("-" * 40)


print("=== 4. *ARGS (Arbitrary Positional Arguments) ===")
# *args allows you to pass any number of positional arguments to a function
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of (1, 2, 3):", sum_all(1, 2, 3))
print("Sum of (10, 20, 30, 40, 50):", sum_all(10, 20, 30, 40, 50))
print("-" * 40)


print("=== 5. **KWARGS (Arbitrary Keyword Arguments) ===")
# **kwargs allows you to pass any number of keyword arguments (key=value)
def print_student_details(**kwargs):
    print("Printing student profile data:")
    for key, value in kwargs.items():
        print(f"  {key} -> {value}")

print_student_details(name="Sarthak", branch="CSE", semester=2, score=92)
print("-" * 40)


print("=== 6. COMBINED: *ARGS AND **KWARGS TOGETHER ===")
# You can use both in a single function! Order must be: standard args, *args, **kwargs
def universal_logger(task_name, *args, **kwargs):
    print(f"Task: {task_name}")
    print(f"Positional tags (*args): {args}")
    print(f"Keyword metadata (**kwargs): {kwargs}")

universal_logger(
    "Data Processing", 
    "priority_high", "python_script", 
    author="Sarthak", version=1.2
)
print("=" * 40)
# 1. Define a regular function
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]

# 2. Apply map() - pass the function and the list
result_iterator = map(square, numbers)

# 3. Convert the map object to a list to view it
squared_list = list(result_iterator)

print("Original:", numbers)
print("Squared: ", squared_list)

fruits = ["apple", "banana", "cherry"]

# start=1 makes it count from 1 instead of 0
print("--- Enumerate Example ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")

    names = ["Sarthak", "Rahul", "Priya"]
scores = [92, 85, 95]

print("\n--- Zip Example ---")
for name, score in zip(names, scores):
    print(f"{name} scored {score} marks.")