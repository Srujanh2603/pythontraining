#UNPACKING OF TUPLES
#tex=(10,20,30)
#(a,*b)=tex
#print(a,b)

def create_tuples():
    t1=(1,2,3,4,5)
    t2=('a', 'b', 'c', 'd', 'e')
    t3=('apple', 'orange', 'banana')
    return t1, t2, t3

def access_tuples(t1, t2):
    print("Tuple 1: ", t1)
    print("First element: ", t1[0])
    print("Second element: ", t1[1])
    print("Tuple 2: ", t2)
    print("Last element: ", t2[-1])
    print("Second last element: ", t2[-2])
    print(t1[0:5])

def unpack_t1(t3):
    (green,yellow,red)=t3
    print(green)
    print(yellow)
    print(red)
    
def unpack_t2(fruits):
    fruits=('apple','banana','cherry','strawberry','raspberry')
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)
    
def change_tuples(t1, t2):
    l1=list(t1)
    l2=list(t2)
    l1.append(6)
    l2.remove('c')
    t1=tuple(l1)
    t2=tuple(l2)
    return t1, t2

def loopthrough_tuple(t1):
    print('Looping through tuple 1 using for loop: ')
    for item in t1:
        print(item)
        
    print('Looping through tuple 2 using while loop and index numbers: ')
    index=0
    while index<len(t1):
        print(t1[index])
        index+=1
        
def join_tuples(t1, t2):
    t3=t1+t2
    return t3

t1, t2, t3=create_tuples()
access_tuples(t1,t2)
print()

unpack_t1(t3)
print()

fruits=('apple','banana','cherry','strawberry','raspberry')
unpack_t2(fruits)
print()

t1,t2=change_tuples(t1,t2)
print("After making changes")
access_tuples(t1,t2)
print()

t3=join_tuples(t1,t2)
print("Joined tuple",t3)