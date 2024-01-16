a=[]
n1=int(input("Enter1"))
n2=(int(input("Enter2 ")))
n3=(int(input("Enter3")))
n4=(int(input("Enter 4")))
l=[n1,n2,n3,n4]
min=n1
while len(l)!=0:
    for i in range(len(l)):
        if l[i]<min:
            min=l[i]
    a.append(min)
    l.remove(min)
    if len(l)!=0:
        min=l[0]
for j in range(len(a)):
    if i!= (len(a)-1):
        print(a[j],end=" ")
    else:
        print(a[j])
