import numpy as n 
l=[[3,4,5],[5,6,7]] #2x3
a=n.array(l)
k=[[4,5,6],[7,8,9],[10,11,12]]
b= n.array(k)
f= [[12,13,4],[2,98,70],[90,4,5]]
c= n.array(f)
o= c+b
print(o)
x=b*b
print(x)
print(n.sqrt(b))
print(a.min)
print(a.max)
print(n.where(c>15))
print(n.nonzero(a)) # see both the list inside the tuple one element from one list and anothe from another list gives the index where the is non zero element
print(n.count_nonzero(a))