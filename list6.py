#wap to demonstrate list intersection and union
def union(l1,l2):
    l3=sorted(list(set(l1)|set(l2)))
    return l3

def intersection(l1,l2):
    l4=sorted(list(set(l1)&set(l2)))
    return l4

l1=[10,20,30,40,50,60]
l2=[10,20,60,80]
print(union(l1,l2))
print(intersection(l1,l2))

