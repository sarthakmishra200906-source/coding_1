def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
a=int(input("Enter 1st number: "))
orignal=a
sum=0
while a>0:
    digit=a%10
    sum+=factorial(digit)
    a//=10
if sum==orignal:
    print("The number is strong")
else:
    print("The number is not strong")


   