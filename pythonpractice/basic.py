n=list(map(int,input("enter value seprated by space: ").split()))
pos=int(input("enter position to insert value: "))
val=int(input("enter value to insert: "))
n.insert(pos,val)
print(n)
s=set(n)
print("out of unique values: ",s)
#print value without  , and curly bracket in terminal
print("unique values are: ",*s)
print("largest value is: ",max(s))

s.remove(max(s))
print("second largest value is: ",max(s))



