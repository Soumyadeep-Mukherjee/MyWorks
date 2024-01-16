import numpy as n 
x=[[1,0,-1],[2,3,4],[5,6,7]]
y=[[[1,2],[2,3],[3,4]],[[4,4],[11,13],[45,60]]]
a= n.array(x)
b=n.array(y)
l=a.T # Gives transpose of the array 
#print(l)
a.flat # this gives an iterator ove the array
'''for i in a.flat:
    print(i)
print(a.ndim) #give the dimmension 
print(a.size) # gives the number of elements
print(b.ndim) 
print(b.size)
print(a.nbytes)# gives the number of bytes consumed by one element
print(b.nbytes)'''
print(a.argmin()) # gives index of max after flattening the array
print(b.argmin()) # gives min in same way
print(b.argmax())
print(a.argsort()) #Gives the list of ascending order index run it and check
print(a.argmax(axis=0)) # run it and check , if prob reffer harry's video at time 40- 42 min check
print(b.argmax(axis=1))
print(b.argmax(axis=0))
