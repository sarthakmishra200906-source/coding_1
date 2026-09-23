def sum (a):
    sum=0
    while a>0:
        digit=a%10
        sum+=digit
        a//=10
    return sum
a=int(input("Enter 1st number: "))
print("The sum of digits is: ",sum(a))
