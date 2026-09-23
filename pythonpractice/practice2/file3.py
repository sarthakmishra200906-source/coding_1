with open ("file.txt", "r") as f:
    content = f.read()
    result=content.split()
    print(len(result))
