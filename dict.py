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

for x in mydict:
    print(x)
for x in mydict:
    print(mydict[x])

print("Keys: ")
for keys in mydict.keys():
    print(keys)
    
print("Values: ")
for values in mydict.values():
    print(values)
    
print("Key-value pairs:")
for keys,values in mydict.items():
    print(keys,':',values)
    
if 'name' in mydict:
    print("'name' exists in dictionary")
else:
    print("'name' does not exist in dictionary")

mydict['age']=35
print("Modified age: ",mydict['age'])
mydict.update({'age':45})

mydict['color1']='fair'
print(mydict)
mydict.update({'color2':'Dark'})

removedvalue=mydict.pop('city')
print("Removed value: ",removedvalue)
print(mydict)
mydict.popitem()
print(mydict)

mydict.clear()
print("Dictionary after clear: ",mydict)

del mydict


family={
    'child1':{
        'name':'Alice',
        'year':2004
        },
    'child2':{
        'name':'Bob',
        'year':2007
        },
    'child3':{
        'name':'Charlie',
        'year':2011
        }
}

print(family)
print(family['child1']['name'])

for _ in family:
    print(family[_]['name'])
    print(family[_]['year'])
    
for x in family:
    print(family[x])
    
for x,obj in family.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])