mt=(1,2,3)
another_tuple=tuple([4,5,6])
print(mt[0])
print(mt[-1])
print(mt[1:3])

combined_tuple=mt+another_tuple
print(combined_tuple)
repeat_tuple=mt*3
print(repeat_tuple)

print(2 in mt)
print(5 in mt)
print(len(mt))
for item in mt:
    print(item)
    
string_to_tuple=tuple('hello')
print(string_to_tuple)

list_to_tuple=tuple([1,2,3])
print(list_to_tuple)

print(mt.count(2))
print(mt.index(3))

tupleint=(2,9,4,0,2,5,6)
sorted_tuple=tuple(sorted(tupleint))
print(sorted_tuple)
reversed_tuple=tuple(sorted(tupleint, reverse=True))
print(reversed_tuple)

toft=((3,'apple'),(1,'orange'),(2,'banana'))
st=sorted(toft,key=lambda x:x[0])  #x[0] means 1,2.. x[1] means 'apple','orange'...
print(st)
st1=sorted(st,key=lambda x:x[1])
print(st1)

squaretuple=tuple(x**2 for x in range(1,6))
print(squaretuple)

#Zipping of tuples
l1=[1,2,3]
l2=['a','b','c']
zipped_tupple=tuple(zip(l1,l2))
print(zipped_tupple)

#Named tuples

from collections import namedtuple
import math
Point=namedtuple('Point',['x','y'])
p1=Point(1,2)
p2=Point(4,6)
print(p1)
print(p2)

distance=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
print("Distance: ",distance)

#filter and reduce function 

t=(1,2,3,4,5,6)
print(tuple(filter(lambda x:x%2==0,t)))
print(t)
def add(x,y):
    return x+y
from functools import reduce
print(reduce(add,t))
