n= input().split(",")
m= input().split(",")
common=[]
k=[]
if len(n)!= len(m):
    print("Input not complete")
for i in range(len(m)):
    for j in range(len(m)):
        if n[i]==n[j]:
            continue
        elif m[i]==m[j]:
            k=[]
            if n[i]<n[j]:
                k.append(n[i])
                k.append(n[j])
            else:
                k.append(n[j])
                k.append(n[i])
        if k in common:
            continue
        elif k== []:
            continue
        else:
            common.append(k)

print(common)