'''3
     *
    **
   ***
  ****
 *****'''

n=int(input("Enter n:"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()