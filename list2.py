#wap to count unique values in the lists
l=[10,15,20,30,35,40,15,10,30,25,40]
ul=[]
count=0
for i in l:
    if i not in ul:
        count+=1 
        ul.append(i)
print(ul)
print("Count: %d" % count)