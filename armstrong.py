#write a pgm to check whether a number is armstong no. or not 
num=int(input())
temp=num
#print(num)
l=len(str(num))
sum=0
while temp > 0:
    digit=temp%10
    sum=sum+digit**l
    temp//=10
if num==sum:
    print(num, "is a Armstrong number")
else:
    print(num, "is not a Armstrong number")
