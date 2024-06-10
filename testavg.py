#write a python prgm to find best of 2 test avg marks out of 3 test marks accepted by the user
m1=int(input("M1= "))
m2=int(input("M2= "))
m3=int(input("M3= "))
if m1>m2:
    if m2>m3:
        total=m1+m2
    else:
        total=m1+m3
elif m1>m3:
    total=m1+m2
else:
    total=m2+m3
avg=total/2
print("Average: ",avg)