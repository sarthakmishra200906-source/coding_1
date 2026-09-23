# Take a string input from the user
a = input("Enter a string: ")

# 1. Reverse the entire string using slicing [start:end:step] with a step of -1
print("The string in reverse order is:", a[::-1])


# 2. Reverse each word in the string individually
# .split() breaks the sentence into a list of words based on spaces
r = a.split()
for i in r:
    # Print each word reversed, keeping them on the same line with end=" "
    print(i[::-1], end=" ")
print()  # Print a new line after the word-reversal loop finishes


# 3. Count total number of vowels and consonants
vowels = 0
consonants = 0

if a:
    for i in a:
        # Check if the character (converted to lowercase) is a vowel
        if i.lower() in "aeiou":
            vowels += 1

    # Total characters minus vowels gives consonants
    consonants = len(a) - vowels

    print("Total number of vowels in the string:", vowels)
    print("Total number of consonants in the string:", consonants)


# 4. Find the first non-repeating character in the user's input string
found = False

for i in a:
    # .count(i) checks how many times the character appears in the whole string
    if a.count(i) == 1:
        print("The first non-repeating character in the string is:", i)
        found = True
        break  # Stop checking as soon as we find the first unique character

# If the loop finished and 'found' is still False, no unique character exists
if not found:
    print("No non-repeating character found in the string.")


# 5. Strip leading and trailing whitespace
s = a.strip()  # Removes extra spaces from the very beginning and very end
print("The string after removing leading and trailing whitespace is:", s)


# 6. Count the frequency of each unique character (Fixed to prevent duplicates!)
seen = set()  # To track characters we've already counted
for i in s:
    if i not in seen:
        seen.add(i)
        print(f"The frequency of '{i}' in the string is: {s.count(i)}")


# 7. Toggle case: Convert lowercase to uppercase and uppercase to lowercase
print("Toggled case string: ", end="")
for i in s:
    if i.islower():
        print(i.upper(), end="")  # If it's lowercase, print it as uppercase
    elif i.isupper():
        print(i.lower(), end="")  # If it's uppercase, print it as lowercase
    else:
        print(i, end="")          # Keep spaces or symbols as they are
print()  # Print a final new line


# 8. Find the length of the longest word in the string
result = 0
for i in a.split():
    if len(i) > result:
        result = len(i)
print("The length of the longest word in the string is:", result)


# 9. String Compression: Perform basic compression (e.g., "aabcccccaaa" -> "a2b1c5a3")
def compress_string(text):
    if not text:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(len(text)):
        # If the current character matches the next one, increment count
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            # Otherwise, append the character and its count
            compressed.append(text[i] + str(count))
            count = 1  # Reset count for the next character
            
    return "".join(compressed)

print("Compressed string:", compress_string(s))