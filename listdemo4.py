#Print sum and average of the values in the list
#Max and Min values
l=[10,15,20,30,35,40]
sum=0
for i in l:
    sum+=i
print(sum)
avg=sum/len(l)
print(avg)

print(l[0], l[-1])

l2=[23,43,12,56,43,67,54,33,99,5]
#l2.sort()
print(l2)
print(l2[0], l2[-1])
mini=l2[0]
maxi=l2[0]
for i in l2:
    if mini>i:
        mini=i
    if maxi<i:
        maxi=i
print(mini)
print(maxi)