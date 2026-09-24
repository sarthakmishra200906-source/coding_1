# Read all lines from the source file into a list
with open("file.py", "r") as f:
    lines = f.readlines()

# Reverse the list of lines using slicing [::-1]
reversed_lines = lines[::-1]

# Write the reversed lines into a new file
with open("reversed_practice.txt", "w") as f:
    f.writelines(reversed_lines)

print("File lines have been reversed and saved to 'reversed_practice.txt'!")