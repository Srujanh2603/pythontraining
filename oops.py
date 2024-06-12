def power(n,p):
    if p==0:
        return 1
    return (n*power(n,p-1))
n=5
p=2
print(power(n,p))

'''print
54321
5432
543
54
5
using recursion'''
n=5
def pattern(n,m):
    if n==0:
        return 