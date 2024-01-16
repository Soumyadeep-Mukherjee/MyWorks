'''def distance(w1,w2):
    m="abcdefghijklmnopqrstuvwxyz"
    n1=len(w1)
    n2=len(w2)
    w1.lower()
    w2.lower()
    d=0
    if n1 != n2:
        return -1
    else:
        for i in range (n1):
            k=m.index(w1[i])-m.index(w2[i])
            d+= abs(k)
    return d
print(distance("dog","cat"))'''
# 17th Dec timmed assignment
#Q1
'''class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def print_info(self):
        print(self.name,self.marks,sep=":")
s= Student("Soumya",100)
s.print_info()'''
#Q3
'''import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self):
        return(math.sqrt((self.x**2)+(self.y**2)))
    def is_origin(self):
        if self.x==0 and self.y==0:
            return True
        else:
            return False
    def on_xaxis(self):
        if self.x==0:
            return True
        else:
            return False
    def on_yaxis(self):
        if self.y==0:
            return True
        else:
            return False
    def slope(self):
        return(self.y/self.x)
    def quadrant(self):
        if self.x <0 and self.y<0:
            return "third"
        elif self.x>0 and self.y>0:
            return "first"
        elif self.x<0 and self.y>0:
            return "Second"
        elif self.x>0 and self.y<0:
            return "Fourth"
        else:
            return "On axis or Origin"
p=Point(3,4)
print(p.distance())
print(p.is_origin())'''
#Q4
class Signal():
    def __init__(self,T):
        self.T=T
        v=0
        state="red"
    def sense(self,v_new):
        self.v=v_new
    def update(self):
        if self.v>self.T:
            self.state="green"
        elif self.v<self.T:
            self.state="red"
        else:
            pass
        return(self.state)
S=Signal(20)
S.sense(15)
S.update()
print(S.state)
#Q5
class vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_info(self):
        print((self.x,self.y))
    def scale(self,s):
        return([s*self.x,s*self.y])
    def reflect_about_X(self):
        return([self.x,-(self.y)])
    def reflect_about_Y(self):
        return([-(self.x),self.y])
    def add(self,vector(c,d)):
        f=self.x+vector.c
        g=self.y+vector.d
        return([f,g])
d= vector(3,4)
d.print_info()
print(d.reflect_about_X())
print(d.reflect_about_Y())
print(d.scale(3))
print(d.add(7,3))






