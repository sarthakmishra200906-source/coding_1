with open("file.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)
    
    # Split content into a list of words and make them lowercase for a safe search
    words = content.lower().split()
    
    # Check if the word exists in the list directly
    if "print" in words:
        print("Word is present!")
    else:
        print("Word is not present.")