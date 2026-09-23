p=int(input("Enter princpal amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time: "))
si=(p*r*t)/100
print("The simple interest is: ",si)
compound_interest=p*(1+r/100)**t
print("The compound interest is: ",compound_interest)
