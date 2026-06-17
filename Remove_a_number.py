n=int(input("Enter a number:"))
r=int(input("Enter a value to remove:"))
s=0
b=1
while(n):
  a=n%10
  if(a!=r):
    s=s+a*b
    b=b*10
  n=n//10
print(s)
