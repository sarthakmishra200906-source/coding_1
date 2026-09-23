def palandrom():
    a=input("Enter a string: ")
    if a==a[::-1]:
        print("The string is palandrom")
    else:
        print("The string is not palandrom")
def intpalandrom():
    a=int(input("Enter a number: "))
    if str(a)==str(a)[::-1]:
        print("The number is palandrom")
    else:
        print("The number is not palandrom")
while True:
    switch=input("Enter 1 for string and 2 for number or 3 to quit: ")
    if switch=="1":
        palandrom()
    elif switch=="2":
        intpalandrom()  
    elif switch=="3":
        break
    else:
        print("Invalid input")


