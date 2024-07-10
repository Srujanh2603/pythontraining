#calculation not dependent on the input , O(1)
#single loop O(n)
#nested loop O(n2)

def access(arr,index):
    return arr[index]

arr=[1,2,3,4,5]
index=2
result=access(arr,index)
print(f'Element at index {index} is {result}')


#binary search

def search(arr,key):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return -1
arr=[1,2,3,4,5]
key=3
res=search(arr,key)
if res==-1:
    print("Not found")
else:
    print(f'Element found at index {res}')
    
def linearsearches(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

arr=[3,4,2,4,9,1,8]
key=4
r=linearsearches(arr,key)
if r==-1:
    print("Not found")
else:
    print(f'Element found at index {r}')
    
    
#Bubble Sort
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,2,7,4,9,3,1]
print("Sorted array: ",bubble(arr))

#selection sort
#selection sort repeatedly finds the minimum element from the unsorted part and swaps with the first unsorted element . O(n^2)
def selection(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
            arr[i],arr[min]=arr[min],arr[i]
    return arr

arr=[5,2,7,4,9,3,1,8,6]

print("Sorted array: ",selection(arr))

#insertion sort

def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[12,34,11,5,6,13]
print(insertion(arr))

#quick sort

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)-1]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+middle+quicksort(right)

arr=[12,34,11,5,6,13]
print("Given array is:",arr)
print("Sorted array: ",quicksort(arr))

