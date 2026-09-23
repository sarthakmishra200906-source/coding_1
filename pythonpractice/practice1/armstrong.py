def cube(a):
    return a*a*a
sum=0
a=int(input("Enter 1st number: "))
orignal=a
while a>0:
    digit=a%10
    sum+=cube(digit)
    a//=10
if sum==orignal:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
    