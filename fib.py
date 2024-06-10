#fibonacci series of given number n
def fib(n):
    if n<0:
        print("invalid input")
    a=0
    b=1
    for i in range(1,n+1):
        if i>2:
            c=a+b
            a=b
            b=c
            print(b,end=' ') #end is delimiter
        if i==1:
            print(a,end=' ')
        if i==2:
            print(b,end=' ')     
n=int(input("Enter n: "))
fib(n)