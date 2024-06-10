'''11)
A A A A A
A A A A A 
A A A A A 
A A A A A        
A A A A A
Take user input'''

a=input("Enter Character: ")
n=int(input("Enter row:"))
k=int(input("Enter column:"))
for i in range(0,n):
    for j in range(0,k):
        print(a,end=" ")
    print("\r")
    