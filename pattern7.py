'''7)
1
22
333
4444
55555'''

n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
    
n=5
for i in range(n):
    for j in range(i+1):
        #if j<=i:
            print(j+1,end=' ')
    print()