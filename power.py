def power(n,p):
    if p==0:
        return 1
    return (n*power(n,p-1))
n=2
p=6
print(power(n,p))



def p(m,q):
    if q==1:
        return 2
    temp=p(m,q/2)
    if q%2!=0:
        return m*temp*temp
    else:
        return temp*temp
m=2
q=65
print(p(m,q))