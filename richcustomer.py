#you are given an nxm integer grids where accounts are i j is the amount of money the ith customer has in the jth bank.the customers wealth is the amount of money they have in all the bank accounts. the richest customer is the customer that has the maximum wealth
def richestcustomer(accounts):
    maxwealth=0
    for customer in accounts:
        wealth=sum(customer)
        if wealth>maxwealth:
            maxwealth=wealth
    return maxwealth


if __name__ =="__main__":
    m=int(input("Enter the number of customers:"))
    n=int(input("Enter the number of banks:"))
    accounts=[]
    for i in range(m):
        print(f'Enter the wealth for customer {i+1} in {n} banks')
        cust_wealth=list(map(int,input().split()))
        accounts.append(cust_wealth)
        
print(richestcustomer(accounts))

