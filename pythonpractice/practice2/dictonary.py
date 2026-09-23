# ==========================================
# PYTHON DICTIONARIES ALL-IN-ONE PRACTICE
# ==========================================

# 1. Creation & Access
# Dictionaries store data in key-value pairs
print("1. Creation & Access:")
student = {"name": "Sarthak", "age": 19, "branch": "CSE"}
print("Student dict:", student)
print("Accessing via key:", student["name"])
print("Accessing via .get():", student.get("branch"))
print("-" * 40)


# 2. Modifying & Adding Elements
# You can add new keys or change existing values directly
print("2. Modifying & Adding:")
student["age"] = 20          # Updates existing value
student["college"] = "NIST"  # Adds a new key-value pair
print("After modification:", student)
print("-" * 40)


# 3. Removing Elements
# Use .pop() to remove a specific key, or del keyword
print("3. Removing Elements:")
removed_val = student.pop("age")  # Removes 'age' and returns its value
print(f"Removed age ({removed_val}). Dict now:", student)
print("-" * 40)


# 4. Dictionary Views (.keys(), .values(), .items())
print("4. Viewing Keys, Values, and Items:")
car = {"brand": "Toyota", "model": "Supra", "year": 2022}
print("Keys:", list(car.keys()))
print("Values:", list(car.values()))
print("Items (Pairs):", list(car.items()))
print("-" * 40)


# 5. Looping Through a Dictionary
print("5. Looping through a Dictionary:")
for key, value in car.items():
    print(f"Key: {key} --> Value: {value}")
print("-" * 40)


# 6. Checking if a Key Exists
print("6. Key Membership Testing:")
if "brand" in car:
    print("'brand' exists in the dictionary!")
print("-" * 40)


# 7. Merging Dictionaries
print("7. Merging Dictionaries:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)  # Merges dict2 into dict1
print("Merged dict:", dict1)
print("-" * 40)


# 8. Practical Trick: Frequency Counter (Super Important for Exams!)
# Counting how many times each character appears in a string using a dictionary
print("8. Frequency Counter Application:")
text = "programming"
freq = {}
for char in text:
    # .get(char, 0) gets current count or 0 if it doesn't exist yet
    freq[char] = freq.get(char, 0) + 1
print(f"Character frequencies in '{text}':", freq)
print("-" * 40)


# 9. Nested Dictionaries
print("9. Nested Dictionaries:")
classroom = {
    "student1": {"name": "Alice", "score": 85},
    "student2": {"name": "Bob", "score": 90}
}
print("Classroom data:", classroom)
print("Access nested value (Bob's score):", classroom["student2"]["score"])
print("=" * 40)