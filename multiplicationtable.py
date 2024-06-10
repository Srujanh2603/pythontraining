#multiplication table 
def table(n):
    for i in range(1,21):
        print("%d*%d=%d"%(n,i,n*i))
n=6
table(n)