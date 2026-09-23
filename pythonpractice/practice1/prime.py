a=int(input("Enter 1st number: "))
for i in range(2,a):
    if a%i==0:
        print("The number is not prime")
        break
else:
    print("The number is prime")