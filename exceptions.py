try:
    num1=int(input())
    num2=int(input())
    res=num1/num2
    print(res)
except ValueError:
    print("Invalid")
except ZeroDivisionError:
    print("Invalid")
else:
    print("NO exception")
finally:
    print("end of prgm")
    
    
#convert to integer

def convert(string):
    try:
        n=int(string)
        print('Integer value: ',n)
    except ValueError:
        print("Invalid")
    
string=input("Enter a string")
print(string)
convert(string)

def getpositive():
    while True:
        try:
            num=int(input())
            if num<=0:
                raise ValueError("Not positive integer")
            return num
        except ValueError as e:
            print("error",e)
            
pi=getpositive()
print("You entered:",pi)

class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
    
try:
    raise MyCustomError("This is a custom error message")
except MyCustomError as e:
    print("Custom error:",e)
    
    
def access_list_element(l,i):
    try:
        value=l[i]
        print("value at index",i,'is:',value)
    except IndexError:
        print('Error index')
        
ml=[1,3,5]
i=int(input())
print(access_list_element(ml,i))


#File error
try:
    file=open('nonexistingfile.txt','r')
    content=file.read()
    file.close()
except FileNotFoundError:
    print("File not found")