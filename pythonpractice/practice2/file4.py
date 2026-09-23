with open("file.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)
    
    # Split content into words to count total words later
    words = content.split()
    
    vowels = 0
    consonants = 0
    
    # Loop through each character in the file content
    for char in content:
        # Check if the character is an alphabet letter (ignores spaces, numbers, punctuation)
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
                
    print(f"Total number of vowels in file.txt: {vowels}")
    print(f"Total number of consonants in file.txt: {consonants}")
    print(f"Total number of words in file.txt: {len(words)}")