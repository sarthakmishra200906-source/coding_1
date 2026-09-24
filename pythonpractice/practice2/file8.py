# First, let's create a dummy input file with some numbers for testing
with open("numbers.txt", "w") as f:
    f.write("10\n15\n22\n37\n40\n5\n")

# Now, read and split the numbers into even and odd files
with open("numbers.txt", "r") as infile, \
     open("evens.txt", "w") as evenfile, \
     open("odds.txt", "w") as oddfile:
    
    for line in infile:
        # Strip newline characters and convert the string line to an integer
        num = int(line.strip())
        
        # Check if even or odd, and write to the respective file
        if num % 2 == 0:
            evenfile.write(str(num) + "\n")
        else:
            oddfile.write(str(num) + "\n")

print("Even and odd numbers have been successfully split into 'evens.txt' and 'odds.txt'!")