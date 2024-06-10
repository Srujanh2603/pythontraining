#Sort based on how close a number is to 50
#Customized sort
def fun(n):
    return abs(n-50)
thisl=[100,50,65,82,23]
thisl.sort(key=fun)
print(thisl)

thislist=['banana','Orange','cherry','Kiwi']
thislist.sort()
print(thislist)
thislist.sort(key=str.lower)
print(thislist)