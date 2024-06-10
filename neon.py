#neon no or not
num=int(input("Enter number: "))
sq=num*num
sum=0
temp=sq
while sq!=0:
    sum=sum+sq%10
    sq=sq//10
if sum==num:
    print("Neon number")
else:
    print("Not neon number")