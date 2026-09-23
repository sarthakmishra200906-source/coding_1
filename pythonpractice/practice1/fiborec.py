def fibonaccy(n):
    if n<=1:
        return n
    else:
        return(fibonaccy(n-1)+fibonaccy(n-2))
a=int(input("Enter the number of terms: "))
if a<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(a):
        print(fibonaccy(i)) 
