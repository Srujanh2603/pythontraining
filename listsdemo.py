l1=["apple","banana","cherry","mango"]
l2=[10,20,30,40]
l3=[True, False]
l4=list(("Jack"))
l5=list(("Jack","John"))

print(l4)
print(l5)
print(l1[0])
print(l1[0:4])
print(l1[:4])
print(l1[0:])
print(l1[:])

print(l1[-4:-1])
print(l1[-1:-4])
x=len(l1)
print(x)
print(type(l1))
print(type(l1[0]))
if 'apple' in l1:
    print("yes")
l1[1]="Kiwi" 
print(l1)
l1[1:3]=["Pineapple","Dates","x"]
print(l1)     

l1[1:2]=["Cherry","Orange","Watermelon"]
print(l1)

l2[1:3]=[80]
print(l2)
l2.insert(0,100)
print(l2)
l2.append(70)
print(l2)
l1.extend(l2)
print(l1)

l1.remove("Watermelon")
print(l1)
l1.pop(4)
print(l1)
del l3
l4.clear()
print(l4)

thislist=['orange','apple','mango','pineapple']
for i in range(len(thislist)):
    print(thislist[i])
print('\r')
for x in thislist:
    print(x)
print('\r')
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1
print('\r')

#list comprehension [expr for expr in thislist if expr is not None]
y=[l1[i] for i in range(len(l1)) if l1[i] == 'apple']
print(y)
[print(l1[i]) for i in range(len(l1)) if l1[i] == 'Orange']

fruits = ['apple','orange','watermelon','kiwi']
newfruits = []
for x in fruits:
    if 'a' in x:
        newfruits.append(x)
print(newfruits)
print('\r')
newfruits=[x for x in fruits if 'a' not in x]
print(newfruits)
print('\r')
thislist.sort()
print(thislist)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
thislist.sort(reverse=True)
print(thislist)

marks=[90,48,59,67,100]
d=[]
for x in marks:
    y=abs(x-50)
    d.append(y)
print(d)
#marks.sort()

