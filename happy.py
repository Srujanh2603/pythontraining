#happy no or not
'''def numsquaresum(n):
    num=0
    while(n):
        digit=n%10
        num=num+digit*digit
        n=n//10
    return num
def Happynum(n):
    st=set()
    st.add(n)
    while(True):
        if n==1:
            return True
        n=numsquaresum(n)
        if n in st:
            return False
        st.add(n)
    return False
n=23
if Happynum(n):
    print(True)
else:
    print(False)'''
    
def ishappy(n):
    sum=0
    while n!=0:
        r=n%10
        sum=sum+r**2
        n=n//10
    return sum
n=44
res=n
while res!=1 and res!=4:
    res=ishappy(res)
if res==1:
    print("yes")
else:
    print("no")