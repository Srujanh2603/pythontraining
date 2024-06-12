#find the peak element in the list of integers.Peak element is an elementthat is greater than or equal to its neighbour element.
def peak(lst):
    if not lst:
        return None
    l=0
    r=len(lst)-1
    while(l<r):
        mid=l+(r-l)//2
        if lst[mid]<lst[mid+1]:
            l=mid+1
        else:
            r=mid
    return lst[l]
lst=[1,2,1,3,5,6,4]
print(peak(lst))