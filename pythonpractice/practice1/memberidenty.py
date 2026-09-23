a=input("Enter a value: ")
b= input("enter a key value: ")
if __name__=="__main__":
    switch=input("Enter 1 for identy and 2 for membership: ")
    if switch=="1":
        switch1=input("Enter 1 for is and 2 for not is: ")
        if switch1=="1":
           print(a is b)# its used to check if two variables point to the same object in memory. It returns True if they do, and False otherwise.
        elif switch1=="2":
              print(a is not b)# its used to check if two variables do not point to the same object in memory. It returns True if they do not, and False otherwise.
    if switch=="2":
        switch2=input("Enter 1 for in and 2 for not in: ")
        if switch2=="1":
            print(b in a)# its used to check if a value is present in a sequence (like a list, tuple, or string). It returns True if the value is found, and False otherwise.
        elif switch2=="2":
            print(b not in a)# its used to check if a value is not present in a sequence. It returns True if the value is not found, and False otherwise.
