#Given an array of n numbers and another number x.The task is to check whether or not there exists two elements in the array is exact sum is x.
x=int(input("Enter X:"))
arr=[1,-1,2,4,5]
def check(arr,x):
    for i in arr:
        for j in arr:
            if(i+j==x and i!=j):
                return True
    return False

print(check(arr,x))
    
