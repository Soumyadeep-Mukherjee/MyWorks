n= input("Enter the string:")
c=True
for i in range(len(n)):
    if n[i]!=n[(-(i+1))]:
         c=False
if c:
     print("Yes boy it is a pallindrome")
else:
     print("oops! no ")

