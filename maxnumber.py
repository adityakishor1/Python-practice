l=[]
n=int(input("Enter length of list:"))
for i in range(n):
  val=int(input("Enter numbers:"))
  l.append(val)
print(l)	
max=l[0]
for i in range(n):
 if l[i]>max:
  max=l[i]
print("max number=",max)	
