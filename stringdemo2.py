age=36
name='Rahul'
print(f'My name is {name}, Im {age}')

#reverse a string
str=input()

def str_reverse(str):
    rstr=''
    i=len(str)
    while i>0:
        rstr=rstr+str[i-1]
        i=i-1
    return rstr

reversed=str_reverse(str)
print(reversed)