def reverce_string(string):
    a=input("Enter a string: ")
    print("The reverce of the string is: ",a[::-1])
def reverse_number():
    a=int(input("Enter a number: "))
    print("The reverce of the number is: ",str(a)[::-1])    
if __name__=="__main__":
    switch=input("Enter 1 for string and 2 for number: ")
    if switch=="1":
        reverce_string()
    elif switch=="2":
        reverse_number()  
    else:
        print("Invalid input")