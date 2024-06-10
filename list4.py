#wap to extract elements with the frequency greater than k
li=[1,2,3,2,3,4,5,4,5,6,5,6,7,8,2,1]
k=2
newlist=[]
for i in li:
    freq=li.count(i)
    if freq>k and i not in newlist:
        newlist.append(i)
print(newlist)