#wap to test a list contains elements in the range
li=[3,4,2,5,6,7,8,11]
start=3
end=10
res=True
for i in li:
    if i<start or i>end:
        res=False
        break
print(res)
