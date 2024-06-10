#factorial 
n=8
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print("Factorial is ",fact(n))