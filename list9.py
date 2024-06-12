#find the largest sub-array sum of the given number
def large(mylist):
    maxsum=cursum=mylist[0]
    for i in mylist[1:]:
        cursum=max(i,cursum+i)
        maxsum=max(cursum,maxsum)
    return maxsum
mlist=[1,3,8,-2,6,-8,5]
print(large(mlist))    