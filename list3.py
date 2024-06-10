#Find out the duplicate removal list product using list comprehension
def product(result):
    prod=1
    for i in result:
        prod*=i
    return prod
list=[1,2,3,3,5,6,5,6,1]
print("Original: ",list)
res=[]
[res.append(x) for x in list if x not in res]
product=product(res)
print("Product: ",product)
