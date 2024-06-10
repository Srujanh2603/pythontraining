# Star pattern 1
#*****
#*****
#*****
#*****
#*****
''' Steps for pattern problem
1.See the number of rows and apply loop for it
2.See the no of colums and apply the loop
3.Check for any relationship btwn rows and columns
4.Print the pattern
5.Check for where to print spaces'''

n=int(input("Enter row:"))
k=int(input("Enter column:"))
for i in range(0,n):
    for j in range(0,k):
        print("*",end=" ")
    print()

