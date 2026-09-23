with open("file.py", "r") as f:
    # .readlines() reads ALL lines and returns them as a list of strings
    content1 = f.readlines()
    
    # Loop through each line and print it
    for line in content1:
        print(line.strip())  # .strip() removes extra newline spacing
        
    # Find the total number of lines just by checking the length of the list!
    total_lines = len(content1)
    
    print(f"Total number of lines in file.py: {total_lines}")