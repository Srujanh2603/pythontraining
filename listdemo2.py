#WAP to swap 1st and last element of the list
def swap(l):
    size = len(l)
    temp=l[0]                   #temp=l[3]
    l[0]=l[size-1]              #l[3]=l[4]
    l[size-1]=temp              #l[4]=temp
    return l

l=[10,20,30,40,50]

print(l)
print(swap(l))