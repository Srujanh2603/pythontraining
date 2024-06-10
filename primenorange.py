#prime no.s till n
count=0
for i in range(int(input("Enter start range: ")),int(input("Enter end range: "))+1):
    if i==1:
        continue
    for x in range(2,i):
        if(i%x==0):
            break
    else:
        print(i,end=" ")
        count+=1
print("\n Count= ",count)

