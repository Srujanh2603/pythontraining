#wap to partition a list around a given value such that all elements less than the given value come before it and all elements greater than given value come after it
def partition(list,pivot):
    less=[x for x in list if x<pivot]
    equal=[x for x in list if x == pivot]
    great=[x for x in list if x > pivot]
    return less+equal+great

mylist=[3, 1, 4, 1, 5, 9, 2, 6, 5]
pivot=4
print("Partioned list:",partition(mylist,pivot))