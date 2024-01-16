n=int(input())
p=int(input())
a=[]
b=[]
C=False
if (n==1 or p==1) :
    print("N")
else:
    for i in range(2,n+1):
        if n%i==0:
            a.append(i)
        else:
            pass
    for j in range(2,p+1):
        if p%j==0:
            b.append(j)
        else:
            pass
    for i in range (len(a)):
        for j in range (len(b)):
            if a[i]==b[j]:
                C= True
                break
            else:
                pass
    if C:
        print("N")
    else:
        print("damn yes")