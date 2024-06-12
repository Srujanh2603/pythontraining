thisdict={
    'brand':'Ford',
    'model':'Mustang',
    'year': 1964
}

thisdict2=dict(namee='John',age=36,country='Norway')
print(thisdict2)

mydict={}

mydict['name']='Alice'
mydict['age']=30
mydict['city']='New York'

print("Initial dictionary: ",mydict)
print('name:',mydict['name'])
x=mydict.keys()
print(x)
y=mydict.values()
print(y)
z=mydict.items()
print(z)
m=mydict.get('city')
print(m)