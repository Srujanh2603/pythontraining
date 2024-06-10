#spy no or not
num=int(input("Enter number: "))
sum=0
prod=1
while num!=0:
    sum=sum+num%10
    prod=prod*num%10
    num=num//10
if sum==prod:
    print("Spy")
else:
    print("Not Spy")