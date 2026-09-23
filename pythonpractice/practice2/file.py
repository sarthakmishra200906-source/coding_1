with open("file.txt", "w") as f:
    f.write("Hello, World!")
   
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

with open("file.txt", "a") as f:
    f.write("\n welcom to python")
   
    with open("file.txt", "r") as f:
        content = f.read()
        print(content)

