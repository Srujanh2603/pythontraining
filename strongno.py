#Strong number-> the sum of factorial of individual digits is equal to the number itself
n=int(input("Enter a number"))
temp=n
sum=0
while(n):
    i=1
    fact=1
    rem=n%10
    while i<=rem :
        fact=fact*i
        i+=1
    sum=sum+fact
    n=n//10
if sum==temp:
    print("is a strong number")
else:
    print("is not a strong number")