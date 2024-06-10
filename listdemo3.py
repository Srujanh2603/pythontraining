#swapping elements at given positions
def swap(l,p1,p2):
    temp=l[p1]
    l[p1]=l[p2]
    l[p2]=temp
    return l

l=[10,20,30,40,50]
print(l)
p1,p2=1,3
print(swap(l,p1,p2))