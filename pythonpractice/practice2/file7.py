# Simulating taking input (in a real scenario, you can put this inside a loop or use input())
# Let's write a few entries to a mini-CSV file
filename = "students.csv"

# Using 'a' (append) mode so previous entries aren't erased when adding new data
with open(filename, "a") as f:
    # Example student data
    students_data = [
        ("Sarthak", 92),
        ("Rahul", 85),
        ("Priya", 95)
    ]
    
    for name, marks in students_data:
        # Format as Name,Marks and write with a newline
        f.write(f"{name},{marks}\n")

print("Student records successfully appended to 'students.csv'!")

# Let's read it back to verify the CSV format
print("\n--- Reading 'students.csv' ---")
with open(filename, "r") as f:
    print(f.read())