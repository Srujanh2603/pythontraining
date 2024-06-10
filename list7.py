#wap to merge 2 sorted lists into a single list
#Using sorted()
l1=[1,3,5,7,9]
l2=[2,4,6,8,10,11]
l3=sorted(l1+l2)
print(l3)

#Without using sorted()
def sortmerge(l1,l2):
    i=j=0
    l4=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l4.append(l1[i])
            i=i+1
        else:
            l4.append(l2[j])
            j=j+1
    l4.extend(l1[i:])
    l4.extend(l2[j:])      
    return l4
print(sortmerge(l1,l2))
