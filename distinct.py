#given an array of integers and number k. find the count of distinct elements in every window of size k in the array

def count_distinct_in_window(arr,n,k):
    result = []
    for i in range(n-k+1):
        window=arr[i:i+k]
        distinct_count=len(set(window))
        result.append(distinct_count)
    return result
n=int(input('Enter no of elements:'))
arr=[]
for _ in range(n):
    arr.append(int(input()))
k=int(input('Enter the size of the window'))
result = count_distinct_in_window(arr,n,k)
for count in result:
    print(count,end="\t")