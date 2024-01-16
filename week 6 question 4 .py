def  two_level_sort(scores):
    l=[]
    c=[]
   
   
    while (len(scores)>0):
        a=scores[0][0]
        d=scores[0]
        for i in range(len(scores)):
            if scores[i][0]<a:
                a=scores[i][0]
                d=scores[i]
        l.append(d)
        scores.remove(d)
        
    while(len(l)>0):
        b=l[0][1]
        e=l[0]
        for j in range(len(l)):
            if l[j][1]<b:
                b=l[j][1]
                e=l[j]
        c.append(e)
        l.remove(e)
        
    return c
print(two_level_sort([('Harish', 80), ('Aparna', 90), ('Harshita', 80)]))


    
        
