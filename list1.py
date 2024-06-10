#Count the number of occurrences of given item in the lists

def count_occ(list, x):
    count=0
    for i in list:
        if i==x:
            count+=1
    return count

list=[1,2,3,4,5,6,7,8,9,10,2,4,5,3,5,4,5]
x=int(input("Number:"))
print(count_occ(list,x))