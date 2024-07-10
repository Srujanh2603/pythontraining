#equlibrium program
def equlibrium_index(arr):
    n=len(arr)
    for i in range(n):
        lsum=sum(arr[:i])
        rsum=sum(arr[i+1:])
        if lsum==rsum:
            return i
    return -1

arr=[-7,1,5,2,-2,3,0]
print(equlibrium_index(arr))

#you are given an nxm integer grids where accounts are i j is the amount of money the ith customer has in the jth bank.the customers wealth is the amount of money they have in all the bank accounts. the richest customer is the customer that has the maximum wealth