#to read a string from user and implement the logic to remove the characters which are at the odd numbers
#of the index
s=input()
a=''
for i in range(0,len(s),2):
    #if i%2==0:
        a=a+s[i]
print(a)